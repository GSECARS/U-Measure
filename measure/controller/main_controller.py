import sys
from qtpy.QtWidgets import QApplication
from qtpy.QtCore import QSettings

from measure.widget import MainWidget


class MainController:

    def __init__(self) -> None:
        self._app = QApplication(sys.argv)
        self._settings = QSettings("GSECARS", "U-Measure")
        self._widget = MainWidget(settings=self._settings)

    def run(self) -> None:
        self._widget.display(
            window_size=self._settings.value("window_size"),
            window_position=self._settings.value("window_position")
        )
        sys.exit(self._app.exec())
