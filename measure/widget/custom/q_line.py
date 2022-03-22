from qtpy.QtWidgets import QFrame
from typing import Optional


class QLine(QFrame):
    def __init__(self, vertical: Optional[bool] = True) -> None:
        super(QLine, self).__init__()

        self._vertical = vertical

        self._set_orientation()

    def _set_orientation(self) -> None:
        if self._vertical:
            self.setFrameShape(QFrame.Shape.VLine)
        else:
            self.setFrameShape(QFrame.Shape.HLine)
