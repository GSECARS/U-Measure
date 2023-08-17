#!usr/bin/python
##############################################################################################
# File Name: q_line.py
# Description: This file contains the custom vertical/horizontal line widget.
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

from qtpy.QtWidgets import QFrame
from typing import Optional


class QLine(QFrame):
    """Custom vertical/horizontal line widget to expand to the available space."""

    def __init__(self, vertical: Optional[bool] = True) -> None:
        super(QLine, self).__init__()

        self._vertical = vertical
        self._set_orientation()

    def _set_orientation(self) -> None:
        """Sets the orientation of the line to vertical or horizontal."""
        if self._vertical:
            self.setFrameShape(QFrame.Shape.VLine)
        else:
            self.setFrameShape(QFrame.Shape.HLine)
