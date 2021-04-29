from PyQt5 import QtWidgets

from src.model import simulation
from src.model.distributions import continuous, discreet
from src.dialogs import ParametrizationDialog
from src.qt.mainview import MainViewTemplate
from src.simulator import Simulation
from src.tools import json_exporter, json_importer


# ---- Paths ----
ENVIRONMENTS_PATH = '../environments'

# ---- Messages ----
EXIT_MESSAGE = '¿Are you sure you want to quit?'
ENVIRONMENT_LOADED_MESSAGE = 'Simulation environment settings has been loaded successfully'
ENVIRONMENT_SAVED_MESSAGE = 'Simulation environment settings has been saved successfully'
LOAD_ENVIRONMENT_MESSAGE = 'Load simulation environment'
SAVE_ENVIRONMENT_MESSAGE = 'Save simulation environment'


class SpecxMainWindow(QtWidgets.QMainWindow, MainViewTemplate):
    """
    Class used for the creation of the main window of the simulation software.
    Here the simulation scenarios on which tests will be done are configured
    """

    def __init__(self):
        self.environment = simulation.Environment(id='uJ96^YJtgTbkLHxA')
        super(SpecxMainWindow, self).__init__()
        self.setup(self)

        # Signals
        self._connect_button_signals()
        self._connect_drop_signals()
        self._connect_menu_signals()

    def _connect_button_signals(self):
        """
        Button signal connection
        """

        self.btn_simulator.clicked.connect(self.start_simulation)
        self.btn_clean.clicked.connect(self._reset_component_values)
        self.btn_save_settings.clicked.connect(self.save_environment)
        self.btn_load_settings.clicked.connect(self.load_environment)

    def _connect_drop_signals(self):
        """
        Drop down signal connection
        """

        for drop in self.channel_drops:
            drop.setCurrentIndex(-1)
            drop.activated.connect(self.show_parametrization_modal)

    def _connect_menu_signals(self):
        """
        Menu signal connection
        """

        self.action_menu_new.triggered.connect(self.new_simulation_environment)
        self.action_menu_exit.triggered.connect(self.close)
        self.action_menu_about.triggered.connect(self.about)
        self.action_menu_help.triggered.connect(self.help)

    def _reset_component_values(self):
        """
        Reset all current settings in the GUI (Default values will be loaded)
        """
        self.sample_time.setValue(simulation.DEFAULT_SAMPLE_INTERVAL_VALUE)
        self.threshold.setValue(simulation.DEFAULT_THRESHOLD_VALUE)
        for drop in self.channel_drops:
            drop.setCurrentIndex(-1)

    def _setup_from_simulation_environment(self, data):
        """

        :param data:
        :return:
        """
        try:
            channels = data.get('channels')
            settings = data.get('settings')
            self.sample_time.setValue(settings.get('sample_interval'))
            self.threshold.setValue(settings.get('threshold'))
            self.energy_flag.setChecked(settings.get('energy'))
            self.usage_flag.setChecked(settings.get('usage'))
            for drop, channel in zip(self.channel_drops, channels):
                distribution = channel.get('distribution')
                drop.setCurrentText(distribution.get('name'))
        except Exception as e:
            print(f'Error: {e}')

    def about(self):
        """
        Short Software description
        """

        pass

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """

        # close = QtWidgets.QMessageBox.information(
        #     self,
        #     'Exit',
        #     c.EXIT_MESSAGE,
        #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #     QtWidgets.QMessageBox.No
        # )
        # if close == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        event.accept()

    def help(self):
        """

        """

        pass

    def new_simulation_environment(self):
        """
        Delete all current settings in the GUI. Default values are loaded
        and the data of the former simulation environment is deleted
        """

        self._reset_component_values()
        self.btn_simulator.setEnabled(False)
        self.environment = simulation.Environment(id='uJ96^YJtgTbkLHxA')

    def show_parametrization_modal(self):
        """
        Shows a modal window to parameterize the selected distribution
        on the drop down
        """

        # Sender attributes
        sender_index = self.channel_drops.index(self.sender())
        sender_text = self.sender().currentText()

        # Create or update channel
        new_channel = simulation.Channel(
            number=sender_index,
            frequency=self.channel_labels[sender_index].text(),
            distribution=continuous.DISTRIBUTIONS.get(sender_text)()
        )

        modal = ParametrizationDialog(self, distribution=new_channel.distribution)
        modal.exec()

        if modal.result() == 1:
            self.environment.add_or_update_channel(new_channel)
            self.btn_simulator.setEnabled(len(self.environment.channels) == len(self.channel_drops))
            self.btn_save_settings.setEnabled(len(self.environment.channels) == len(self.channel_drops))
        else:
            self.sender().setCurrentIndex(-1)

    def start_simulation(self):
        """
        Shows a window with the simulation options and channel's chart
        """

        try:
            simulator = Simulation(self, id='test', environment=self.environment)
            simulator.show()
        except Exception as e:
            print(f'The Simulation could not be initialized: \n{e}')

    def save_environment(self):
        """
        Save the simulation environment settings to a JSON file
        """

        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_ENVIRONMENT_MESSAGE,
            ENVIRONMENTS_PATH,
            'JSON Files (*.json)'
        )
        if filepath:
            settings = [
                self.sample_time.value(),
                self.threshold.value(),
                self.energy_flag.isChecked(),
                self.usage_flag.isChecked()
            ]
            self.environment.update_settings(settings)
            json_exporter.save(filepath, self.environment.to_json())
            QtWidgets.QMessageBox.information(
                self,
                ENVIRONMENT_SAVED_MESSAGE,
                f'File saved at {filepath}',
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )

    def load_environment(self):
        """
        Load the simulation environment settings from a JSON file
        """

        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            LOAD_ENVIRONMENT_MESSAGE,
            ENVIRONMENTS_PATH,
            'JSON Files (*.json)'
        )
        if filepath:
            self._setup_from_simulation_environment(json_importer.load(filepath))
            QtWidgets.QMessageBox.information(
                self,
                'Information',
                ENVIRONMENT_LOADED_MESSAGE,
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )


# App launcher block code
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = SpecxMainWindow()
    window.show()
    sys.exit(app.exec_())
