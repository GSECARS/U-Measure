# !/usr/bin/python3
# ----------------------------------------------------------------------
# U-Measure - A GUI software for ultrasonic data collection.
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# Copyright (C) 2022  GSECARS, The University of Chicago
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
# ----------------------------------------------------------------------

from pathlib import Path
from qtpy.QtWidgets import (
    QGroupBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QAbstractSpinBox,
)
from qtpy.QtCore import Qt, QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

from measure.model import PathModel


class ExperimentWidget(QGroupBox):
    """Experiment widget groupbox to be used in the MainWidget."""

    def __init__(self, model: PathModel) -> None:
        super(ExperimentWidget, self).__init__()

        self._qss = Path(model.qss_path, "experiment_group.qss").as_posix()

        # Initialize experiment group's widgets
        self._lbl_frequencies = QLabel("Frequencies")
        self._lbl_threshold = QLabel("Threshold")
        self._lbl_reset = QLabel("Reset")
        self._lbl_repetitions = QLabel("Repetitions")
        self._lbl_scan = QLabel("Scan")
        self._lbl_file_number = QLabel("#File")
        self._lbl_cycles = QLabel("Cycles")
        self._lbl_vpp = QLabel("Vpp")
        self.txt_frequencies = QLineEdit()
        self.txt_threshold = QLineEdit()
        self.txt_reset = QLineEdit()
        self.txt_scan = QLineEdit()
        self.spin_repetitions = QSpinBox()
        self.spin_cycles = QSpinBox()
        self.spin_file_number = QSpinBox()
        self.spin_vpp = QDoubleSpinBox()

        # List of experiment group's widgets
        self._experiment_widgets = [
            self._lbl_frequencies,
            self._lbl_threshold,
            self._lbl_reset,
            self._lbl_repetitions,
            self._lbl_scan,
            self._lbl_file_number,
            self._lbl_cycles,
            self._lbl_vpp,
            self.txt_frequencies,
            self.txt_threshold,
            self.txt_reset,
            self.txt_scan,
            self.spin_repetitions,
            self.spin_cycles,
            self.spin_file_number,
            self.spin_vpp,
        ]

        # Run experiment group's widget methods
        self._configure_experiment_group()
        self._configure_experiment_labels()
        self._configure_experiment_text_boxes()
        self._configure_experiment_spin_boxes()
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
        self.setStyleSheet(open(self._qss, "r").read())

    def _configure_experiment_labels(self) -> None:
        """Configuration of the experiment group's labels."""
        labels = [
            self._lbl_frequencies,
            self._lbl_threshold,
            self._lbl_reset,
            self._lbl_repetitions,
            self._lbl_scan,
            self._lbl_file_number,
            self._lbl_cycles,
            self._lbl_vpp,
        ]
        [label.setObjectName("lbl-experiment") for label in labels]

    def _configure_experiment_text_boxes(self) -> None:
        """Configuration of the experiment group's text boxes."""
        self.txt_frequencies.setObjectName("txt-experiment")
        self.txt_threshold.setObjectName("txt-experiment")
        self.txt_scan.setObjectName("txt-experiment")
        self.txt_reset.setObjectName("txt-experiment")

        # Validator for frequencies.
        expression = QRegularExpression("^(((?:0|[1-9][0-9]*)\.[0-9]+)*\, )*$")
        validator = QRegularExpressionValidator(expression)
        self.txt_frequencies.setValidator(validator)

        # Validator for threshold frequency
        single_expression = QRegularExpression("^((?:0|[1-9][0-9]*)\.[0-9]+)$")
        single_validator = QRegularExpressionValidator(single_expression)
        self.txt_threshold.setValidator(single_validator)
        self.txt_reset.setValidator(single_validator)

        self.txt_threshold.setMaximumWidth(52)
        self.txt_reset.setMaximumWidth(52)
        self.txt_scan.setMinimumWidth(200)

        self.txt_frequencies.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.txt_threshold.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.txt_reset.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.txt_scan.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def _configure_experiment_spin_boxes(self) -> None:
        """Configuration of the experiment group's spin boxes."""
        spin_boxes = [
            self.spin_repetitions,
            self.spin_cycles,
            self.spin_file_number,
        ]
        for spin_box in spin_boxes:
            spin_box.setObjectName("spin-experiment")
            spin_box.setAlignment(Qt.AlignCenter)
            spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.spin_repetitions.setMinimum(1)
        self.spin_repetitions.setMaximum(10000)
        self.spin_repetitions.setSingleStep(1)

        self.spin_cycles.setMinimum(1)
        self.spin_cycles.setMaximum(10)
        self.spin_cycles.setSingleStep(1)

        self.spin_file_number.setMinimum(1)
        self.spin_file_number.setMaximum(100000)
        self.spin_file_number.setSingleStep(10)

        self.spin_vpp.setObjectName("spin-vpp")
        self.spin_vpp.setMinimum(0.0)
        self.spin_vpp.setMaximum(5.0)
        self.spin_vpp.setSingleStep(0.1)
        self.spin_vpp.setDecimals(1)
        self.spin_vpp.setAlignment(Qt.AlignCenter)
        self.spin_vpp.setButtonSymbols(QAbstractSpinBox.NoButtons)

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
        frequencies_layout.addWidget(self.txt_threshold)
        frequencies_layout.addWidget(self._lbl_reset)
        frequencies_layout.addWidget(self.txt_reset)
        experiment_layout.addLayout(frequencies_layout, 0, 0, 1, 6)

        # layout for load and temperature
        load_temperature_layout = QHBoxLayout()
        load_temperature_layout.setContentsMargins(0, 0, 0, 0)
        load_temperature_layout.addWidget(self._lbl_cycles)
        load_temperature_layout.addWidget(self.spin_cycles)
        load_temperature_layout.addWidget(self._lbl_vpp)
        load_temperature_layout.addWidget(self.spin_vpp)
        load_temperature_layout.addWidget(self._lbl_repetitions)
        load_temperature_layout.addWidget(self.spin_repetitions)
        load_temperature_layout.addStretch(1)
        load_temperature_layout.addWidget(self._lbl_file_number)
        load_temperature_layout.addWidget(self.spin_file_number)
        load_temperature_layout.addWidget(self._lbl_scan)
        load_temperature_layout.addWidget(self.txt_scan)
        experiment_layout.addLayout(load_temperature_layout, 1, 0, 1, 6)

        self.setLayout(experiment_layout)
