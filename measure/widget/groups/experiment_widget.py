import os
from qtpy.QtWidgets import (
    QGroupBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QCheckBox,
    QDoubleSpinBox,
    QAbstractSpinBox,
)
from qtpy.QtCore import Qt, QRegularExpression
from qtpy.QtGui import QRegularExpressionValidator

from measure.util import qss_path


class ExperimentWidget(QGroupBox):
    """Experiment widget groupbox to be used in the MainWidget."""

    _qss = os.path.join(qss_path, "experiment_group.qss")

    def __init__(self) -> None:
        super(ExperimentWidget, self).__init__()

        # Initialize experiment group's widgets
        self._lbl_frequencies = QLabel("Frequencies")
        self._lbl_load = QLabel("Load (tons)")
        self._lbl_temperature = QLabel("Temperature (K)")
        self.txt_frequencies = QLineEdit()
        self.spin_load = QDoubleSpinBox()
        self.spin_temperature = QDoubleSpinBox()
        self.check_repeated = QCheckBox("Repeated collection")

        # List of experiment group's widgets
        self._experiment_widgets = [
            self._lbl_frequencies,
            self._lbl_load,
            self._lbl_temperature,
            self.txt_frequencies,
            self.spin_load,
            self.spin_temperature,
            self.check_repeated,
        ]

        # Run experiment group's widget methods
        self._configure_experiment_group()
        self._configure_experiment_labels()
        self._configure_experiment_text_boxes()
        self._configure_experiment_spin_boxes()
        self._configure_experiment_check_boxes()
        self._connect_experiment_widgets()
        self._layout_experiment_widgets()

    def disable(self) -> None:
        """Disables all experiment group's widgets."""
        [widget.setEnabled(False) for widget in self._experiment_widgets]

    def enable(self) -> None:
        """Enables all experiment group's widgets."""
        [widget.setEnabled(True) for widget in self._experiment_widgets]

    def _configure_experiment_group(self) -> None:
        """Configuration of the experiment groupbox."""
        # Set group object name
        self.setObjectName("group-experiment")

        # Set the stylesheet from assets/qss/experiment_group.qss
        self.setStyleSheet(open(self._qss, "r").read())

    def _configure_experiment_labels(self) -> None:
        """Configuration of the experiment group's labels."""
        labels = [
            self._lbl_frequencies,
            self._lbl_load,
            self._lbl_temperature,
        ]
        [label.setObjectName("lbl-experiment") for label in labels]

    def _configure_experiment_text_boxes(self) -> None:
        """Configuration of the experiment group's text boxes."""
        self.txt_frequencies.setObjectName("txt-experiment")

        # Validator for frequencies.
        expression = QRegularExpression("^(((?:0|[1-9][0-9]*)\.[0-9]+)*\, )*$")
        validator = QRegularExpressionValidator(expression)
        self.txt_frequencies.setValidator(validator)

    def _configure_experiment_spin_boxes(self) -> None:
        """Configuration of the experiment group's spin boxes."""
        self.spin_load.setObjectName("spin-load")
        self.spin_load.setMinimum(0.0)
        self.spin_load.setMaximum(900.0)
        self.spin_load.setSingleStep(10.0)
        self.spin_load.setDecimals(1)
        self.spin_load.setAlignment(Qt.AlignCenter)
        self.spin_load.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.spin_temperature.setObjectName("spin-temperature")
        self.spin_temperature.setMinimum(0.0)
        self.spin_temperature.setMaximum(3000.0)
        self.spin_temperature.setSingleStep(100.0)
        self.spin_temperature.setDecimals(1)
        self.spin_temperature.setAlignment(Qt.AlignCenter)
        self.spin_temperature.setButtonSymbols(QAbstractSpinBox.NoButtons)

    def _configure_experiment_check_boxes(self) -> None:
        """Configuration of the experiment group's check boxes."""
        self.check_repeated.setTristate(False)
        self.check_repeated.setObjectName("check-repeated")

    def _connect_experiment_widgets(self) -> None:
        """Connects signals and slots for some experiment widgets."""
        self.txt_frequencies.returnPressed.connect(self._txt_frequencies_return_pressed)

    def _txt_frequencies_return_pressed(self) -> None:
        """Loses focus on return press."""
        self.txt_frequencies.clearFocus()

    def _layout_experiment_widgets(self) -> None:
        """Sets the layout for the experiment group widgets."""
        # Main experiment layout
        experiment_layout = QGridLayout()
        experiment_layout.setContentsMargins(0, 0, 0, 0)

        # layout for frequency widgets
        frequencies_layout = QHBoxLayout()
        frequencies_layout.setContentsMargins(0, 0, 0, 0)
        frequencies_layout.addWidget(self._lbl_frequencies)
        frequencies_layout.addWidget(self.txt_frequencies)
        experiment_layout.addLayout(frequencies_layout, 0, 0, 1, 6)

        # layout for load and temperature
        load_temperature_layout = QHBoxLayout()
        load_temperature_layout.setContentsMargins(0, 0, 0, 0)
        load_temperature_layout.addWidget(self.check_repeated)
        load_temperature_layout.addStretch(1)
        load_temperature_layout.addWidget(self._lbl_load)
        load_temperature_layout.addWidget(self.spin_load)
        load_temperature_layout.addWidget(self._lbl_temperature)
        load_temperature_layout.addWidget(self.spin_temperature)
        experiment_layout.addLayout(load_temperature_layout, 1, 0, 1, 6)

        self.setLayout(experiment_layout)
