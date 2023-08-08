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
    _target: str = field(init=False, repr=False, compare=False, default="")
    _prefix: str = field(init=False, repr=False, compare=False, default="")
    _filename: str = field(init=False, repr=False, compare=False, default="")

    def __post_init__(self) -> None:
        object.__setattr__(self, "_mso", self.settings.value("mso", type=str))
        object.__setattr__(self, "_afg", self.settings.value("afg", type=str))
        object.__setattr__(self, "_target", self.settings.value("target", type=str))
        object.__setattr__(self, "_prefix", self.settings.value("prefix", type=str))
        object.__setattr__(
            self, "_filename", self.settings.value("filename", type=str)
        )

    def set_setup_defaults(self) -> None:
        """Sets the default values for the setup section."""
        object.__setattr__(self, "mso", "164.54.160.105")
        object.__setattr__(self, "afg", "164.54.160.117")
        object.__setattr__(self, "target", "")
        object.__setattr__(self, "prefix", "")
        object.__setattr__(self, "filename", "")

    @property
    def mso(self) -> str:
        return self._mso

    @property
    def afg(self) -> str:
        return self._afg

    @property
    def target(self) -> str:
        return self._target

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def filename(self) -> str:
        return self._filename

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

    @target.setter
    def target(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_target", value)
            self.settings.setValue("target", self._target)

    @prefix.setter
    def prefix(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_prefix", value)
            self.settings.setValue("prefix", self._prefix)

    @filename.setter
    def filename(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_filename", value)
            self.settings.setValue("filename", self._filename)
