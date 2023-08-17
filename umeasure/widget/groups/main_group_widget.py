#!usr/bin/python
##############################################################################################
# File Name: main_group_widget.py
# Description: This file contains the main group widget.
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

from qtpy.QtWidgets import QWidget, QGridLayout

from umeasure.widget.groups import SetupWidget, ExperimentWidget, ControlStatusWidget


class MainGroupWidget(QWidget):
    """Custom widget to hold all the groupboxes."""

    def __init__(self) -> None:
        super(MainGroupWidget, self).__init__()

        self.setup = SetupWidget()
        self.experiment = ExperimentWidget()
        self.control_status = ControlStatusWidget()

        self._layout_widgets()

    def _layout_widgets(self) -> None:
        """Sets the layout for the main group widgets."""
        main_layout = QGridLayout()
        main_layout.setRowStretch(2, 1)
        main_layout.addWidget(self.setup, 0, 0, 1, 1)
        main_layout.addWidget(self.experiment, 1, 0, 1, 1)
        main_layout.addWidget(self.control_status, 2, 0, 1, 1)

        self.setLayout(main_layout)
