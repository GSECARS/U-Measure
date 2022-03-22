from qtpy.QtWidgets import QWidget, QGridLayout

from measure.widget.groups import SetupWidget, ExperimentWidget, ControlStatusWidget


class MainGroupWidget(QWidget):
    """Custom widget to hold all the groupboxes."""

    def __init__(self) -> None:
        super(MainGroupWidget, self).__init__()

        self.setup = SetupWidget()
        self.experiment = ExperimentWidget()
        self.control_status = ControlStatusWidget()

        self._layout_widgets()

    def _layout_widgets(self) -> None:
        """Sets the layout for the main group widgets."""
        main_layout = QGridLayout()
        main_layout.setRowStretch(2, 1)
        main_layout.addWidget(self.setup, 0, 0, 1, 1)
        main_layout.addWidget(self.experiment, 1, 0, 1, 1)
        main_layout.addWidget(self.control_status, 2, 0, 1, 1)

        self.setLayout(main_layout)
