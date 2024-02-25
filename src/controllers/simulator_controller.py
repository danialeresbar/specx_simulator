import qdarktheme

from collections.abc import Iterable
from functools import cache
from PySide6 import QtWidgets

from constants.paths import EXPERIMENT_COLLECTION_PATH, UI_PATH
from constants.simulation import (
    SIMULATION_EXPERIMENT_NOT_READY_CAPTION,
    SIMULATION_EXPERIMENT_READY_CAPTION,
)
from constants.ui import (
    DARK_THEME,
    LOAD_SIMULATION_EXPERIMENT_CAPTION,
    LOAD_SIMULATION_EXPERIMENT_ERROR_TEXT,
    LOAD_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
    SAVE_SIMULATION_EXPERIMENT_CAPTION,
    SAVE_SIMULATION_EXPERIMENT_ERROR_TEXT,
    SAVE_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
)
from controllers.simulation_channel_controller import ChannelConfigController
from models.distribution import ProbabilityDistribution
from models.simulation import SimulationExperiment, SimulationMeasurement
from tools.files import export_json, load_json
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
    """
    This class is responsible for controlling the simulation experiment. It
    connects the UI components with the simulation experiment model.
    """

    def __init__(self, experiment: SimulationExperiment, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.experiment: SimulationExperiment = experiment
        self.setup_ui(self)
        qdarktheme.setup_theme(DARK_THEME)
        self.initialize_component_values()
        self.__connect_button_signals()

    @property
    def experiment_is_ready(self) -> bool:
        """
        Check if the experiment is ready to start. The experiment is ready if
        the simulation settings and the channels are ready.

        :return: True if the experiment is ready, False otherwise.
        """
        return all(
            (
                self.channel_config_stack_area.widget(index).is_ready
                for index in range(self.channel_config_stack_area.count())
            )
        )

    def __connect_button_signals(self) -> None:
        """
        Connect the signals of the buttons to the corresponding slots. This
        method MUST be called in the constructor of the class.
        """
        # Simulation settings
        self.simulation_energy_selector_btn.toggled.connect(self.enable_experiment_settings)
        self.simulation_occupancy_selector_btn.toggled.connect(self.enable_experiment_settings)
        self.load_simulation_settings_btn.clicked.connect(self.load_simulation_environment)
        self.save_simulation_settings_btn.clicked.connect(self.save_simulation_environment)

        # Simulation channels
        def set_channel_config_page(button: QtWidgets.QAbstractButton) -> None:
            """
            Set the current page of the frequency setup area to the given page
            index.

            :param button: The button that was clicked.
            """
            self.channel_config_stack_area.setCurrentIndex(self.channel_button_group_widget.btn_group.id(button))

        self.channel_button_group_widget.btn_group.buttonClicked.connect(set_channel_config_page)

    def _load_experiment_channel_data(self) -> None:
        for index, channel in enumerate(self.experiment.channels):
            channel_config: ChannelConfigController = self.channel_config_stack_area.widget(index)
            selector: QtWidgets.QComboBox = channel_config.function_selector_box
            selector.setCurrentText(channel.associated_distribution.name)
            selector.setItemData(channel_config.function_selector_box.currentIndex(), channel.associated_distribution)
            selector.currentIndexChanged.emit(selector.currentIndex())

        if self.experiment_is_ready:
            self.simulation_status_label.setText(SIMULATION_EXPERIMENT_READY_CAPTION)

    def _save_experiment_channel_data(self) -> None:
        for i, channel in enumerate(self.experiment.channels):
            channel_config: ChannelConfigController = self.channel_config_stack_area.widget(i)
            channel.associated_distribution = channel_config.function_selector_box.currentData()
            for j, parameter in enumerate(channel_config.get_available_function_parameter_values()):
                channel.associated_distribution.parameters[j].value = parameter

    def _update_channel_config_stack_area_components(self, distributions: Iterable[ProbabilityDistribution]) -> None:
        """
        Update the channel stack area with the available probability distributions.

        :param distributions: The available probability distributions.
        """
        for index in range(self.channel_config_stack_area.count()):
            channel_config: ChannelConfigController = self.channel_config_stack_area.widget(index)
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

        sender: QtWidgets.QAbstractButton = self.sender()
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
        self.save_simulation_settings_btn.setEnabled(True)
        fp: str = (
            CONTINUOUS_PROBABILITY_DISTRIBUTIONS_FIXTURE
            if measurement == SimulationMeasurement.ENERGY
            else DISCRETE_PROBABILITY_DISTRIBUTIONS_FIXTURE
        )
        self.channel_config_stack_area.setEnabled(True)
        self._update_channel_config_stack_area_components(
            distributions=ProbabilityDistribution.from_fixture(fixture=_load_fixture(fp))
        )

    def initialize_component_values(self) -> None:
        # Frames and Areas
        self.simulation_channel_frame.setEnabled(False)
        self.simulation_parameters_frame.setEnabled(False)

        # Load UI components default values
        self.channel_config_stack_area.clear()
        for _ in self.experiment.channels:
            self.channel_config_stack_area.addWidget(ChannelConfigController(self))

        self.channel_button_group_widget.initialize_buttons(
            button_labels=[channel.frequency for channel in self.experiment.channels]
        )
        self.channel_config_stack_area.setEnabled(False)
        self.simulation_sampling_box.setValue(self.experiment.settings.sample_interval)
        self.simulation_threshold_box.setValue(self.experiment.settings.energy_threshold)

        # Experiment status
        self.simulation_status_label.setText(SIMULATION_EXPERIMENT_NOT_READY_CAPTION)

    def start_simulation_experiment(self) -> None:
        pass

    def load_simulation_environment(self) -> None:
        """
        Load a simulation environment from a JSON file. The user will be
        prompted to select the file path. The experiment settings and channels
        parameters will be loaded from the file. If the file is not valid, an
        error message will be shown.
        """
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            LOAD_SIMULATION_EXPERIMENT_CAPTION,
            EXPERIMENT_COLLECTION_PATH,
            'Simulation settings (*.json)',
        )
        if not filepath:
            return

        try:
            self.experiment: SimulationExperiment = SimulationExperiment(**load_json(filepath))
            self.initialize_component_values()
            if self.experiment.settings.measurement == SimulationMeasurement.ENERGY.value:
                self.simulation_energy_selector_btn.setChecked(True)
            else:
                self.simulation_occupancy_selector_btn.setChecked(True)

            self._load_experiment_channel_data()
        except Exception:
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                LOAD_SIMULATION_EXPERIMENT_ERROR_TEXT,
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok,
            )
            return

        QtWidgets.QMessageBox.information(
            self,
            LOAD_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
            f'File loaded from {filepath}',
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok,
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
            EXPERIMENT_COLLECTION_PATH,
            'Simulation settings (*.json)',
        )
        if not filepath:
            return

        try:
            self._save_experiment_channel_data()
            export_json(filepath=filepath, data=self.experiment.model_dump(mode='json'))
        except Exception:
            QtWidgets.QMessageBox.critical(
                self,
                'Error',
                SAVE_SIMULATION_EXPERIMENT_ERROR_TEXT,
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok,
            )
            return

        QtWidgets.QMessageBox.information(
            self,
            SAVE_SIMULATION_EXPERIMENT_SUCCESS_TEXT,
            f'File saved at {filepath}',
            QtWidgets.QMessageBox.Ok,
            QtWidgets.QMessageBox.Ok,
        )
