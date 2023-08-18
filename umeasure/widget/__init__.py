#!usr/bin/python
##############################################################################################
# File Name: __init__.py
# Description: This file is used for the umeasure widget package.
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

from umeasure.widget.setup_widget import SetupWidget
from umeasure.widget.experiment_widget import ExperimentWidget
from umeasure.widget.control_status_widget import ControlStatusWidget
from umeasure.widget.main_widget import MainWidget

__all__ = [
    "SetupWidget",
    "ExperimentWidget",
    "ControlStatusWidget",
    "MainWidget"
]
