#!usr/bin/python
##############################################################################################
# File Name: logs_model.py
# Description: This file contains the logs model, that is used to create and store the
#              application logs.
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
from gselogger import LoggerModel


@dataclass
class LogsModel:
    """Collection of available log models."""

    _app_name: str = field(init=False, repr=False, compare=False)
    _operation_log: LoggerModel = field(init=False, repr=False, compare=False)
    _error_log: LoggerModel = field(init=False, repr=False, compare=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_app_name", "U-Measure")
        # Operational logs object
        object.__setattr__(
            self,
            "_operation_log",
            LoggerModel(app_name=self._app_name, filename="operation"),
        )
        # Error logs object
        object.__setattr__(
            self, "_error_log", LoggerModel(app_name=self._app_name, filename="error")
        )

    @property
    def operation_log(self) -> LoggerModel:
        return self._operation_log

    @property
    def error_log(self) -> LoggerModel:
        return self._error_log
