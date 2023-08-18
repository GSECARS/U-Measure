#!usr/bin/python
##############################################################################################
# File Name: control_status_widget.py
# Description: This file contains the control and status widget groupbox.
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
    QVBoxLayout,
    QSizePolicy,
    QLabel,
    QPushButton,
    QPlainTextEdit,
)
from qtpy.QtCore import Qt

from umeasure.model import PathModel
from umeasure.widget.custom import QLine


class ControlStatusWidget(QGroupBox):
    """Control and status widget groupbox to be used in the MainWidget."""

    def __init__(self, paths: PathModel) -> None:
        super(ControlStatusWidget, self).__init__()

        self._paths = paths

        # Initialize control group's widgets
        self._lbl_elapsed = QLabel("Elapsed time")
        self._lbl_feedback = QLabel("Feedback")
        self.lbl_repetition_status = QLabel()
        self.lbl_time = QLabel("0:00:00")
        self.lbl_status = QLabel("Idle")
        self.btn_collection = QPushButton("Collect")
        self.txt_feedback = QPlainTextEdit()
        self.line_horizontal = QLine(vertical=False)

        # Run control group's widget methods
        self._configure_control_status_group()
        self._configure_control_status_labels()
        self._configure_control_status_buttons()
        self._configure_control_status_text_boxes()
        self._layout_control_status_widgets()

    def _configure_control_status_group(self) -> None:
        """Configuration of the control status groupbox."""
        # Set group object name
        self.setObjectName("group-control-status")

        # Set the stylesheet from assets/qss/control_status_group.qss
        self.setStyleSheet(open(os.path.join(self._paths.qss_path, "control_status_group.qss"), "r").read())

    def _configure_control_status_labels(self) -> None:
        """Configuration of the control group's labels."""
        labels = [
            self._lbl_elapsed,
            self._lbl_feedback,
            self.lbl_time,
        ]
        [label.setObjectName("lbl-control-status") for label in labels]
        self.lbl_time.setObjectName("lbl-time")
        self.lbl_repetition_status.setObjectName("lbl-status")
        self.lbl_status.setObjectName("lbl-status")

        self.lbl_repetition_status.setVisible(False)

    def _configure_control_status_buttons(self) -> None:
        """Configuration of the control group's buttons."""
        self.btn_collection.setObjectName("btn-collection")
        self.btn_collection.setFlat(True)
        self.btn_collection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btn_collection.setMinimumWidth(150)

    def _configure_control_status_text_boxes(self) -> None:
        """Configuration of the control group's text boxes."""
        self.txt_feedback.setObjectName("txt-feedback")
        self.txt_feedback.setReadOnly(True)
        self.txt_feedback.setMinimumHeight(100)
        self.txt_feedback.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def _layout_control_status_widgets(self) -> None:
        """Sets the layout for the control status group widgets."""
        # Main control status layout
        control_status_layout = QGridLayout()
        control_status_layout.setContentsMargins(0, 0, 0, 0)
        control_status_layout.setColumnStretch(0, 1)

        # layout for the feedback section
        feedback_layout = QVBoxLayout()
        feedback_layout.addWidget(self._lbl_feedback)
        feedback_layout.addWidget(self.line_horizontal)
        feedback_layout.addWidget(self.txt_feedback)
        control_status_layout.addLayout(feedback_layout, 0, 0, 1, 1)

        # layout for elapsed time
        elapsed_layout = QVBoxLayout()
        elapsed_layout.setContentsMargins(0, 0, 0, 0)
        elapsed_layout.addWidget(self._lbl_elapsed, alignment=Qt.AlignCenter)
        elapsed_layout.addWidget(self.lbl_time, alignment=Qt.AlignCenter)

        # layout for status and collection
        collection_layout = QVBoxLayout()
        collection_layout.setContentsMargins(0, 0, 0, 0)
        collection_layout.addWidget(self.lbl_status, alignment=Qt.AlignCenter)
        collection_layout.addWidget(
            self.lbl_repetition_status, alignment=Qt.AlignCenter
        )
        collection_layout.addWidget(self.btn_collection)

        # layout for the complete control part
        control_layout = QVBoxLayout()
        control_layout.addStretch(1)
        control_layout.addLayout(elapsed_layout)
        control_layout.addLayout(collection_layout)
        control_status_layout.addLayout(control_layout, 0, 1, 1, 1)

        self.setLayout(control_status_layout)
