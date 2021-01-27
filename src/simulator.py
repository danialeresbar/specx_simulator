from datetime import datetime
from uuid import uuid4

from modules.qt.simulator_qt_ui import UiSimWindow, QtWidgets, QtGui
from modules.utils.thread_tools import FileThread, SimulationThread


# ---- Date formats ----
DATE_FORMAT = "%m-%d-%Y-%H-%M-%S"


# ---- GUI default values ----
DEFAULT_SPEED = 1
MAX_SPEED = 64
MIN_SPEED = 1/MAX_SPEED


# ---- GUI messages ----
SAVE_CHART_MESSAGE = 'Save chart'
SAVE_CHART_SUCCESS = 'Chart saved successfully'


# ---- Paths ----
PROJECT_PATH = '../../'
SETTINGS_PATH = f'{PROJECT_PATH}/config'
SIMULATIONS_PATH = f'{PROJECT_PATH}/simulations/'


class SimulationWindow(QtWidgets.QMainWindow, UiSimWindow):
    """
    Class with the components required to simulate a scenario (Previously configured in the Main window)
    """

    def __init__(self, **kwargs):
        super(SimulationWindow, self).__init__()
        self.setupUi(self)

        self.environment = kwargs.get('environment', None)
        self.simulation_filepath = f'{SIMULATIONS_PATH}Simulation-{datetime.now().strftime(DATE_FORMAT)}.csv'
        self.speed_factor = 1

        # Button signals connection
        self.btn_start.clicked.connect(self.__start)
        self.btn_play.clicked.connect(self.__resume)
        self.btn_pause.clicked.connect(self.__pause)
        self.btn_stop.clicked.connect(self.__stop)
        self.btn_increase_speed.clicked.connect(self.increase_speed)
        self.btn_decrease_speed.clicked.connect(self.decrease_speed)
        self.btn_max_speed.clicked.connect(self.__max_speed)
        self.btn_reset_speed.clicked.connect(self.__default_speed)
        self.btn_save_chart.clicked.connect(self.save_chart)
        self.btn_open_csvfile.clicked.connect(self.show_outfile)

        self.__prepare_simulation()

    def closeEvent(self, event):
        """
        Override of the closeEvent method to close the window
        """
        # close = QtWidgets.QMessageBox.information(
        #     self,
        #     'Exit',
        #     "Do you want close this simulation window?",
        #     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #     QtWidgets.QMessageBox.No
        # )
        # if close == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()
        event.accept()

    def plot_channel_charts(self):
        """
        Build and initialize the graphs of each channel taking into account whether the assigned distribution
        is continuous or discrete simulation
        """
        pass
        # index = 0
        # for channel in self.channels.values():
        #     if channel["distribution"].get('name') == c.BERNOULLI:
        #         chart = LineChart(title="Canal {}".format(channel.get("id")))
        #         self.series.append(
        #             chart.dynamic_line()
        #         )
        #         self.chartviews[index].setChart(chart)
        #     else:
        #         chart = SplineChart(title="Canal {}".format(channel.get("id")))
        #         self.series.append(
        #             chart.dynamic_spline()
        #         )
        #         self.chartviews[index].setChart(chart)
        #     index += 1
        #
        # self.percent_chart = BarChart(
        #     title="%  Channel usage",
        #     parameters=self.channels.copy()
        # )
        # self.series.append(self.percent_chart.plot_bar_chart())
        # self.chartviews[9].setChart(self.percent_chart)

    def __prepare_simulation(self):
        """
        Prepare the simulation scenario by calling each setting method
        """
        self.__simulation_btn_mannager(True, False, False, False)
        self.__speed_btn_mannager(False, False, False, False)
        self.series = list()
        self.plot_channel_charts()

    def save_chart(self):
        """
        Save the selected chart in one of the available formats
        """
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_CHART_MESSAGE,
            f'{self.environment.id}-{self.environment.timestamp}-chart',
            "JPG (*.jpg);;PNG (*.png)",
            options=QtWidgets.QFileDialog.Options()
        )

        if filepath:
            output = QtGui.QPixmap(self.chartviews[9].grab())
            output.save(filepath, quality=100)
            if output:
                QtWidgets.QMessageBox.information(
                    self,
                    SAVE_CHART_MESSAGE,
                    SAVE_CHART_SUCCESS,
                    QtWidgets.QMessageBox.Ok
                )
            else:
                QtWidgets.QMessageBox.critical(
                    self,
                    SAVE_CHART_MESSAGE,
                    'Error',
                    QtWidgets.QMessageBox.Ok
                )

    def show_outfile(self):
        """
        Opens an instance of the file with the results of the current simulation
        """
        self.__file_thread = FileThread(
            name=f'File-{self.simulation_filepath}',
            kwargs={
                'filepath': self.simulation_filepath
            }
        )
        self.__file_thread.setDaemon(True)
        self.__file_thread.start()

    def __start(self):
        """
        Start the simulation process
        """
        self.__thread = SimulationThread(
            name=f'Simulation-{uuid4()}',
            target=self.speed_value,
            kwargs={
                'callback': self.__finish_sim,
                'channels': self.channels.copy(),
                'filepath': self.simulation_filepath,
                'generators': self.generators.copy(),
                'parameters': self.parameters.copy(),
                'series': self.series.copy()
            }
        )
        self.__thread.setDaemon(True)
        self.__thread.start()
        self.__simulation_btn_mannager(False, False, True, True)
        self.__speed_btn_mannager(True, True, True, True)
        self.btn_start.setText("RESTART")

    def __resume(self):
        self.__thread.resume()
        self.__simulation_btn_mannager(False, False, True, True)

    def __pause(self):
        self.__thread.pause()
        self.__simulation_btn_mannager(False, True, False, True)

    def __stop(self):
        if self.__thread.is_alive:
            if self.__thread.paused:
                self.__thread.resume()
                self.__thread.stop()
            else:
                self.__thread.stop()
            self.__speed_btn_mannager(False, False, False, False)
            self.__simulation_btn_mannager(True, False, False, False)
        self.__prepare_simulation()

    def speed_value(self):
        return self.speed

    def increase_speed(self):
        self.speed *= 2
        self.__speed_btn_mannager(True, True, True, True)
        if self.speed < 1:
            self.label_speed.setText("X{}".format(self.speed))
        else:
            self.label_speed.setText("X{}".format(int(self.speed)))
        if self.speed == c.MAX_SPEED:
            self.__speed_btn_mannager(False, True, False, True)

    def decrease_speed(self):
        self.speed /= 2
        self.__speed_btn_mannager(True, True, True, True)
        if self.speed < 1:
            self.label_speed.setText("X{}".format(self.speed))
        else:
            self.label_speed.setText("X{}".format(int(self.speed)))
        if self.speed == c.MIN_SPEED:
            self.__speed_btn_mannager(True, False, True, True)

    def __default_speed(self):
        self.speed = 1
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.__speed_btn_mannager(True, True, True, True)

    def __max_speed(self):
        self.speed = c.MAX_SPEED
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.__speed_btn_mannager(False, True, False, True)

    def __simulation_btn_mannager(self, f1, f2, f3, f4):
        self.btn_start.setEnabled(f1)
        self.btn_play.setEnabled(f2)
        self.btn_pause.setEnabled(f3)
        self.btn_stop.setEnabled(f4)

    def __speed_btn_mannager(self, f1, f2, f3, f4):
        self.btn_increase_speed.setEnabled(f1)
        self.btn_decrease_speed.setEnabled(f2)
        self.btn_max_speed.setEnabled(f3)
        self.btn_reset_speed.setEnabled(f4)

    def __finish_sim(self, interrupted):
        self.__simulation_btn_mannager(True, False, False, False)
        self.__speed_btn_mannager(False, False, False, False)
        self.speed = 1
        self.label_speed.setText("X{}".format(int(self.speed)))
        self.btn_open_csvfile.setEnabled(interrupted)
        self.btn_save_chart.setEnabled(interrupted)
