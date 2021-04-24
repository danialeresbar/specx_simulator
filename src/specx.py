from PyQt5 import QtWidgets

# from dialogs import ParametrizationDialog
# from simulator import SimulationScenario
from model import simulation
from src.qt.mainview import MainViewTemplate


# ---- GUI labels ----
ENERGY_LABEL = 'energy'
SAMPLING_LABEL = 'sampling'
THRESHOLD_LABEL = 'threshold'
USAGE_LABEL = 'usage'


# ---- GUI messages ----
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
        super(SpecxMainWindow, self).__init__()
        self.setup(self)                                                    # Build the GUI designed with Qt designer
        self.environment = simulation.Environment(id='uJ96^YJtgTbkLHxA')    # Random ID
        self.add_environment_channels()

        # Menu signals connection
        self.action_menu_new.triggered.connect(self.new_sim)
        self.action_menu_exit.triggered.connect(self.close)
        self.action_menu_about.triggered.connect(self.about)
        self.action_menu_help.triggered.connect(self.help)

        # Button signals connection
        self.btn_simulator.clicked.connect(self.start_simulation)
        self.btn_clean.clicked.connect(self.reset_settings)
        self.btn_save_settings.clicked.connect(self.save_environment)
        self.btn_load_settings.clicked.connect(self.load_environment)

        # ComboBox binding to the parametrization window modal
        for drop in self.channel_drops:
            drop.activated.connect(self.show_parametrization_modal)

    def add_environment_channels(self):
        """

        :return:
        """

        pass
        # for index, label in enumerate(self.labels):
        #     channel = simulation.Channel(number=index, frequency=label.text())
        #     self.environment.add_or_update_channel(channel)

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
        pass

    def setup_gui_components(self):
        """
        Configure the data of the GUI components using the information stored in the simulation environment loaded
        """
        pass

    def new_sim(self):
        """
        Delete all current settings in the GUI. Default values are loaded
        and the data of the former simulation environment is deleted
        """

        self.reset_settings()

    def show_parametrization_modal(self):
        """
        Shows a modal window to parameterize a selected distribution
        """
        selected_channel = simulation.Channel()
        distribution_key = self.sender().currentText()
        # for channel in self.environment.channels:
        #     if channel.id == self.boxes.index(self.sender()):
        #         # channel.distribution = models.distribution_selector(distribution_key)
        #         current_channel = channel
        #
        # modal = ParametrizationDialog(self, distribution=selected_channel.distribution)
        # modal.exec()
        # if modal.result() == 1:
        #     pass
        # else:
        #     self.sender().setCurrentIndex(-1)
        # self.check_boxes()
        # print(self.environment)
        # for channel in self.environment.channels:
        #     print(channel)

    def reset_settings(self):
        """
        Reset all current settings in the GUI (Default values will be loaded)
        """
        self.sample_time.setValue(simulation.DEFAULT_SAMPLE_INTERVAL_VALUE)
        self.threshold.setValue(simulation.DEFAULT_THRESHOLD_VALUE)
        for box in self.boxes:
            box.setCurrentIndex(-1)
        self.check_boxes()

    def start_simulation(self):
        """
        Shows a window with the simulation options and channel's chart
        """

        pass
        # simulation_scenario = SimulationScenario(self, id='test', environment=self.environment)
        # simulation_scenario.show()
        # try:
        #     simulation_scenario = SimulationScenario(self, id='test', environment=self.environment)
        #     simulation_scenario.show()
        #     self.simulation_scenarios.append(simulation_scenario)
        # except Exception as e:
        #     print(f'Simulation scenario could not be initialized: \n{e}')

    def save_environment(self):
        """
        Save the parametrized channels distribution (discrete or continuous) to a JSON file
        """

        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_ENVIRONMENT_MESSAGE,
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            # self.environment.set_settings({
            #     SAMPLING_LABEL: self.sample_time.value(),
            #     THRESHOLD_LABEL: self.threshold.value(),
            #     ENERGY_LABEL: self.energy_flag.isChecked(),
            #     USAGE_LABEL: self.usage_flag.isChecked(),
            # })
            # self.environment.save_as_json(filepath)
            QtWidgets.QMessageBox.information(
                self,
                ENVIRONMENT_SAVED_MESSAGE,
                f'File saved at {filepath}',
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )

    def load_environment(self):
        """
        Load the parametrized channels distribution (discrete or continuous) from a JSON file
        """

        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            LOAD_ENVIRONMENT_MESSAGE,
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            # self.environment = simulation.Environment()
            # success = self.environment.load_data(filepath)
            # if success:
            #     self.setup_gui_components()
            #     QtWidgets.QMessageBox.information(
            #         self,
            #         'Information',
            #         ENVIRONMENT_LOADED_MESSAGE,
            #         QtWidgets.QMessageBox.Ok,
            #         QtWidgets.QMessageBox.Ok
            #     )
            self.btn_simulator.setEnabled(True)

    def check_boxes(self):
        """
        Check each distribution box in order to verify that all channels have been parameterized
        """

        # activation_key = bool()
        for drop in self.channel_drops:
            if drop.currentIndex() == -1:  # -1 is the placeholder index
                self.btn_simulator.setEnabled(False)
                self.btn_save_settings.setEnabled(False)
                return

        self.btn_simulator.setEnabled(True)
        self.btn_save_settings.setEnabled(True)


# App launcher block code
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = SpecxMainWindow()
    window.show()
    sys.exit(app.exec_())
