#!usr/bin/python
##############################################################################################
# File Name: setup_widget.py
# Description: This file contains the setup widget groupbox.
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

import os
from qtpy.QtWidgets import (
    QGroupBox,
    QGridLayout,
    QHBoxLayout,
    QSizePolicy,
    QLabel,
    QLineEdit,
    QPushButton,
    QDoubleSpinBox,
    QAbstractSpinBox,
)
from qtpy.QtCore import Qt
from gsewidgets import (
    Label,
    IPv4InputBox,
    FileNameInputBox,
    NoWheelNumericSpinBox,
    FlatButton,
)

from umeasure.model import PathModel


class SetupWidget(QGroupBox):
    """Setup widget groupbox to be used in the MainWidget."""

    def __init__(self, paths: PathModel) -> None:
        super(SetupWidget, self).__init__()

        self._paths = paths

        # Initialize setup group's widgets
        self._lbl_mso = Label("MSO", object_name="lbl-setup")
        self._lbl_afg = Label("AFG", object_name="lbl-setup")
        self._lbl_cycle = Label("Cycle", object_name="lbl-setup")
        self._lbl_run_number = Label("#Run", object_name="lbl-setup")
        self._lbl_vpp = Label("Vpp", object_name="lbl-setup")
        self.lbl_path = Label(object_name="lbl-path")
        self.txt_mso = IPv4InputBox(object_name="txt-setup")
        self.txt_afg = IPv4InputBox(object_name="txt-setup")
        self.txt_cycle = FileNameInputBox(object_name="txt-setup")
        self.txt_run_number = FileNameInputBox(object_name="txt-setup")
        self.spin_vpp = NoWheelNumericSpinBox(
            min_value=0.0,
            max_value=5.0,
            default_value=2.0,
            incremental_step=0.1,
            precision=1,
            object_name="spin-vpp",
        )
        self.btn_reset = FlatButton("Reset", object_name="btn-reset")

        # List of setup group's widgets
        self._setup_widgets = [
            self._lbl_mso,
            self._lbl_afg,
            self._lbl_cycle,
            self._lbl_run_number,
            self._lbl_vpp,
            self.txt_mso,
            self.txt_afg,
            self.txt_cycle,
            self.txt_run_number,
            self.spin_vpp,
            self.btn_reset,
        ]

        # Run setup group's widget methods
        self._configure_setup_group()
        self._layout_setup_widgets()

    def disable(self) -> None:
        """Disables all setup group's widgets."""
        [widget.setEnabled(False) for widget in self._setup_widgets]

    def enable(self) -> None:
        """Enables all setup group's widgets."""
        [widget.setEnabled(True) for widget in self._setup_widgets]

    def _configure_setup_group(self) -> None:
        """Configuration of the setup groupbox."""
        # Set group object name
        self.setObjectName("group-setup")

        # Set the stylesheet from assets/qss/setup_group.qss
        self.setStyleSheet(
            open(os.path.join(self._paths.qss_path, "setup_group.qss"), "r").read()
        )

    def _layout_setup_widgets(self) -> None:
        """Sets the layout for the setup group widgets."""
        # Main setup layout widget
        setup_layout = QGridLayout()
        setup_layout.setContentsMargins(0, 0, 0, 0)

        # layout for mso widgets
        mso_layout = QHBoxLayout()
        mso_layout.setContentsMargins(0, 0, 0, 0)
        mso_layout.setSpacing(7)
        mso_layout.addWidget(self._lbl_mso)
        mso_layout.addWidget(self.txt_mso)
        setup_layout.addLayout(mso_layout, 0, 0, 1, 6)

        # layout for afg widgets
        afg_layout = QHBoxLayout()
        afg_layout.setContentsMargins(0, 0, 0, 0)
        afg_layout.setSpacing(13)
        afg_layout.addWidget(self._lbl_afg)
        afg_layout.addWidget(self.txt_afg)
        setup_layout.addLayout(afg_layout, 1, 0, 1, 6)

        # layout for cycle, #run and vpp widgets
        run_vpp_layout = QHBoxLayout()
        run_vpp_layout.setContentsMargins(0, 0, 0, 0)
        run_vpp_layout.addWidget(self._lbl_cycle)
        run_vpp_layout.addWidget(self.txt_cycle)
        run_vpp_layout.addWidget(self._lbl_run_number)
        run_vpp_layout.addWidget(self.txt_run_number)
        run_vpp_layout.addWidget(self._lbl_vpp)
        run_vpp_layout.addWidget(self.spin_vpp)
        run_vpp_layout.addStretch(1)
        setup_layout.addLayout(run_vpp_layout, 2, 0, 1, 4)

        # layout for path widgets
        path_layout = QHBoxLayout()
        path_layout.setContentsMargins(0, 0, 0, 0)
        path_layout.addWidget(self.lbl_path)
        path_layout.addStretch(1)
        setup_layout.addLayout(path_layout, 3, 0, 1, 4)

        # layout for reset widgets
        reset_layout = QHBoxLayout()
        reset_layout.setContentsMargins(0, 0, 0, 0)
        reset_layout.addStretch(1)
        reset_layout.addWidget(self.btn_reset)
        setup_layout.addLayout(reset_layout, 2, 4, 2, 2)

        self.setLayout(setup_layout)
