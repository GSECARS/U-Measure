#!/usr/bin/python3
# ----------------------------------------------------------------------
# U-Measure - A GUI software for ultrasonic data collection.
# Author: Christofanis Skordas (skordasc@uchicago.edu)
# Copyright (C) 2022  GSECARS, The University of Chicago
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import time
from datetime import datetime
from pyvisa import ResourceManager, VisaIOError
from typing import Optional
from qtpy.QtCore import QObject, Signal


from measure.model import SetupModel, ExperimentModel


class VisaController(QObject):
    """Provides a way to interact with the tekVISA instruments."""

    new_feedback_message = Signal(str)
    current_repetition = Signal(int)

    def __init__(
        self,
        setup_model: SetupModel,
        experiment_model: ExperimentModel,
        basedir: str,
        base_dir_changed: Signal(str),
    ) -> None:
        super(VisaController, self).__init__()

        self._setup_model = setup_model
        self._experiment_model = experiment_model
        self._basedir = basedir

        self._base_dir_changed = base_dir_changed
        self._base_dir_changed.connect(self._update_base_dir)

        self._resource_manager = ResourceManager()
        self._mso_resource = None
        self._afg_resource = None
        self.connected = False

    def _update_base_dir(self, base_dir: str) -> None:
        self._basedir = base_dir
        print(base_dir)

    def connect(self) -> None:
        """Connects with the tek instruments."""
        try:
            self._mso_resource = self._resource_manager.open_resource(
                f"TCPIP::{self._setup_model.mso}::INSTR"
            )
            self._afg_resource = self._resource_manager.open_resource(
                f"TCPIP::{self._setup_model.afg}::INSTR"
            )
        except VisaIOError as error:
            self.connected = False
            error_message = f"VisaIOError: {error.description} ({error.error_code})."
            self.new_feedback_message.emit(error_message)
        else:
            self.connected = True
            self.new_feedback_message.emit(f"{self._mso_resource.query('*IDN?')}")
            self.new_feedback_message.emit(f"{self._afg_resource.query('*IDN?')}")

    def _acquire_signal(
        self,
        frequency: float,
        abort_status: bool,
        step: Optional[int] = 1,
    ) -> None:
        """Sends all the acquire commands to the mso instrument."""

        self._mso_resource.write(":acquire:state stop")
        self._mso_resource.write("acquire:stopafter sequence")
        self._mso_resource.write(":acquire:state run")

        while (
            self._mso_resource.query_ascii_values(":acquire:state?", converter="b")[0]
            == 1
        ):
            if abort_status:
                return None
            time.sleep(1.0)
        time.sleep(2.0)

        self._mso_resource.write(":save:waveform:fileformat auto")

        run_number = self._setup_model.run_number
        load = self._experiment_model.load
        temperature = self._experiment_model.temperature

        timestamp = ""
        if self._experiment_model.repetitions == 1:
            timestamp = "_" + datetime.now().strftime("%m.%d.%Y_%H.%M.%S")

        filename = (
            self._basedir
            + f"{run_number}_{load}ton_{temperature}K_{frequency}MHz{timestamp}"
        )
        if self._experiment_model.repetitions > 1:
            scan = self._experiment_model.scan
            filename += f"_{scan}{step}"

        filename += ".csv"

        self._mso_resource.write(f":save:waveform ch1, '{filename}'")

        self.new_feedback_message.emit(
            f"Waveform data at {frequency}MHz save in file {filename}."
        )

        time.sleep(2.0)

    def _send_signal(self, frequency: float, number_of_cycles: int) -> None:
        """Sends the collection commands to the afg instrument."""
        vpp = self._setup_model.vpp

        self._afg_resource.write(":output1:state off")
        self._afg_resource.write(":source1:burst:ncycles 1")

        if number_of_cycles == 2:
            self._afg_resource.write(":source1:function:shape user1")
            self._afg_resource.write(f":source1:frequency {frequency * 1.0e6/2.0}")
        else:
            self._afg_resource.write(":source1:function:shape sin")
            self._afg_resource.write(f":source1:frequency {frequency * 1.0e6}")

        self._afg_resource.write(f":source1:voltage {vpp}")
        self._afg_resource.write(":source1:phase 0.0e0")
        self._afg_resource.write(":source1:voltage:offset 0.0e0")
        self._afg_resource.write(":output1:state on")

        self.new_feedback_message.emit(
            f"Sending {number_of_cycles} cycle(s) {frequency}MHz signal with Vpp = {vpp}V."
        )

    def collect_data(self, abort_status: bool) -> None:
        """Runs the data collection loop, accounts for multiple iterations."""

        if self.connected:
            repetitions = self._experiment_model.repetitions
            current_index = 0

            file_number = self._experiment_model.file_number

            while repetitions > 0:

                if abort_status:
                    return None

                current_index += 1
                self.current_repetition.emit(current_index)
                self._collection_process(abort_status=abort_status, step=file_number)
                repetitions -= 1
                file_number += 1

    def restore_defaults(self) -> None:
        reset_frequency = self._experiment_model.reset_frequency
        """Sends some default values to the instruments."""
        if self.connected:
            self._afg_resource.write(":source1:burst:ncycles 1")
            self._afg_resource.write(":source1:function:shape user1")
            self._afg_resource.write(f":source1:frequency {reset_frequency * 1.0e6 / 2.0}")
            self._afg_resource.write(":output1:state on")

            self._mso_resource.write("acquire:stopafter runstop")
            self._mso_resource.write(":acquire:state run")

    def _collection_process(self, abort_status: bool, step: Optional[int] = 1) -> None:
        """The collection process for one iteration, multiple frequencies can be used."""

        for index, frequency in enumerate(self._experiment_model.frequencies):

            if frequency > self._experiment_model.threshold:
                number_of_cycles = 2
            else:
                number_of_cycles = 1

            self._send_signal(frequency=frequency, number_of_cycles=number_of_cycles)
            self._acquire_signal(
                frequency=frequency, step=step, abort_status=abort_status
            )
