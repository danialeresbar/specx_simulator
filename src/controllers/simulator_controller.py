import qdarktheme

from collections.abc import Iterable
from functools import cache, partial
from PySide6 import QtWidgets

from constants.paths import ENVIRONMENT_COLLECTION_PATH, UI_PATH
from constants.ui import (
    LOAD_SIMULATION_EXPERIMENT_CAPTION,
    LOAD_SIMULATION_EXPERIMENT_ERROR_TEXT,
    LOAD_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
    SAVE_SIMULATION_EXPERIMENT_CAPTION,
    SAVE_SIMULATION_EXPERIMENT_ERROR_TEXT,
    SAVE_SIMULATION_EXPERIMENT_SUCCESS_TEXT
)
from controllers.simulation_channel_controller import ChannelConfigController
from models.distribution import ProbabilityDistribution
from models.simulation import SimulationExperiment, SimulationMeasurement
from tools.files import export_json, load_json
from views.resources.custom import DefaultChannelConfigView
from views.simulator_view import SimulatorView

CONTINUOUS_PROBABILITY_DISTRIBUTIONS_FIXTURE = f'{UI_PATH}/content/continuous_probability_distributions.json'
DISCRETE_PROBABILITY_DISTRIBUTIONS_FIXTURE = f'{UI_PATH}/content/discrete_probability_distributions.json'


@cache
def _load_fixture(fp: str):
    """
    Load the fixture file and return its content.

    :param fp: The fixture file path.
    :return: The fixture content.
    """
    return load_json(filepath=fp)


class Simulator(QtWidgets.QMainWindow, SimulatorView):
    """"""
    def __init__(self, experiment: SimulationExperiment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.experiment: SimulationExperiment = experiment
        self.setup_ui(self)
        qdarktheme.setup_theme('dark')
        self.__connect_button_signals()
        self.initialize_components()

    def __connect_button_signals(self):
        """
        Connect the header buttons signals
        """
        # Simulation settings
        self.simulation_energy_selector_btn.toggled.connect(self.enable_experiment_settings)
        self.simulation_occupancy_selector_btn.toggled.connect(self.enable_experiment_settings)
        self.load_simulation_settings_btn.clicked.connect(self.load_simulation_environment)
        self.save_simulation_settings_btn.clicked.connect(self.save_simulation_environment)

        # Simulation channels
        def set_channel_config_page(page: int) -> None:
            """
            Set the current page of the frequency setup area to the given page
            index.

            :param page: The page index.
            """
            self.simulation_frequency_setup_area.setCurrentIndex(page)

        for index in range(len(self.experiment.channels)):
            button: QtWidgets.QPushButton = getattr(self, f'channel_{index + 1}_btn')
            button.clicked.connect(partial(set_channel_config_page, page=index + 1))

    def _update_experiment_channels(self) -> None:
        for index, channel in enumerate(self.experiment.channels, start=1):
            channel_config: ChannelConfigController = self.simulation_frequency_setup_area.widget(index)
            # TODO: Pick the UI component values and update the channel fields

    def _update_simulation_frequency_setup_area(self, distributions: Iterable[ProbabilityDistribution]) -> None:
        for index, channel in enumerate(self.experiment.channels, start=1):
            channel_config: ChannelConfigController = self.simulation_frequency_setup_area.widget(index)
            ChannelConfigController.clean_parameters_layout(layout=channel_config.function_parameters_frame.layout())
            channel_config.refresh_selector_options(options=distributions)
            channel_config.function_chart_frame.set_default_content()

    def enable_experiment_settings(self, checked: bool) -> None:
        """
        Enable the experiment settings when the energy or occupancy button is
        checked.

        :param checked: The state of the button.
        """
        if not checked:
            return

        sender = self.sender()
        measurement: SimulationMeasurement = (
            SimulationMeasurement.ENERGY
            if sender is self.simulation_energy_selector_btn
            else SimulationMeasurement.OCCUPANCY
        )
        self.experiment.settings.measurement = measurement
        self.simulation_parameters_frame.setEnabled(True)
        self.simulation_settings_buttons_frame.setEnabled(True)
        self.simulation_channel_frame.setEnabled(True)
        self.simulation_threshold_label.setEnabled(measurement == SimulationMeasurement.ENERGY)
        self.simulation_threshold_box.setEnabled(measurement == SimulationMeasurement.ENERGY)
        fp = (
            CONTINUOUS_PROBABILITY_DISTRIBUTIONS_FIXTURE
            if measurement == SimulationMeasurement.ENERGY
            else DISCRETE_PROBABILITY_DISTRIBUTIONS_FIXTURE
        )
        self._update_simulation_frequency_setup_area(
            distributions=ProbabilityDistribution.from_fixture(fixture=_load_fixture(fp))
        )

    def initialize_components(self) -> None:
        # Frames and Areas
        self.simulation_channel_frame.setEnabled(False)
        # self.simulation_player_frame.setEnabled(False)
        self.simulation_parameters_frame.setEnabled(False)
        self.simulation_settings_buttons_frame.setEnabled(False)
        default_index: int = self.simulation_frequency_setup_area.addWidget(DefaultChannelConfigView(self))
        self.simulation_frequency_setup_area.setCurrentIndex(default_index)

        # Load UI components default values
        for _ in self.experiment.channels:
            self.simulation_frequency_setup_area.addWidget(ChannelConfigController(self))

        self.simulation_sampling_box.setValue(self.experiment.settings.sample_interval)
        self.simulation_threshold_box.setValue(self.experiment.settings.energy_threshold)

    def start_simulation(self) -> None:
        pass

    def load_simulation_environment(self) -> None:
        """
        Load a simulation environment from a JSON file.
        """
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            LOAD_SIMULATION_EXPERIMENT_CAPTION,
            ENVIRONMENT_COLLECTION_PATH,
            'Simulation settings (*.json)'
        )
        if not filepath:
            return

        try:
            self.experiment: SimulationExperiment = SimulationExperiment(**load_json(filepath))
            self.initialize_components()
        except Exception:
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                LOAD_SIMULATION_EXPERIMENT_ERROR_TEXT,
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )
            return

        QtWidgets.QMessageBox.information(
            self,
            LOAD_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
            f'File loaded from {filepath}',
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )

    def save_simulation_environment(self) -> None:
        """
        Save the current simulation experiment. The experiment settings and
        channels parameters will be saved in a JSON file. The user will be
        prompted to select the file path.
        """
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_SIMULATION_EXPERIMENT_CAPTION,
            ENVIRONMENT_COLLECTION_PATH,
            'Simulation settings (*.json)'
        )
        if not filepath:
            return

        try:
            export_json(filepath=filepath, data=self.experiment.model_dump_json())
        except Exception:
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                SAVE_SIMULATION_EXPERIMENT_ERROR_TEXT,
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )
            return

        QtWidgets.QMessageBox.information(
            self,
            SAVE_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
            'File saved at {filepath}',
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok
        )
