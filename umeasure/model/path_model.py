#!usr/bin/python
##############################################################################################
# File Name: path_model.py
# Description: This file contains the paths for the assets.
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
from pathlib import Path, PurePosixPath


@dataclass(frozen=True)
class PathModel:
    """
    Model that holds the paths for the assets directories.
    """

    _assets_path: str = field(init=False, compare=False, repr=False)
    _icon_path: str = field(init=False, compare=False, repr=False)
    _qss_path: str = field(init=False, compare=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "_assets_path", Path("umeasure/assets").absolute().as_posix()
        )
        object.__setattr__(
            self,
            "_icon_path",
            PurePosixPath(self._assets_path).joinpath("icons").as_posix(),
        )
        object.__setattr__(
            self,
            "_qss_path",
            PurePosixPath(self._assets_path).joinpath("qss").as_posix(),
        )

    @property
    def icon_path(self) -> str:
        return self._icon_path

    @property
    def qss_path(self) -> str:
        return self._qss_path
