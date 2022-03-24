from qtpy.QtWidgets import QMessageBox


class MsgBox(QMessageBox):
    """Custom popup message box widget to expand to the available space."""

    def __init__(self, msg: str):
        super(MsgBox, self).__init__()
        self.critical(self, "Error", msg, QMessageBox.Ok)
