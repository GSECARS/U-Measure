#!usr/bin/python
##############################################################################################
# File Name: main_widget.py
# Description: This file contains the main application widget.
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

import os
from qtpy.QtCore import QObject, Signal, QSize, QPoint, Qt, QEvent
from qtpy.QtGui import QCloseEvent, QIcon
from qtpy.QtWidgets import QMainWindow, QFrame, QMessageBox, QGridLayout
from typing import Optional

from umeasure.model import PathModel
from umeasure.widget import SetupWidget, ExperimentWidget, ControlStatusWidget


class MainWidget(QMainWindow, QObject):
    """This is used as the main application window."""

    # Signals
    close_event_changed: Signal = Signal()

    def __init__(self, paths: PathModel) -> None:
        super(MainWidget, self).__init__()

        # Paths
        self._paths = paths

        # Section widgets
        self.setup = SetupWidget(paths=self._paths)
        self.experiment = ExperimentWidget(paths=self._paths)
        self.control_status = ControlStatusWidget(paths=self._paths)

        # Main frame widget
        self._main_frame = QFrame()

        # Event helpers
        self._close_triggered: bool = False
        self._threads_finished: bool = False

        # Run methods
        self._configure_main_window()

    def display_window(
        self,
        version: str,
        window_size: Optional[QSize] = None,
        window_position: Optional[QPoint] = None,
        window_state: Optional[int] = None,
    ) -> None:
        """Sets the main application window's properties and displays the application main window."""
        # Set the Window Title
        self.setWindowTitle(f"U-Measure v{version}")
        # Set the application icon
        self.setWindowIcon(
            QIcon(os.path.join(self._paths.icon_path, "ultrasonic_icon.ico"))
        )
        # Set the central widget
        self.setCentralWidget(self._main_frame)
        # Set application object name
        self.setObjectName("main-widget")
        # Set the stylesheet from assets/qss/main_widget.qss
        self.setStyleSheet(
            open(os.path.join(self._paths.qss_path, "main_widget.qss"), "r").read()
        )

        # Resize the main application window
        if window_size is not None:
            self.resize(window_size)

        # Move the main application on the screen
        if window_position is not None:
            self.move(window_position)

        # Display the main application window based on the window state
        if window_state == 1:
            self.showMaximized()
        else:
            # Show the main application window
            self.showNormal()

    def _configure_main_window(self) -> None:
        """Configures the layout for the main application window."""
        # Main frame layout
        main_frame_layout = QGridLayout()
        main_frame_layout.setRowStretch(2, 1)
        main_frame_layout.addWidget(self.setup, 0, 0, 1, 1)
        main_frame_layout.addWidget(self.experiment, 1, 0, 1, 1)
        main_frame_layout.addWidget(self.control_status, 2, 0, 1, 1)

        # Set the main frame layout
        self._main_frame.setLayout(main_frame_layout)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Creates a message box for exit confirmation if closeEvent is triggered."""
        _msg_question = QMessageBox.question(
            self,
            "Exit confirmation",
            "Are you sure you want to close the application?",
            defaultButton=QMessageBox.No,
        )

        if _msg_question == QMessageBox.Yes:
            # Emit the application close event changed signal, to update the main window settings.
            self.close_event_changed.emit()

            # Make sure that all threads and methods are aborted before closing the application.
            self._close_triggered = True
            while not self._threads_finished:
                continue

            # Close the application
            event.accept()
        else:
            event.ignore()

    def changeEvent(self, event: QEvent) -> None:
        """Updates the state of the window on changes"""
        if event.type() == QEvent.WindowStateChange:
            # Center the window to screen after
            if event.oldState() & Qt.WindowState.WindowMaximized:
                center = self.screen().availableGeometry().center()

                # Position the window in the middle of the active screen
                x = int(center.x() - self.width() / 2)
                y = int(center.y() - self.height() / 2)
                self.setGeometry(x, y, 800, 600)

    @property
    def close_triggered(self) -> bool:
        """Returns True if the close event was triggered."""
        return self._close_triggered

    @property
    def threads_finished(self) -> bool:
        """Returns True if all threads are finished."""
        return self._threads_finished

    @threads_finished.setter
    def threads_finished(self, value: bool) -> None:
        """Sets the threads_finished attribute."""
        self._threads_finished = value
