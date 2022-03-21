from qtpy.QtCore import QThread
from typing import Any, Callable


class GUIWorker(QThread):
    """
    The worker class that's been used for threading.
    """

    def __init__(self, method: Callable, args: Any) -> None:
        super(GUIWorker, self).__init__()

        self._method = method
        self._args = args

    def run(self) -> None:
        self._method(*self._args)
