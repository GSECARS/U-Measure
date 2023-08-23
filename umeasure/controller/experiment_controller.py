#!usr/bin/python
##############################################################################################
# File Name: experiment_controller.py
# Description: This file contains the controller logic for the experiment section.
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

from umeasure.model.settings import ExperimentSettingsModel
from umeasure.widget import ExperimentWidget


class ExperimentController:
    """Provides a way to control and connect the experiment widget with the experiment model."""

    def __init__(
        self, widget: ExperimentWidget, model: ExperimentSettingsModel
    ) -> None:
        self._model = model
        self._widget = widget

        self._update_experiment_values()
        self._connect_experiment_widgets()

    def _connect_experiment_widgets(self) -> None:
        """Connects experiment signals and slots."""
        self._widget.txt_frequencies.textChanged.connect(
            self._txt_frequencies_text_changed
        )
        self._widget.spin_threshold.textChanged.connect(
            self._spin_threshold_text_changed
        )
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
        self._widget.spin_repetitions.setValue(self._model.repetitions)
        self._widget.spin_file_number.setValue(self._model.file_number)
        self._widget.spin_load.setValue(self._model.load)
        self._widget.spin_temperature.setValue(self._model.temperature)
        self._widget.spin_threshold.setValue(self._model.threshold)
        self._widget.txt_scan.setText(self._model.scan)
        self._widget.spin_vpp.setValue(self._model.vpp)

        # Update frequencies text
        frequencies_str = ""
        if self._model.frequencies:
            for index, frequency in enumerate(self._model.frequencies):
                frequencies_str += str(frequency)
                if not index == len(self._model.frequencies) - 1:
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
        self._model.frequencies = frequencies_list

    def _spin_threshold_text_changed(self) -> None:
        """Updates the current threshold value based on user input."""
        self._model.threshold = float(self._widget.spin_threshold.text())

    def _check_repeated_changed(self, state) -> None:
        """Updates the current repeat value based on user input."""
        if state == 0:
            self._model.repeat = False
        else:
            self._model.repeat = True

    def _txt_scan_text_changed(self) -> None:
        """Updates the current scan value based on user input."""
        self._model.scan = self._widget.txt_scan.text()

    def _spin_repetitions_value_changed(self) -> None:
        """Updates the current repetitions value based on user input."""
        self._model.repetitions = self._widget.spin_repetitions.value()

    def _spin_file_number_value_changed(self) -> None:
        """Updates the current file number value based on user input."""
        self._model.file_number = self._widget.spin_file_number.value()

    def _spin_load_value_changed(self) -> None:
        """Updates the current load value based on user input."""
        self._model.load = self._widget.spin_load.value()

    def _spin_temperature_value_changed(self) -> None:
        """Updates the current temperature value based on user input."""
        self._model.temperature = self._widget.spin_temperature.value()
