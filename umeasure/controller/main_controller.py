#!usr/bin/python
##############################################################################################
# File Name: main_controller.py
# Description: This file contains the controller logic for the U-Measure application.
#
# Attribution:
# - This file is part of the U-Measure project.
#
# License: GPL-3.0
#
# U-Measure
#
# Copyright (c) 2023 Christofanis Skordas
# Copyright (c) 2023 GSECARS, The University of Chicago
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##############################################################################################

import datetime
import sys
from qtpy.QtWidgets import QApplication, QMessageBox
from qtpy.QtCore import QSettings, QObject, Signal, QTimer, Qt

from umeasure.model import MainModel, QtWorkerModel
from umeasure.widget import MainWidget
from umeasure.widget.custom import MsgBox
from umeasure.controller import SetupController, ExperimentController, VisaController


class MainController(QObject):
    """Used to connect all controllers, models and widgets."""

    # Signals
    collect_triggered: Signal = Signal()
    abort_triggered: Signal = Signal()
    finished: Signal = Signal()

    def __init__(self) -> None:
        super(MainController, self).__init__()
        self._app = QApplication(sys.argv)
        self._model = MainModel()
        self._settings = QSettings("GSECARS", "U-Measure")
        self._widget = MainWidget(paths=self._model.paths)

        # Main application thread
        self._main_worker = QtWorkerModel(self._thread_methods, ())

        # Setup controller
        self._setup_controller = SetupController(
            widget=self._widget.setup, model=self._model.settings.setup
        )

        # Experiment controller
        self._experiment_controller = ExperimentController(
            widget=self._widget.experiment, model=self._model.settings.experiment
        )

        # Visa controller
        self._visa_controller = VisaController(
            setup_settings=self._model.settings.setup,
            experiment_settings=self._model.settings.experiment,
            basedir=self._setup_controller.basedir,
        )

        # Connect the signal and slot for the main widget settings
        self._widget.close_event_changed.connect(self._close_event_triggered)

        # Helpers
        self._collecting = False
        self._aborting = False
        self._input_check_passed = True
        self._start_time = None

        # Timer
        self._main_timer = QTimer()
        self._main_timer.setInterval(30)

        # Run methods
        self._configure_main_controller()
        self._configure_widgets()
        self._connect_widgets()

    def _close_event_triggered(self) -> None:
        """Saves the main application window size, position and state."""
        # If the window is maximized, save the maximized state, otherwise save the normal state
        # and the window size and position
        if self._widget.windowState() == Qt.WindowState.WindowMaximized:
            self._model.settings.sizing.window_state = 1
        else:
            self._model.settings.sizing.window_state = 0
            # Window size
            self._model.settings.sizing.window_size = self._widget.size()
            # Window position
            self._model.settings.sizing.window_position = self._widget.pos()

    def _configure_main_controller(self) -> None:
        """Basic configuration for functionality of the main controller."""
        # Start the main application thread
        self._main_worker.start()

    def _configure_widgets(self) -> None:
        """Sets some configuration values before opening the main application window."""
        # Set initial focus
        self._widget.setup.lbl_path.setFocus()

    def _connect_widgets(self) -> None:
        """Connects signals and slots for some, of the available, widgets."""
        self._visa_controller.new_feedback_message.connect(
            self._visa_controller_message
        )
        self._visa_controller.current_repetition.connect(
            self._change_current_repetition
        )

        self._main_timer.timeout.connect(self._timer_ticks)
        self._widget.control_status.btn_collection.clicked.connect(
            self._btn_collection_clicked
        )
        self.collect_triggered.connect(self._change_to_collecting)
        self.abort_triggered.connect(self._change_to_aborting)
        self.finished.connect(self._change_to_idle)

    def disable_widgets(self) -> None:
        """Disables setup and experiment widgets."""
        self._widget.setup.disable()
        self._widget.experiment.disable()

    def enable_widgets(self) -> None:
        """Enables setup and experiment widgets."""
        self._widget.setup.enable()
        self._widget.experiment.enable()

    def _timer_ticks(self) -> None:
        """Timer tick timeout method."""
        elapsed_time = datetime.datetime.now() - self._start_time
        current_delta = datetime.timedelta(seconds=elapsed_time.seconds)
        self._widget.control_status.lbl_time.setText(str(current_delta))

    def _change_to_collecting(self) -> None:
        """Changes the collection status to collecting."""
        self.disable_widgets()

        self._append_feedback(message="Starting new collection process.")

        self._widget.control_status.lbl_status.setText("Collecting")
        self._widget.control_status.btn_collection.setText("Abort")

        self._widget.control_status.lbl_status.setEnabled(False)
        self._widget.control_status.lbl_time.setEnabled(False)
        self._widget.control_status.lbl_repetition_status.setEnabled(False)

        self._widget.control_status.lbl_repetition_status.setVisible(True)

    def _change_to_idle(self) -> None:
        """Changes the collection status to idle."""
        self.enable_widgets()
        self._aborting = False
        self._collecting = False

        self._widget.control_status.lbl_status.setText("Idle")
        self._widget.control_status.btn_collection.setText("Collect")

        self._widget.control_status.lbl_status.setEnabled(True)
        self._widget.control_status.lbl_time.setEnabled(True)
        self._widget.control_status.lbl_repetition_status.setEnabled(True)

        self._widget.control_status.lbl_repetition_status.setVisible(False)

        self._main_timer.stop()

    def _change_to_aborting(self) -> None:
        """Changes the collection status to aborting."""
        self._widget.control_status.lbl_status.setText("Aborting")
        self._aborting = True

    def _change_current_repetition(self, repetition: int) -> None:
        """Changes the current status text of the repetitions."""
        self._widget.control_status.lbl_repetition_status.setText(
            f"{repetition}/{self._experiment_controller.model.repetitions}"
        )

    def _check_for_empty_txt_boxes(self, field_name: str, text: str) -> bool:
        """Looks for empty text boxes."""
        if text.strip() == "":
            message = f"The {field_name} field can't be empty. Please try again."
            self._append_feedback(message)
            MsgBox(msg=message)

            self._input_check_passed = False

        return self._input_check_passed

    def _check_for_valid_ip(self, field_name: str, ip: str) -> bool:
        """Checks if the input is a valid IPv4."""
        sections = ip.split(".")

        if len(sections) != 4:
            self._input_check_passed = False

        for section in sections:
            if not isinstance(int(section), int):
                self._input_check_passed = False

            if int(section) < 0 or int(section) > 255:
                self._input_check_passed = False

        if not self._input_check_passed:
            message = f"The {field_name} must be a valid IPv4. Please try again."
            self._append_feedback(message)
            MsgBox(msg=message)

        return self._input_check_passed

    def _check_input_before_collection(self) -> None:
        """Runs the check methods before starting a collection."""

        if not self._check_for_empty_txt_boxes(
            field_name="MSO", text=self._setup_controller.model.mso
        ):
            return None

        if not self._check_for_empty_txt_boxes(
            field_name="AFG", text=self._setup_controller.model.afg
        ):
            return None

        if not self._check_for_empty_txt_boxes(
            field_name="Cycle", text=self._setup_controller.model.cycle
        ):
            return None

        if not self._check_for_empty_txt_boxes(
            field_name="#Run", text=self._setup_controller.model.run_number
        ):
            return None

        if not self._check_for_empty_txt_boxes(
            field_name="Threshold",
            text=str(self._experiment_controller.model.threshold),
        ):
            return None

        if self._experiment_controller.model.repetitions > 1:
            if not self._check_for_empty_txt_boxes(
                field_name="Scan", text=self._experiment_controller.model.scan
            ):
                return None

        if not self._check_for_valid_ip(
            field_name="MSO", ip=self._setup_controller.model.mso
        ):
            return None

        if not self._check_for_valid_ip(
            field_name="AFG", ip=self._setup_controller.model.afg
        ):
            return None

    def _btn_collection_clicked(self) -> None:
        """Starts/stops a collection on button click."""
        if self._collecting:
            self.abort_triggered.emit()
            return None

        self._input_check_passed = True
        self._check_input_before_collection()

        if not self._input_check_passed:
            return None

        _msg_question = QMessageBox.question(
            self._widget,
            "Collection confirmation",
            f"The load and temperature of the experiment are {self._experiment_controller.model.load} tons and\n"
            f"{self._experiment_controller.model.temperature} K, respectively.\n\n"
            f"Are you sure you want to continue with the collection?",
        )

        if _msg_question != QMessageBox.Yes:
            return None

        self.collect_triggered.emit()
        self._start_time = datetime.datetime.now()
        self._main_timer.start(100)
        self._collecting = True
        self._main_timer.start()

    def _thread_methods(self) -> None:
        """Runs the thread methods."""
        while not self._widget.close_triggered:
            self._collection_process()

        # Set the threads finished flag to True, so the application can close.
        self._widget.threads_finished = True

    def _collection_process(self) -> None:
        """Collection process."""
        if self._collecting:
            self._visa_controller.connect()
            self._visa_controller.collect_data(abort_status=self._aborting)
            self.finished.emit()

        self._visa_controller.restore_defaults()

    def _visa_controller_message(self, message: str):
        """Adds some information on the feedback section."""
        self._append_feedback(message=message)

    def _append_feedback(self, message: str):
        """Adds a new line with the input text on the feedback text widget."""
        self._widget.group_widget.control_status.txt_feedback.appendPlainText(
            f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {message}"
        )

    def run(self, version: str) -> None:
        """Runs the main application window."""
        # Log the application start
        self._model.logger.operation_log.info(f"U-Measure v{version} started.")

        # Display the main application window
        self._widget.display_window(
            version=version,
            window_size=self._model.settings.sizing.window_size,
            window_position=self._model.settings.sizing.window_position,
            window_state=self._model.settings.sizing.window_state,
        )

        # Set the application exit code
        sys.exit(self._app.exec())
