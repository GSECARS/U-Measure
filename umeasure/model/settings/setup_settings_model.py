#!usr/bin/python
##############################################################################################
# File Name: setup_settings_model.py
# Description: This file is used for the setup settings model.
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
class SetupSettingsModel:
    """U-Measure general setup settings model."""

    settings: QSettings = field(repr=False, compare=False)

    _mso: str = field(init=False, repr=False, compare=False, default="")
    _afg: str = field(init=False, repr=False, compare=False, default="")
    _cycle: str = field(init=False, repr=False, compare=False, default="")
    _run_number: str = field(init=False, repr=False, compare=False, default="")

    def __post_init__(self) -> None:
        """Post-initialization method."""
        object.__setattr__(self, "_mso", self.settings.value("mso", type=str))
        object.__setattr__(self, "_afg", self.settings.value("afg", type=str))
        object.__setattr__(self, "_cycle", self.settings.value("cycle", type=str))
        object.__setattr__(
            self, "_run_number", self.settings.value("run_number", type=str)
        )

    def set_defaults(self) -> None:
        """Sets the default values."""
        object.__setattr__(self, "mso", "164.54.160.105")
        object.__setattr__(self, "afg", "164.54.160.117")
        object.__setattr__(self, "cycle", "2022-2")
        object.__setattr__(self, "run_number", "D2711")

    @property
    def mso(self) -> str:
        """Returns the MSO."""
        return self._mso

    @mso.setter
    def mso(self, value: str) -> None:
        """Sets the MSO."""
        object.__setattr__(self, "_mso", value)
        self.settings.setValue("mso", self._mso)

    @property
    def afg(self) -> str:
        """Returns the AFG."""
        return self._afg

    @afg.setter
    def afg(self, value: str) -> None:
        """Sets the AFG."""
        object.__setattr__(self, "_afg", value)
        self.settings.setValue("afg", self._afg)

    @property
    def cycle(self) -> str:
        """Returns the cycle."""
        return self._cycle

    @cycle.setter
    def cycle(self, value: str) -> None:
        """Sets the cycle."""
        object.__setattr__(self, "_cycle", value)
        self.settings.setValue("cycle", self._cycle)

    @property
    def run_number(self) -> str:
        """Returns the run number."""
        return self._run_number

    @run_number.setter
    def run_number(self, value: str) -> None:
        """Sets the run number."""
        object.__setattr__(self, "_run_number", value)
        self.settings.setValue("run_number", self._run_number)
