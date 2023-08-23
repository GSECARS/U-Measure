#!usr/bin/python
##############################################################################################
# File Name: experiment_widget.py
# Description: This file contains the experiment groupbox widget.
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
from qtpy.QtWidgets import QGroupBox, QGridLayout, QHBoxLayout
from gsewidgets import (
    Label,
    NoWheelNumericSpinBox,
    MultiFloatInputBox,
    FileNameInputBox,
)

from umeasure.model import PathModel


class ExperimentWidget(QGroupBox):
    """Experiment widget groupbox to be used in the MainWidget."""

    def __init__(self, paths: PathModel) -> None:
        super(ExperimentWidget, self).__init__()

        self._paths = paths

        # Initialize experiment group's widgets
        self._lbl_frequencies = Label("Frequencies", object_name="lbl-experiment")
        self._lbl_threshold = Label("Threshold", object_name="lbl-experiment")
        self._lbl_repetitions = Label("Repetitions", object_name="lbl-experiment")
        self._lbl_scan = Label("Scan", object_name="lbl-experiment")
        self._lbl_file_number = Label("#File", object_name="lbl-experiment")
        self._lbl_load = Label("Load (tons)", object_name="lbl-experiment")
        self._lbl_temperature = Label("Temperature (K)", object_name="lbl-experiment")
        self.txt_frequencies = MultiFloatInputBox(
            placeholder="e.g. 25, 27.0, 0.2", object_name="txt-experiment"
        )
        self.txt_scan = FileNameInputBox(object_name="txt-experiment")
        self.spin_repetitions = NoWheelNumericSpinBox(
            min_value=1,
            max_value=10000,
            default_value=1,
            incremental_step=1,
            object_name="spin-experiment",
        )
        self.spin_file_number = NoWheelNumericSpinBox(
            min_value=1,
            max_value=100000,
            default_value=1,
            incremental_step=10,
            object_name="spin-experiment",
        )
        self.spin_load = NoWheelNumericSpinBox(
            min_value=0.0,
            max_value=900.0,
            default_value=0.0,
            incremental_step=10.0,
            precision=1,
            object_name="spin-experiment",
        )
        self.spin_temperature = NoWheelNumericSpinBox(
            min_value=0.0,
            max_value=3000.0,
            default_value=0.0,
            incremental_step=100.0,
            precision=1,
            object_name="spin-experiment",
        )
        self.spin_threshold = NoWheelNumericSpinBox(
            min_value=0.0,
            max_value=10000000.0,
            default_value=27.00,
            incremental_step=1,
            precision=2,
            object_name="spin-experiment",
        )

        # List of experiment group's widgets
        self._experiment_widgets = [
            self._lbl_frequencies,
            self._lbl_threshold,
            self._lbl_repetitions,
            self._lbl_scan,
            self._lbl_file_number,
            self._lbl_load,
            self._lbl_temperature,
            self.txt_frequencies,
            self.txt_scan,
            self.spin_repetitions,
            self.spin_file_number,
            self.spin_load,
            self.spin_temperature,
            self.spin_threshold,
        ]

        # Run experiment group's widget methods
        self._configure_experiment_group()
        self._layout_experiment_widgets()

    def disable(self) -> None:
        """Disables all experiment group's widgets."""
        [widget.setEnabled(False) for widget in self._experiment_widgets]

    def enable(self) -> None:
        """Enables all experiment group's widgets."""
        [widget.setEnabled(True) for widget in self._experiment_widgets]

    def _configure_experiment_group(self) -> None:
        """Configuration of the experiment groupbox."""
        # Set group object name
        self.setObjectName("group-experiment")

        # Set the stylesheet from assets/qss/experiment_group.qss
        self.setStyleSheet(
            open(os.path.join(self._paths.qss_path, "experiment_group.qss"), "r").read()
        )

    def _layout_experiment_widgets(self) -> None:
        """Sets the layout for the experiment group widgets."""
        # Main experiment layout
        experiment_layout = QGridLayout()
        experiment_layout.setContentsMargins(0, 0, 0, 0)

        # layout for frequency widgets
        frequencies_layout = QHBoxLayout()
        frequencies_layout.setContentsMargins(0, 0, 0, 0)
        frequencies_layout.addWidget(self._lbl_frequencies)
        frequencies_layout.addWidget(self.txt_frequencies)
        frequencies_layout.addWidget(self._lbl_threshold)
        frequencies_layout.addWidget(self.spin_threshold)
        experiment_layout.addLayout(frequencies_layout, 0, 0, 1, 6)

        # layout for load and temperature
        load_temperature_layout = QHBoxLayout()
        load_temperature_layout.setContentsMargins(0, 0, 0, 0)
        load_temperature_layout.addWidget(self._lbl_load)
        load_temperature_layout.addWidget(self.spin_load)
        load_temperature_layout.addWidget(self._lbl_temperature)
        load_temperature_layout.addWidget(self.spin_temperature)
        load_temperature_layout.addWidget(self._lbl_repetitions)
        load_temperature_layout.addWidget(self.spin_repetitions)
        load_temperature_layout.addStretch(1)
        load_temperature_layout.addWidget(self._lbl_file_number)
        load_temperature_layout.addWidget(self.spin_file_number)
        load_temperature_layout.addWidget(self._lbl_scan)
        load_temperature_layout.addWidget(self.txt_scan)
        experiment_layout.addLayout(load_temperature_layout, 1, 0, 1, 6)

        self.setLayout(experiment_layout)
