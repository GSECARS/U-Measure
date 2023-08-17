#!usr/bin/python
##############################################################################################
# File Name: setup_controller.py
# Description: This file contains the controller logic for the setup section.
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

from qtpy.QtCore import QSettings

from umeasure.model import SetupModel
from umeasure.widget.groups import SetupWidget


class SetupController:
    """Provides a way to control and connect the setup widget with the setup model."""

    basedir: str = None

    def __init__(self, widget: SetupWidget, settings: QSettings) -> None:
        self.model = SetupModel(settings=settings)
        self._widget = widget

        self._update_setup_values()
        self._update_basedir()
        self._connect_setup_widgets()

    def _connect_setup_widgets(self) -> None:
        """Connects setup widgets signals and slots."""
        self._widget.txt_mso.textChanged.connect(self._txt_mso_text_changed)
        self._widget.txt_afg.textChanged.connect(self._txt_afg_text_changed)
        self._widget.txt_cycle.textChanged.connect(self._txt_cycle_text_changed)
        self._widget.txt_run_number.textChanged.connect(
            self._txt_run_number_text_changed
        )
        self._widget.spin_vpp.valueChanged.connect(self._spin_vpp_value_changed)
        self._widget.btn_reset.clicked.connect(self._btn_reset_clicked)

    def _update_setup_values(self) -> None:
        """Update the setup GUI values."""
        self._widget.txt_mso.setText(self.model.mso)
        self._widget.txt_afg.setText(self.model.afg)
        self._widget.txt_cycle.setText(self.model.cycle)
        self._widget.txt_run_number.setText(self.model.run_number)
        self._widget.spin_vpp.setValue(self.model.vpp)

    def _update_basedir(self) -> None:
        """Updates the current base directory and updates the GUI path label."""
        self.basedir = (
            f"C:/Data/13BMD/{self.model.cycle}/GSECARS/{self.model.run_number}/"
        )
        self._widget.lbl_path.setText(self.basedir)

    def _txt_mso_text_changed(self) -> None:
        """Updates the current mso IP based on user input."""
        self.model.mso = self._widget.txt_mso.text()

    def _txt_afg_text_changed(self) -> None:
        """Updates the current afg IP based on user input."""
        self.model.afg = self._widget.txt_afg.text()

    def _txt_cycle_text_changed(self) -> None:
        """Updates the current cycle value based on user input."""
        self.model.cycle = self._widget.txt_cycle.text()
        self._update_basedir()

    def _txt_run_number_text_changed(self) -> None:
        """Updates the current run number based on user input."""
        self.model.run_number = self._widget.txt_run_number.text()
        self._update_basedir()

    def _spin_vpp_value_changed(self) -> None:
        """Updates the current vpp value based on user input."""
        self.model.vpp = self._widget.spin_vpp.value()

    def _btn_reset_clicked(self) -> None:
        """Restores default values and updates the GUI."""
        self.model.set_setup_defaults()
        self._update_setup_values()
