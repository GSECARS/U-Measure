import sys
from qtpy.QtWidgets import QApplication
from qtpy.QtCore import QSettings

from measure.widget import MainWidget
from measure.controller import SetupController, ExperimentController


class MainController:
    """Used to connect all controllers, models and widgets."""

    def __init__(self) -> None:
        self._app = QApplication(sys.argv)
        self._settings = QSettings("GSECARS", "U-Measure")
        self._widget = MainWidget(settings=self._settings)

        # Setup controller
        self._setup_controller = SetupController(
            widget=self._widget.group_widget.setup,
            settings=self._settings
        )

        # Experiment controller
        self._experiment_controller = ExperimentController(
            widget=self._widget.group_widget.experiment,
            settings=self._settings
        )

        # Set initial focus
        self._widget.group_widget.setup.lbl_path.setFocus()

    def run(self) -> None:
        """Starts the application."""
        self._widget.display(
            window_size=self._settings.value("window_size"),
            window_position=self._settings.value("window_position")
        )
        sys.exit(self._app.exec())
