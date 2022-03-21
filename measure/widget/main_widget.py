from qtpy.QtWidgets import QWidget


class MainWidget(QWidget):

    def __init__(self) -> None:
        super(MainWidget, self).__init__()

    def display(self) -> None:
        self.showNormal()
