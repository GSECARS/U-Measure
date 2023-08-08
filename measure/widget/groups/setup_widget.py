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

from pathlib import Path
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
from qtpy.QtCore import Qt, QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

from measure.model import PathModel


class SetupWidget(QGroupBox):
    """Setup widget groupbox to be used in the MainWidget."""

    def __init__(self, model: PathModel) -> None:
        super(SetupWidget, self).__init__()

        self._qss = Path(model.qss_path, "setup_group.qss").as_posix()

        # Initialize setup group's widgets
        self._lbl_mso = QLabel("MSO")
        self._lbl_afg = QLabel("AFG")
        self._lbl_target = QLabel("Path")
        self._lbl_prefix = QLabel("Prefix")
        self._lbl_filename = QLabel("Filename")
        self.lbl_path = QLabel()
        self.txt_mso = QLineEdit()
        self.txt_afg = QLineEdit()
        self.txt_target = QLineEdit()
        self.txt_prefix = QLineEdit()
        self.txt_filename = QLineEdit()
        self.btn_reset = QPushButton("Reset")

        # List of setup group's widgets
        self._setup_widgets = [
            self._lbl_mso,
            self._lbl_afg,
            self._lbl_target,
            self._lbl_prefix,
            self._lbl_filename,
            self.txt_mso,
            self.txt_afg,
            self.txt_target,
            self.txt_prefix,
            self.txt_filename,
            self.btn_reset,
        ]

        # Run setup group's widget methods
        self._configure_setup_group()
        self._configure_setup_labels()
        self._configure_setup_text_boxes()
        self._configure_setup_buttons()
        self._connect_setup_widgets()
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
        self.setStyleSheet(open(self._qss, "r").read())

    def _configure_setup_labels(self) -> None:
        """Configuration of the setup group's labels."""
        labels = [
            self._lbl_mso,
            self._lbl_afg,
            self._lbl_target,
            self._lbl_prefix,
            self._lbl_filename,
            self.lbl_path,
        ]
        [label.setObjectName("lbl-setup") for label in labels]
        self.lbl_path.setObjectName("lbl-path")

    def _configure_setup_text_boxes(self) -> None:
        """Configuration of the setup group's text boxes."""
        txt_boxes = [
            self.txt_mso,
            self.txt_afg,
            self.txt_target,
            self.txt_prefix,
            self.txt_filename,
        ]
        [txt_box.setObjectName("txt-setup") for txt_box in txt_boxes]

        # IP validator
        expression = QRegularExpression("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        validator = QRegularExpressionValidator(expression, self)
        self.txt_mso.setValidator(validator)
        self.txt_afg.setValidator(validator)

        # Alignment
        self.txt_mso.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.txt_afg.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.txt_target.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.txt_prefix.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.txt_filename.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def _configure_setup_buttons(self) -> None:
        """Configuration of the setup group's buttons."""
        self.btn_reset.setObjectName("btn-reset")
        self.btn_reset.setFlat(True)
        self.btn_reset.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def _connect_setup_widgets(self) -> None:
        """Connects signals and slots for some setup widgets."""
        self.txt_mso.returnPressed.connect(
            lambda: self._txt_return_pressed(self.txt_mso)
        )
        self.txt_afg.returnPressed.connect(
            lambda: self._txt_return_pressed(self.txt_afg)
        )
        self.txt_target.returnPressed.connect(
            lambda: self._txt_return_pressed(self.txt_target)
        )
        self.txt_prefix.returnPressed.connect(
            lambda: self._txt_return_pressed(self.txt_prefix)
        )
        self.txt_filename.returnPressed.connect(
            lambda: self._txt_return_pressed(self.txt_filename)
        )

    @staticmethod
    def _txt_return_pressed(txt_widget: QLineEdit) -> None:
        """Clears focus for selected widgets."""
        txt_widget.clearFocus()

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
        run_vpp_layout.addWidget(self._lbl_target)
        run_vpp_layout.addWidget(self.txt_target)
        run_vpp_layout.addWidget(self._lbl_prefix)
        run_vpp_layout.addWidget(self.txt_prefix)
        run_vpp_layout.addWidget(self._lbl_filename)
        run_vpp_layout.addWidget(self.txt_filename)
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
