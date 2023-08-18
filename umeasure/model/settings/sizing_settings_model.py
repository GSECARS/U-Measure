#!usr/bin/python
##############################################################################################
# File Name: sizing_settings_model.py 
# Description: This file is used for the sizing settings model.
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
from qtpy.QtCore import QSettings, QSize, QPoint


@dataclass
class SizingSettingsModel:
    """U-Measure main application window sizing and position settings model."""
    
    settings: QSettings = field(repr=False, compare=False)

    _window_size: QSize = field(init=False, repr=False, compare=False, default=None)
    _window_position: QPoint = field(init=False, repr=False,compare=False, default=None)
    _window_state: int = field(init=False, repr=False, compare=False, default=2)

    def __post_init__(self) -> None:
        """Post-initialization method."""
        object.__setattr__(self, "window_size", self.settings.value("window_size", type=QSize))
        object.__setattr__(self, "window_position", self.settings.value("window_position", type=QPoint))
        object.__setattr__(self, "window_state", self.settings.value("window_state", type=int))

    @property
    def window_size(self) -> QSize | None:
        """Returns the window size."""
        return self._window_size
    
    @window_size.setter
    def window_size(self, value: QSize) -> None:
        """Sets the window size."""
        object.__setattr__(self, "_window_size", value)
        self.settings.setValue("window_size", self._window_size)

    @property
    def window_position(self) -> QPoint | None:
        """Returns the window position."""
        return self._window_position
    
    @window_position.setter
    def window_position(self, value: QPoint) -> None:
        """Sets the window position."""
        object.__setattr__(self, "_window_position", value)
        self.settings.setValue("window_position", self._window_position)

    @property
    def window_state(self) -> int:
        """Returns the window state."""
        return self._window_state
    
    @window_state.setter
    def window_state(self, value: int) -> None:
        """Sets the window state."""
        object.__setattr__(self, "_window_state", value)
        self.settings.setValue("window_state", self._window_state)
