import os
from typing import Optional
from qtpy.QtWidgets import QWidget, QMessageBox, QHBoxLayout
from qtpy.QtGui import QCloseEvent
from qtpy.QtCore import QSettings, QSize, QPoint

from measure.widget.groups import MainGroupWidget
from measure.util import qss_path


class MainWidget(QWidget):
    """This is used as the main application window."""

    _qss: str = os.path.join(qss_path, "main_widget.qss")
    _title: str = "U-Measure"

    def __init__(self, settings: QSettings) -> None:
        super(MainWidget, self).__init__()

        self._settings = settings
        self.group_widget = MainGroupWidget()

        # Run main application methods
        self._configure_main_widget()
        self._layout_main_widget()

    def _configure_main_widget(self) -> None:
        """Configures the main application widget."""
        # Set application object name
        self.setObjectName("main-widget")

        # Sets the application title
        self.setWindowTitle(self._title)

        # Sets the stylesheet from /assets/qss/main_widget.qss
        self.setStyleSheet(open(self._qss, "r").read())

    def _layout_main_widget(self) -> None:
        """Sets the layout for the main application widgets."""
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.group_widget)
        self.setLayout(layout)

    def display(
        self,
        window_size: Optional[QSize] = None,
        window_position: Optional[QPoint] = None,
    ) -> None:
        """Displays, resizes and moves the main application window."""
        # Show the main application window
        self.showNormal()

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

            # Save window size and position.
            self._settings.setValue("window_size", self.size())
            self._settings.setValue("window_position", self.pos())

            event.accept()
        else:
            event.ignore()
