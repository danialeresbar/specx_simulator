import qdarktheme

from functools import partial
from typing import Iterable, List

from PySide6 import QtWidgets

from constants.paths import ENVIRONMENT_COLLECTION_PATH, UI_PATH
from constants.ui import (
    LOAD_SIMULATION_ENVIRONMENT_CAPTION,
    LOAD_SIMULATION_ENVIRONMENT_ERROR_TEXT,
    LOAD_SIMULATION_ENVIRONMENT_SUCCESS_TEXT,
    SAVE_SIMULATION_ENVIRONMENT_CAPTION,
    SAVE_SIMULATION_ENVIRONMENT_ERROR_TEXT,
    SAVE_SIMULATION_ENVIRONMENT_SUCCESS_TEXT
)
from controllers.simulation_channel_controller import ChannelConfigController
from models.distribution import ProbabilityDistribution, DistributionParameter
from models.simulation import SimulationEnvironment, SimulationMeasurement
from tools.files import export_json, load_json
from views.simulation_channel_config_view import DefaultChannelConfigView
from views.simulator_view import SimulatorView


def get_continuous_distributions() -> List[ProbabilityDistribution]:
    distribution_data = load_json(f'{UI_PATH}/content/continuous_probability_distributions.json')
    continuous = []
    for pd in distribution_data:
        parameters = [DistributionParameter(**param) for param in pd.get('parameters')]
        continuous.append(
            ProbabilityDistribution(name=pd.get('name'), category=pd.get('category'), parameters=parameters, description=pd.get('description'))
        )

    return continuous


def get_discrete_distributions() -> List[ProbabilityDistribution]:
    distribution_data = load_json(f'{UI_PATH}/content/discrete_probability_distributions.json')
    discrete = []
    for pd in distribution_data:
        parameters = [DistributionParameter(**param) for param in pd.get('parameters')]
        discrete.append(
            ProbabilityDistribution(name=pd.get('name'), category=pd.get('category'), parameters=parameters, description=pd.get('description'))
        )

    return discrete


class Simulator(QtWidgets.QMainWindow, SimulatorView):
    """"""
    def __init__(self, simulation: SimulationEnvironment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.experiment: SimulationEnvironment = simulation
        self.setup_ui(self)
        qdarktheme.setup_theme('dark')
        self.__connect_button_signals()
        self.initialize_components()

    def __connect_button_signals(self):
        """
        Connect the header buttons signals
        """
        # Simulation settings
        self.simulation_energy_selector_btn.clicked.connect(self.enable_simulation_energy_measurement_options)
        self.simulation_occupancy_selector_btn.clicked.connect(self.enable_simulation_occupancy_measurement_options)
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

    def enable_simulation_energy_measurement_options(self) -> None:
        """
        Enable the energy measurement of the simulation. With this selection,
        only the probability distributions configured to simulate the energy
        level for a channel will be available.
        """
        self.experiment.settings.measurement = SimulationMeasurement.ENERGY
        # UI components
        self.simulation_parameters_frame.setEnabled(True)
        self.simulation_settings_buttons_frame.setEnabled(True)
        self.simulation_threshold_label.setEnabled(True)
        self.simulation_threshold_box.setEnabled(True)
        self.simulation_channel_frame.setEnabled(True)
        self._update_simulation_frequency_setup_area(distributions=get_continuous_distributions())

    def enable_simulation_occupancy_measurement_options(self) -> None:
        """
        Enable the occupancy measurement of the simulation. With this selection,
        only probability distributions configured to simulate the use for a
        channel are enabled.
        """
        self.experiment.settings.measurement = SimulationMeasurement.OCCUPANCY
        # UI components
        self.simulation_parameters_frame.setEnabled(True)
        self.simulation_settings_buttons_frame.setEnabled(True)
        self.simulation_threshold_label.setEnabled(False)
        self.simulation_threshold_box.setEnabled(False)
        self.simulation_channel_frame.setEnabled(True)
        self._update_simulation_frequency_setup_area(distributions=get_discrete_distributions())

    def initialize_components(self) -> None:
        # Frames and Areas
        self.simulation_channel_frame.setEnabled(False)
        self.simulation_player_frame.setEnabled(False)
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
            LOAD_SIMULATION_ENVIRONMENT_CAPTION,
            ENVIRONMENT_COLLECTION_PATH,
            'Simulation settings (*.json)'
        )
        if filepath:
            try:
                self.experiment: SimulationEnvironment = SimulationEnvironment(**load_json(filepath))
                self.initialize_components()
            except Exception:
                QtWidgets.QMessageBox.critical(
                    self,
                    'Error',
                    LOAD_SIMULATION_ENVIRONMENT_ERROR_TEXT,
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )
                return

            QtWidgets.QMessageBox.information(
                self,
                LOAD_SIMULATION_ENVIRONMENT_SUCCESS_TEXT,
                f'File loaded from {filepath}',
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )

    def save_simulation_environment(self) -> None:
        """
        Save the current simulation environment. The environment settings
        and all its internal components will be stored in JSON file so that
        it can be loaded at any time.
        """
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_SIMULATION_ENVIRONMENT_CAPTION,
            ENVIRONMENT_COLLECTION_PATH,
            'Simulation settings (*.json)'
        )
        if filepath:
            try:
                export_json(filepath=filepath, data=self.experiment.model_dump_json())
            except Exception:
                QtWidgets.QMessageBox.critical(
                    self,
                    'Error',
                    SAVE_SIMULATION_ENVIRONMENT_ERROR_TEXT,
                    QtWidgets.QMessageBox.Ok,
                    QtWidgets.QMessageBox.Ok
                )
                return
            QtWidgets.QMessageBox.information(
                self,
                SAVE_SIMULATION_ENVIRONMENT_SUCCESS_TEXT,
                f'File saved at {filepath}',
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )
