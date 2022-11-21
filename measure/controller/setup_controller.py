from qtpy.QtCore import QSettings, Signal, QObject

from measure.model import SetupModel
from measure.widget.groups import SetupWidget


class SetupController(QObject):
    """Provides a way to control and connect the setup widget with the setup model."""

    base_dir_changed: Signal = Signal(str)
    basedir: str = None

    def __init__(self, widget: SetupWidget, settings: QSettings) -> None:
        super(SetupController, self).__init__()
        self.model = SetupModel(settings=settings)
        self._widget = widget

        self._update_setup_values()
        self._update_basedir()
        self._connect_setup_widgets()

    def _connect_setup_widgets(self) -> None:
        """Connects setup widgets signals and slots."""
        self._widget.txt_mso.textChanged.connect(self._txt_mso_text_changed)
        self._widget.txt_afg.textChanged.connect(self._txt_afg_text_changed)
        self._widget.txt_hutch.textChanged.connect(self._txt_hutch_text_changed)
        self._widget.txt_cycle.textChanged.connect(self._txt_cycle_text_changed)
        self._widget.txt_institution.textChanged.connect(
            self._txt_institution_text_changed
        )
        self._widget.txt_run_number.textChanged.connect(
            self._txt_run_number_text_changed
        )
        self._widget.spin_vpp.valueChanged.connect(self._spin_vpp_value_changed)
        self._widget.btn_reset.clicked.connect(self._btn_reset_clicked)

    def _update_setup_values(self) -> None:
        """Update the setup GUI values."""
        self._widget.txt_mso.setText(self.model.mso)
        self._widget.txt_afg.setText(self.model.afg)
        self._widget.txt_hutch.setText(self.model.hutch)
        self._widget.txt_cycle.setText(self.model.cycle)
        self._widget.txt_institution.setText(self.model.institution)
        self._widget.txt_run_number.setText(self.model.run_number)
        self._widget.spin_vpp.setValue(self.model.vpp)

    def _update_basedir(self) -> None:
        """Updates the current base directory and updates the GUI path label."""

        hutch = ""
        if not self.model.hutch.strip() == "":
            hutch = self.model.hutch + "/"

        cycle = ""
        if not self.model.cycle.strip() == "":
            cycle = self.model.cycle + "/"

        institution = ""
        if not self.model.institution.strip() == "":
            institution = self.model.institution + "/"

        run_number = ""
        if not self.model.run_number.strip() == "":
            run_number = self.model.run_number + "/"

        self.basedir = f"C:/Data/{hutch}{cycle}{institution}{run_number}"
        self.base_dir_changed.emit(self.basedir)
        self._widget.lbl_path.setText(self.basedir)

    def _txt_mso_text_changed(self) -> None:
        """Updates the current mso IP based on user input."""
        self.model.mso = self._widget.txt_mso.text()

    def _txt_afg_text_changed(self) -> None:
        """Updates the current afg IP based on user input."""
        self.model.afg = self._widget.txt_afg.text()

    def _txt_hutch_text_changed(self) -> None:
        """Updates the current hutch value based on user input."""
        self.model.hutch = self._widget.txt_hutch.text()
        self._update_basedir()

    def _txt_cycle_text_changed(self) -> None:
        """Updates the current cycle value based on user input."""
        self.model.cycle = self._widget.txt_cycle.text()
        self._update_basedir()

    def _txt_institution_text_changed(self) -> None:
        """Updates the current institution value based on user input."""
        self.model.institution = self._widget.txt_institution.text()
        self._update_basedir()

    def _txt_run_number_text_changed(self) -> None:
        """Updates the current run number based on user input."""
        self.model.run_number = self._widget.txt_run_number.text()
        self._update_basedir()

    def _spin_vpp_value_changed(self) -> None:
        """Updates the current vpp value based on user input."""
        self.model.vpp = self._widget.spin_vpp.value()

    def _btn_reset_clicked(self) -> None:
        """Restores default values and updates the GUI."""
        self.model.set_setup_defaults()
        self._update_setup_values()
