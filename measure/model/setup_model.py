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

from dataclasses import dataclass, field
from qtpy.QtCore import QSettings


@dataclass(frozen=False, slots=True)
class SetupModel:
    """Dataclass that holds all necessary data information for the setup section."""

    settings: QSettings = field(init=True, repr=False, compare=False)

    _mso: str = field(init=False, repr=False, compare=False, default="")
    _afg: str = field(init=False, repr=False, compare=False, default="")
    _hutch: str = field(init=False, repr=False, compare=False, default="")
    _cycle: str = field(init=False, repr=False, compare=False, default="")
    _institution: str = field(init=False, repr=False, compare=False, default="")
    _run_number: str = field(init=False, repr=False, compare=False, default="")
    _vpp: float = field(init=False, repr=False, compare=False, default=0.0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_mso", self.settings.value("mso", type=str))
        object.__setattr__(self, "_afg", self.settings.value("afg", type=str))
        object.__setattr__(self, "_hutch", self.settings.value("hutch", type=str))
        object.__setattr__(self, "_cycle", self.settings.value("cycle", type=str))
        object.__setattr__(
            self, "_institution", self.settings.value("institution", type=str)
        )
        object.__setattr__(
            self, "_run_number", self.settings.value("run_number", type=str)
        )

        # Set vpp value
        vpp_value = float(self.settings.value("vpp", type=float))
        if vpp_value is None:
            vpp_value = 0.0
        object.__setattr__(self, "_vpp", vpp_value)

    def set_setup_defaults(self) -> None:
        """Sets the default values for the setup section."""
        object.__setattr__(self, "mso", "164.54.160.105")
        object.__setattr__(self, "afg", "164.54.160.117")
        object.__setattr__(self, "hutch", "13BMD")
        object.__setattr__(self, "cycle", "2022-2")
        object.__setattr__(self, "institution", "GSECARS")
        object.__setattr__(self, "run_number", "D2711")
        object.__setattr__(self, "vpp", 2.0)

    @property
    def mso(self) -> str:
        return self._mso

    @property
    def afg(self) -> str:
        return self._afg

    @property
    def hutch(self) -> str:
        return self._hutch

    @property
    def cycle(self) -> str:
        return self._cycle

    @property
    def institution(self) -> str:
        return self._institution

    @property
    def vpp(self) -> float:
        return self._vpp

    @property
    def run_number(self) -> str:
        return self._run_number

    @mso.setter
    def mso(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_mso", value)
            self.settings.setValue("mso", self._mso)

    @afg.setter
    def afg(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_afg", value)
            self.settings.setValue("afg", self._afg)

    @hutch.setter
    def hutch(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_hutch", value)
            self.settings.setValue("hutch", self._hutch)

    @cycle.setter
    def cycle(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_cycle", value)
            self.settings.setValue("cycle", self._cycle)

    @institution.setter
    def institution(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_institution", value)
            self.settings.setValue("institution", self._institution)

    @run_number.setter
    def run_number(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_run_number", value)
            self.settings.setValue("run_number", self._run_number)

    @vpp.setter
    def vpp(self, value) -> None:
        if isinstance(value, float):
            object.__setattr__(self, "_vpp", value)
            self.settings.setValue("vpp", self._vpp)
