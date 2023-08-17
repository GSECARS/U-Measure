#!usr/bin/python
##############################################################################################
# File Name: gui_worker.py
# Description: This file contains the worker class that's been used for threading.
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

from qtpy.QtCore import QThread
from typing import Any, Callable


class GUIWorker(QThread):
    """
    The worker class that's been used for threading.
    """

    def __init__(self, method: Callable, args: Any) -> None:
        super(GUIWorker, self).__init__()

        self._method = method
        self._args = args

    def run(self) -> None:
        self._method(*self._args)
