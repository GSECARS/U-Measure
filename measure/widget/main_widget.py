from pathlib import Path
from typing import Optional
from qtpy.QtWidgets import QWidget, QMessageBox, QHBoxLayout
from qtpy.QtGui import QCloseEvent, QIcon
from qtpy.QtCore import QSettings, QSize, QPoint

from measure.model import PathModel
from measure.widget.groups import MainGroupWidget


class MainWidget(QWidget):
    """This is used as the main application window."""

    def __init__(self, settings: QSettings, model: PathModel) -> None:
        super(MainWidget, self).__init__()

        self._icon: str = Path(model.icon_path, "ultrasonic_icon.ico").as_posix()
        self._qss: str = Path(model.qss_path, "main_widget.qss").as_posix()

        self._settings = settings
        self.group_widget = MainGroupWidget(model=model)

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
        self.setWindowIcon(QIcon(self._icon))

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
        version: str,
        window_size: Optional[QSize] = None,
        window_position: Optional[QPoint] = None,
    ) -> None:
        """Displays, resizes and moves the main application window."""
        # Show the main application window
        self.setWindowTitle(f"U-Measure {version}")  # Set the title
        self.showNormal()  # Display

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
