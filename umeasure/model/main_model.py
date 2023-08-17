#!/usr/bin/python
##############################################################################################
# File Name: main_model.py
# Description: This is the main model file of the U-Measure project. It is used to create the
#              collection of all the necessary models needed to run the U-Measure application. 
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

from umeasure.model import PathModel


@dataclass
class MainModel:
    """This is used as the main application model."""
    
    _paths: PathModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        """This is used after the initialization of the main application model."""
        object.__setattr__(self, "_paths", PathModel())
    
    @property
    def paths(self) -> PathModel:
        """Returns the paths model."""
        return self._paths