from dialogs import ParametrizationDialog
from simulator import SimulationWindow
from modules.utils import models
from modules.qt.specx_qt_ui import UiMainWindow, QtWidgets


# ---- GUI default values ----
DEFAULT_SAMPLE_TIME = 5
DEFAULT_THRESHOLD = 0.33


# ---- GUI labels ----
ENERGY_LABEL = 'energy'
SAMPLING_LABEL = 'sampling'
THRESHOLD_LABEL = 'threshold'
USAGE_LABEL = 'usage'


# ---- GUI messages ----
EXIT_MESSAGE = '¿Are you sure you want to quit?'
FILE_LOADED = 'Environment settings has been loaded successfully'
FILE_SAVED = 'Environment settings has been saved successfully'
LOAD_CONFIG = 'Load environment'
SAVE_CONFIG = 'Save environment'


class SpecxMainWindow(QtWidgets.QMainWindow, UiMainWindow):
    """
    Main class with all GUI components required for to configure simulation scenarios
    """

    def __init__(self, *args, **kwargs):
        super(SpecxMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)  # Build the GUI designed with Qt designer

        self.environment = models.SimulationEnvironment(id='test')
        self.add_channels()

        # Menu signals connection
        self.new_action_menu.triggered.connect(self.new_sim)
        self.exit_action_menu.triggered.connect(self.close)
        self.about_action_menu.triggered.connect(self.about)
        self.help_action_menu.triggered.connect(self.help)

        # Button signals connection
        self.btn_simulator.clicked.connect(self.__start_simulation)
        self.btn_clean.clicked.connect(self.reset_field_values)
        self.btn_save_file.clicked.connect(self.__save_environment)
        self.btn_load_file.clicked.connect(self.__load_environment)

        # ComboBox binding to the parametrization window modal
        for box in self.boxes:
            box.activated.connect(self.show_parametrization_modal)

    def add_channels(self):
        for index in range(len(self.boxes)):
            channel = models.Channel(
                id=index,
                frequency=self.labels[index].text(),
            )
            self.environment.add_or_update_channel(channel)

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

    # def __load_config(self, channels, parameters):
    #     """
    #     Configure the JSON loaded values in the GUI
    #     """
    #     self.channels = channels.copy()
    #     self.parameters = parameters.copy()
    #     for channel, content in self.channels.items():
    #         index = content.get('id')
    #         distribution = content.get('distribution')
    #         box = self.boxes[index - 1]
    #         if distribution:
    #             box.setCurrentText(
    #                 distribution.get('name', c.BOX_DEFAULT_ITEM)
    #             )
    #             self.generators.insert(
    #                 index - 1,
    #                 c.GENERATORS.get(box.currentText())
    #             )
    #         else:
    #             box.setCurrentText(c.BOX_DEFAULT_ITEM)
    #     self.__check_boxes()
    #     self.energy_flag.setChecked(self.parameters.get(c.ENERGY))
    #     self.sample_time.setValue(self.parameters.get(c.SAMPLING))
    #     self.threshold.setValue(self.parameters.get(c.THRESHOLD))
    #     self.usage_flag.setChecked(self.parameters.get(c.USAGE))

    def new_sim(self):
        """
        Delete all current settings in the GUI (Default values are loaded)
        """
        self.reset_field_values()

    def show_parametrization_modal(self):
        """
        Shows a modal window to parameterize a selected distribution
        """
        current_channel = models.Channel()
        distribution_key = self.sender().currentText()
        for channel in self.environment.channels:
            if channel.id == self.boxes.index(self.sender()):
                channel.distribution = models.find_distribution(distribution_key)()
                current_channel = channel

        modal = ParametrizationDialog(self, distribution=current_channel.distribution)
        modal.exec()

        if modal.result() == 1:
            pass
        else:
            self.sender().setCurrentIndex(-1)
        self.check_boxes()
        # print(self.environment)
        # for channel in self.environment.channels:
        #     print(channel)

    def reset_field_values(self):
        """
        Reset all current settings in the GUI (Default values will be loaded)
        """
        self.sample_time.setValue(DEFAULT_SAMPLE_TIME)
        self.threshold.setValue(DEFAULT_THRESHOLD)
        for box in self.boxes:
            box.setCurrentIndex(-1)
        self.__check_boxes()

    def __start_simulation(self):
        """
        Shows a window with the simulation options and charts
        """
        sim_window = SimulationWindow(self, environment=self.environment)
        sim_window.show()

    def __save_environment(self):
        """
        Save the parametrized channels distribution (discrete or continuous) to a JSON file
        """
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Save environment',
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            self.environment.set_settings({
                SAMPLING_LABEL: self.sample_time.value(),
                THRESHOLD_LABEL: self.threshold.value(),
                ENERGY_LABEL: self.energy_flag.isChecked(),
                USAGE_LABEL: self.usage_flag.isChecked(),
            })
            self.environment.save_as_json(filepath)
            QtWidgets.QMessageBox.information(
                self,
                'Information',
                f'File saved at {filepath}',
                QtWidgets.QMessageBox.Ok,
                QtWidgets.QMessageBox.Ok
            )

    def __load_environment(self):
        """
        Load the parametrized channels distribution (discrete or continuous) from a JSON file
        """
        filepath, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Load environment',
            '../config',
            'JSON Files (*.json)'
        )
        if filepath:
            pass
            # success = manager.load_json(filepath)
            # if success:
            #     self.__load_config(
            #         manager.SETTINGS.get(c.CHANNELS),
            #         manager.SETTINGS.get(c.PARAMETERS),
            #     )
            #     QtWidgets.QMessageBox.information(
            #         self,
            #         'Information',
            #         c.FILE_LOADED,
            #         QtWidgets.QMessageBox.Ok,
            #         QtWidgets.QMessageBox.Ok
            #     )

    def check_boxes(self):
        """
        Check each distribution box in order to verify that all channels have been parameterized
        """
        # activation_key = bool()
        for box in self.boxes:
            if box.currentIndex() == -1:  # -1 is the placeholder index
                self.btn_simulator.setEnabled(False)
                self.btn_save_file.setEnabled(False)
                return

        self.btn_simulator.setEnabled(True)
        self.btn_save_file.setEnabled(True)


# App launcher block
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    window = SpecxMainWindow()
    window.show()
    sys.exit(app.exec_())
