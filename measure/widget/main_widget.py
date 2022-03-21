from typing import Optional
from qtpy.QtWidgets import QWidget, QMessageBox
from qtpy.QtGui import QCloseEvent
from qtpy.QtCore import QSettings, QSize, QPoint


class MainWidget(QWidget):

    def __init__(self, settings: QSettings) -> None:
        super(MainWidget, self).__init__()

        self._settings = settings

    def display(self, window_size: Optional[QSize] = None, window_position: Optional[QPoint] = None) -> None:
        self.showNormal()

        if window_size is not None:
            self.resize(window_size)

        if window_position is not None:
            self.move(window_position)

    def closeEvent(self, event: QCloseEvent) -> None:
        _msg_question = QMessageBox.question(
            self,
            "Exit confirmation",
            "Are you sure you want to close the application?"
        )

        if _msg_question == QMessageBox.Yes:

            # Save window size and position.
            self._settings.setValue("window_size", self.size())
            self._settings.setValue("window_position", self.pos())

            event.accept()
        else:
            event.ignore()
