#!usr/bin/python
##############################################################################################
# File Name: settings_model.py 
# Description: This file contains the settings model and the settings model collection.
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

from umeasure.model.settings import SizingSettingsModel


@dataclass
class SettingsModel:
    """All the settings models are collected here."""

    _settings: QSettings = field(init=False, repr=False, compare=False)
    _sizing: SizingSettingsModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        """Post-initialization method."""
        object.__setattr__(self, "_settings", QSettings("GSECARS", "U-Measure"))
        object.__setattr__(self, "_sizing", SizingSettingsModel(settings=self._settings))
    
    @property
    def sizing(self) -> SizingSettingsModel:
        """Returns the sizing settings model."""
        return self._sizing