import sys
from qtpy.QtWidgets import QApplication

from measure.widget import MainWidget


class MainController:

    def __init__(self) -> None:
        self._app = QApplication(sys.argv)
        self._widget = MainWidget()

    def run(self) -> None:
        self._widget.display()
        sys.exit(self._app.exec())
