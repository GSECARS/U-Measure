from dataclasses import dataclass, field
from qtpy.QtCore import QSettings


@dataclass(frozen=False)
class ExperimentModel:
    """Dataclass that holds all necessary data information for the experiment section."""

    settings: QSettings = field(init=True, repr=False, compare=False)

    _frequencies: list[float] = field(
        init=False, repr=False, compare=False, default_factory=lambda: []
    )
    _threshold: float = field(init=False, repr=False, compare=False, default=27.0)
    _repeat: bool = field(init=False, repr=False, compare=False, default=False)
    _scan: str = field(init=False, repr=False, compare=False, default="A")
    _load: float = field(init=False, repr=False, compare=False, default=0.0)
    _temperature: float = field(init=False, repr=False, compare=False, default=0.0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_scan", self.settings.value("scan", type=str))

        # Set frequencies value
        object.__setattr__(self, "_frequencies", self._convert_array())

        # Set threshold value
        threshold_value = self.settings.value("threshold", type=float)
        if threshold_value is None:
            threshold_value = 0.0
        object.__setattr__(self, "_threshold", threshold_value)

        # Set repeat value
        repeat_value = self.settings.value("repeat", type=bool)
        if repeat_value is None:
            repeat_value = False
        object.__setattr__(self, "_repeat", repeat_value)

        # Set load value
        load_value = self.settings.value("load", type=float)
        if load_value is None:
            load_value = 0.0
        object.__setattr__(self, "_load", load_value)

        # Set temperature value
        temperature_value = self.settings.value("temperature", type=float)
        if temperature_value is None:
            temperature_value = 0.0
        object.__setattr__(self, "_temperature", temperature_value)

    def set_experiment_defaults(self) -> None:
        """Sets the default values for the experiment section."""
        object.__setattr__(self, "_frequencies", [20.0, 30.0, 40.0, 50.0, 60.0])
        object.__setattr__(self, "_threshold", 27)
        object.__setattr__(self, "_repeat", False)
        object.__setattr__(self, "_scan", "A")
        object.__setattr__(self, "_load", 1)
        object.__setattr__(self, "_temperature", 1)

    def _convert_array(self) -> list[float]:
        """Converts the saved array to list[float]."""
        frequencies_list: list[float] = []
        saved_list = self.settings.value("frequencies")
        if saved_list is not None:
            frequencies_list = [float(frequency) for frequency in saved_list]

        return frequencies_list

    @property
    def frequencies(self) -> list[float]:
        return self._frequencies

    @property
    def threshold(self) -> float:
        return self._threshold

    @property
    def repeat(self) -> bool:
        return self._repeat

    @property
    def scan(self) -> str:
        return self._scan

    @property
    def load(self) -> float:
        return self._load

    @property
    def temperature(self) -> float:
        return self._temperature

    @frequencies.setter
    def frequencies(self, value) -> None:
        if isinstance(value, list):
            object.__setattr__(self, "_frequencies", value)
            self.settings.setValue("frequencies", self._frequencies)

    @threshold.setter
    def threshold(self, value) -> None:
        if isinstance(value, float):
            object.__setattr__(self, "_threshold", value)
            self.settings.setValue("threshold", self._threshold)

    @repeat.setter
    def repeat(self, value) -> None:
        if isinstance(value, bool):
            object.__setattr__(self, "_repeat", value)
            self.settings.setValue("repeat", self._repeat)

    @scan.setter
    def scan(self, value) -> None:
        if isinstance(value, str):
            object.__setattr__(self, "_scan", value)
            self.settings.setValue("scan", self._scan)

    @load.setter
    def load(self, value) -> None:
        if isinstance(value, float):
            object.__setattr__(self, "_load", value)
            self.settings.setValue("load", self._load)

    @temperature.setter
    def temperature(self, value) -> None:
        if isinstance(value, float):
            object.__setattr__(self, "_temperature", value)
            self.settings.setValue("temperature", self._temperature)
