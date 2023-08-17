#!usr/bin/python
##############################################################################################
# File Name: main_widget.py
# Description: This file contains the main application widget.
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
from typing import Optional
from qtpy.QtWidgets import QWidget, QMessageBox, QHBoxLayout
from qtpy.QtGui import QCloseEvent, QIcon
from qtpy.QtCore import QSettings, QSize, QPoint

from umeasure.model import PathModel
from umeasure.widget.groups import MainGroupWidget


class MainWidget(QWidget):
    """This is used as the main application window."""

    _title: str = "U-Measure"

    def __init__(self, paths: PathModel, settings: QSettings) -> None:
        super(MainWidget, self).__init__()

        # Paths
        self._paths = paths

        self._settings = settings
        self.group_widget = MainGroupWidget(paths=self._paths)

        # Event helpers
        self._terminated: bool = False

        # Run main application methods
        self._configure_main_widget()
        self._layout_main_widget()

    def _configure_main_widget(self) -> None:
        """Configures the main application widget."""
        # Set application object name
        self.setObjectName("main-widget")

        # Sets the application icon
        self.setWindowIcon(QIcon(os.path.join(self._paths.icon_path, "ultrasonic_icon.ico")))

        # Sets the stylesheet from /assets/qss/main_widget.qss
        self.setStyleSheet(open(os.path.join(self._paths.qss_path, "main_widget.qss"), "r").read())

    def _layout_main_widget(self) -> None:
        """Sets the layout for the main application widgets."""
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.group_widget)
        self.setLayout(layout)

    def display(
        self,
        version: str,
        window_size: Optional[QSize] = None,
        window_position: Optional[QPoint] = None,
    ) -> None:
        """Displays, resizes and moves the main application window."""
        # Show the main application window
        self.showNormal()

        # Set the Window Title
        self.setWindowTitle(f"{self._title} v{version}")

        # Resize the main application window
        if window_size is not None:
            self.resize(window_size)

        # Move the main application on the screen
        if window_position is not None:
            self.move(window_position)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Creates a message box for exit confirmation if closeEvent is triggered."""
        _msg_question = QMessageBox.question(
            self, "Exit confirmation", "Are you sure you want to close the application?"
        )

        if _msg_question == QMessageBox.Yes:
            self._terminated = True

            # Save window size and position.
            self._settings.setValue("window_size", self.size())
            self._settings.setValue("window_position", self.pos())

            event.accept()
        else:
            event.ignore()

    @property
    def terminated(self):
        return self._terminated
