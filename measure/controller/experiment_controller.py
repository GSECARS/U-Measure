from qtpy.QtCore import QSettings

from measure.model import ExperimentModel
from measure.widget.groups import ExperimentWidget


class ExperimentController:
    """Provides a way to control and connect the experiment widget with the experiment model."""

    def __init__(self, widget: ExperimentWidget, settings: QSettings) -> None:
        self.model = ExperimentModel(settings=settings)
        self._widget = widget

        self._update_experiment_values()
        self._connect_experiment_widgets()

    def _connect_experiment_widgets(self) -> None:
        """Connects experiment signals and slots."""
        self._widget.txt_frequencies.textChanged.connect(
            self._txt_frequencies_text_changed
        )
        self._widget.txt_threshold.textChanged.connect(self._txt_threshold_text_changed)
        self._widget.txt_scan.textChanged.connect(self._txt_scan_text_changed)
        self._widget.check_repeated.stateChanged.connect(self._check_repeated_changed)
        self._widget.spin_load.valueChanged.connect(self._spin_load_value_changed)
        self._widget.spin_temperature.valueChanged.connect(
            self._spin_temperature_value_changed
        )

    def _update_experiment_values(self) -> None:
        """Update the experiment GUI values."""
        self._widget.check_repeated.setChecked(self.model.repeat)
        self._widget.spin_load.setValue(self.model.load)
        self._widget.spin_temperature.setValue(self.model.temperature)
        self._widget.txt_threshold.setText(str(self.model.threshold))
        self._widget.txt_scan.setText(self.model.scan)

        # Update frequencies text
        frequencies_str = ""
        if self.model.frequencies:
            for index, frequency in enumerate(self.model.frequencies):

                frequencies_str += str(frequency)
                if not index == len(self.model.frequencies) - 1:
                    frequencies_str += ", "

            self._widget.txt_frequencies.setText(frequencies_str)

    def _txt_frequencies_text_changed(self) -> None:
        """Converts the user input to list[float]."""
        frequencies_list: list[float] = []
        frequencies_str_list = self._widget.txt_frequencies.text().strip().split(",")

        # Covert to float
        for frequency in frequencies_str_list:
            frequency = frequency.strip()
            if frequency != "":
                frequencies_list.append(float(frequency))

        # Update current array
        self.model.frequencies = frequencies_list

    def _txt_threshold_text_changed(self) -> None:
        """Updates the current threshold value based on user input."""
        self.model.threshold = float(self._widget.txt_threshold.text())

    def _check_repeated_changed(self, state) -> None:
        """Updates the current repeat value based on user input."""
        if state == 0:
            self.model.repeat = False
        else:
            self.model.repeat = True

    def _txt_scan_text_changed(self) -> None:
        """Updates the current scan value based on user input."""
        self.model.scan = self._widget.txt_scan.text()

    def _spin_load_value_changed(self) -> None:
        """Updates the current load value based on user input."""
        self.model.load = self._widget.spin_load.value()

    def _spin_temperature_value_changed(self) -> None:
        """Updates the current temperature value based on user input."""
        self.model.temperature = self._widget.spin_temperature.value()
