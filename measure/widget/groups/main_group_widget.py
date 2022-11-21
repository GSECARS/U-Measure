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

from qtpy.QtWidgets import QWidget, QGridLayout

from measure.model import PathModel
from measure.widget.groups import SetupWidget, ExperimentWidget, ControlStatusWidget


class MainGroupWidget(QWidget):
    """Custom widget to hold all the groupboxes."""

    def __init__(self, model: PathModel) -> None:
        super(MainGroupWidget, self).__init__()

        self.setup = SetupWidget(model=model)
        self.experiment = ExperimentWidget(model=model)
        self.control_status = ControlStatusWidget(model=model)

        self._layout_widgets()

    def _layout_widgets(self) -> None:
        """Sets the layout for the main group widgets."""
        main_layout = QGridLayout()
        main_layout.setRowStretch(2, 1)
        main_layout.addWidget(self.setup, 0, 0, 1, 1)
        main_layout.addWidget(self.experiment, 1, 0, 1, 1)
        main_layout.addWidget(self.control_status, 2, 0, 1, 1)

        self.setLayout(main_layout)
