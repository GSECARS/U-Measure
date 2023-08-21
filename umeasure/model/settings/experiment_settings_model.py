#!usr/bin/python
##############################################################################################
# File Name: experiment_settings_model.py
# Description: This file is used for the experiment settings model.
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

from dataclasses import dataclass, field
from qtpy.QtCore import QSettings


@dataclass
class ExperimentSettingsModel:
    """U-Measure experiment settings model."""

    settings: QSettings = field(repr=False, compare=False)
    
    _frequencies: list[float] = field(
        init=False, repr=False, compare=False, default_factory=lambda: []
    )
    _threshold: float = field(init=False, repr=False, compare=False, default=27.0)
    _repetitions: int = field(init=False, repr=False, compare=False, default=1)
    _file_number: int = field(init=False, repr=False, compare=False, default=1)
    _scan: str = field(init=False, repr=False, compare=False, default="A")
    _load: float = field(init=False, repr=False, compare=False, default=0.0)
    _temperature: float = field(init=False, repr=False, compare=False, default=0.0)

    def __post_init__(self) -> None:
        """Post-initialization method."""
        object.__setattr__(self, "_frequencies", self._convert_array())
        # Set threshold value
        threshold_value = self.settings.value("threshold", type=float)
        if threshold_value is None:
            threshold_value = 0.0
        object.__setattr__(self, "_threshold", threshold_value)
        # Set repetitions value
        repetitions_value = self.settings.value("repetitions", type=int)
        if repetitions_value is None:
            repetitions_value = 1
        object.__setattr__(self, "_repetitions", repetitions_value)
        # Set file number value
        file_number_value = self.settings.value("file_number", type=int)
        if file_number_value is None:
            file_number_value = 1
        object.__setattr__(self, "_file_number", file_number_value)
        # Set load value
        load_value = self.settings.value("load", type=float)
        if load_value is None:
            load_value = 0.0
        object.__setattr__(self, "_load", load_value)
        # Set temperature value
        temperature_value = self.settings.value("temperature", type=float)
        if temperature_value is None:
            temperature_value = 0.0
        object.__setattr__(self, "_temperature", temperature_value)

    def set_defaults(self) -> None:
        """Sets the default values for the experiment section."""
        object.__setattr__(self, "_frequencies", [20.0, 30.0, 40.0, 50.0, 60.0])
        object.__setattr__(self, "_threshold", 27)
        object.__setattr__(self, "_repetitions", 1)
        object.__setattr__(self, "_file_number", 1)
        object.__setattr__(self, "_scan", "A")
        object.__setattr__(self, "_load", 1)
        object.__setattr__(self, "_temperature", 1)

    def _convert_array(self) -> list[float]:
        """Converts the saved array to list[float]."""
        frequencies_list: list[float] = []
        saved_list = self.settings.value("frequencies")
        if saved_list is not None:
            frequencies_list = [float(frequency) for frequency in saved_list]

        return frequencies_list
   
    @property
    def frequencies(self) -> list[float]:
        """Returns the frequencies."""
        return self._frequencies
 
    @frequencies.setter
    def frequencies(self, value) -> None:
        """Sets the frequencies."""
        if isinstance(value, list):
            object.__setattr__(self, "_frequencies", value)
            self.settings.setValue("frequencies", self._frequencies)

    @property
    def threshold(self) -> float:
        """Returns the threshold."""
        return self._threshold

    @threshold.setter
    def threshold(self, value) -> None:
        """Sets the threshold."""
        if isinstance(value, float):
            object.__setattr__(self, "_threshold", value)
            self.settings.setValue("threshold", self._threshold)

    @property
    def repetitions(self) -> int:
        """Returns the repetitions."""
        return self._repetitions

    @repetitions.setter
    def repetitions(self, value) -> None:
        """Sets the repetitions."""
        if isinstance(value, int):
            object.__setattr__(self, "_repetitions", value)
            self.settings.setValue("repetitions", self._repetitions)

    @property
    def file_number(self) -> int:
        """Returns the file number."""
        return self._file_number


    @file_number.setter
    def file_number(self, value) -> None:
        """Sets the file number."""
        if isinstance(value, int):
            object.__setattr__(self, "_file_number", value)
            self.settings.setValue("file_number", self._file_number)

    @property
    def scan(self) -> str:
        """Returns the scan."""
        return self._scan

    @scan.setter
    def scan(self, value) -> None:
        """Sets the scan."""
        if isinstance(value, str):
            object.__setattr__(self, "_scan", value)
            self.settings.setValue("scan", self._scan)

    @property
    def load(self) -> float:
        """Returns the load."""
        return self._load

    @load.setter
    def load(self, value) -> None:
        """Sets the load."""
        if isinstance(value, float):
            object.__setattr__(self, "_load", value)
            self.settings.setValue("load", self._load)

    @property
    def temperature(self) -> float:
        """Returns the temperature."""
        return self._temperature
 
    @temperature.setter
    def temperature(self, value) -> None:
        """Sets the temperature."""
        if isinstance(value, float):
            object.__setattr__(self, "_temperature", value)
            self.settings.setValue("temperature", self._temperature)
