#!/usr/bin/python3
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

from qtpy.QtCore import QSettings

from measure.model import ExperimentModel
from measure.widget.groups import ExperimentWidget


class ExperimentController:
    """Provides a way to control and connect the experiment widget with the experiment model."""

    def __init__(self, widget: ExperimentWidget, settings: QSettings) -> None:
        self.model = ExperimentModel(settings=settings)
        self._widget = widget

        self._update_experiment_values()
        self._connect_experiment_widgets()

    def _connect_experiment_widgets(self) -> None:
        """Connects experiment signals and slots."""
        self._widget.txt_frequencies.textChanged.connect(
            self._txt_frequencies_text_changed
        )
        self._widget.txt_threshold.textChanged.connect(self._txt_threshold_text_changed)
        self._widget.txt_reset.textChanged.connect(self._txt_reset_text_changed)
        self._widget.txt_scan.textChanged.connect(self._txt_scan_text_changed)
        self._widget.spin_repetitions.valueChanged.connect(
            self._spin_repetitions_value_changed
        )
        self._widget.spin_file_number.valueChanged.connect(
            self._spin_file_number_value_changed
        )
        self._widget.spin_load.valueChanged.connect(self._spin_load_value_changed)
        self._widget.spin_temperature.valueChanged.connect(
            self._spin_temperature_value_changed
        )

    def _update_experiment_values(self) -> None:
        """Update the experiment GUI values."""
        self._widget.spin_repetitions.setValue(self.model.repetitions)
        self._widget.spin_file_number.setValue(self.model.file_number)
        self._widget.spin_load.setValue(self.model.load)
        self._widget.spin_temperature.setValue(self.model.temperature)
        self._widget.txt_threshold.setText(str(self.model.threshold))
        self._widget.txt_reset.setText(str(self.model.reset_frequency))
        self._widget.txt_scan.setText(self.model.scan)

        # Update frequencies text
        frequencies_str = ""
        if self.model.frequencies:
            for index, frequency in enumerate(self.model.frequencies):

                frequencies_str += str(frequency)
                if not index == len(self.model.frequencies) - 1:
                    frequencies_str += ", "

            self._widget.txt_frequencies.setText(frequencies_str)

    def _txt_frequencies_text_changed(self) -> None:
        """Converts the user input to list[float]."""
        frequencies_list: list[float] = []
        frequencies_str_list = self._widget.txt_frequencies.text().strip().split(",")

        # Covert to float
        for frequency in frequencies_str_list:
            frequency = frequency.strip()
            if frequency != "":
                frequencies_list.append(float(frequency))

        # Update current array
        self.model.frequencies = frequencies_list

    def _txt_threshold_text_changed(self) -> None:
        """Updates the current threshold value based on user input."""
        self.model.threshold = float(self._widget.txt_threshold.text())

    def _txt_reset_text_changed(self) -> None:
        """Updates the current reset frequency based on user input."""
        self.model.reset_frequency = float(self._widget.txt_reset.text())

    def _check_repeated_changed(self, state) -> None:
        """Updates the current repeat value based on user input."""
        if state == 0:
            self.model.repeat = False
        else:
            self.model.repeat = True

    def _txt_scan_text_changed(self) -> None:
        """Updates the current scan value based on user input."""
        self.model.scan = self._widget.txt_scan.text()

    def _spin_repetitions_value_changed(self) -> None:
        """Updates the current repetitions value based on user input."""
        self.model.repetitions = self._widget.spin_repetitions.value()

    def _spin_file_number_value_changed(self) -> None:
        """Updates the current file number value based on user input."""
        self.model.file_number = self._widget.spin_file_number.value()

    def _spin_load_value_changed(self) -> None:
        """Updates the current load value based on user input."""
        self.model.load = self._widget.spin_load.value()

    def _spin_temperature_value_changed(self) -> None:
        """Updates the current temperature value based on user input."""
        self.model.temperature = self._widget.spin_temperature.value()
