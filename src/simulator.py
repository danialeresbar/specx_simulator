from datetime import datetime
# from uuid import uuid4

from qt.simulator_qt_ui import UiSimWindow, QtWidgets, QtGui
from charts.charts import BarChart, LineChart, SplineChart
from tools.thread_tools import FileThread, SimulationThread


# ---- Date formats ----
DATE_FORMAT = "%m-%d-%Y %H-%M-%S"


# ---- GUI default values ----
DEFAULT_SPEED = 1
MAX_SPEED = 64
MIN_SPEED = 1/MAX_SPEED


# ---- GUI messages ----
SAVE_CHART_MESSAGE = 'Save chart'
SAVE_CHART_SUCCESS = 'Chart saved successfully'


# ---- Paths ----
PROJECT_PATH = '../'
ENVIRONMENTS_PATH = f'{PROJECT_PATH}/environments'
SIMULATIONS_PATH = f'{PROJECT_PATH}/simulations/'


class SimulationScenario(QtWidgets.QMainWindow, UiSimWindow):
    """
    Class with the components required to simulate a scenario (Previously configured in the Main window)
    """

    def __init__(self, *args, **kwargs):
        super(SimulationScenario, self).__init__(*args)
        self.setupUi(self)
        self.id = kwargs.get('id', None)
        self.environment = kwargs.get('environment', None)
        self.output_filepath = f'{SIMULATIONS_PATH}Simulation-{datetime.now().strftime(DATE_FORMAT)}.csv'
        self.speed_factor = 1
        self.channel_charts = list()
        self.build_channel_charts()
        self._control_manager(play=False, pause=False, stop=False)
        self.simulation = SimulationThread(
            channels=self.environment.channels,
            charts=self.channel_charts,
            delay=self.check_speed_value,
            sample_time=self.environment.settings.get('sampling'),
            threshold=self.environment.settings.get('threshold'),
        )

        # Simulation control button signals connection
        self.btn_start.clicked.connect(self.start)
        self.btn_play.clicked.connect(self.resume)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_save_chart.clicked.connect(self.save_chart)
        self.btn_show_csvfile.clicked.connect(self.show_csvfile)

        # Simulation speed button signals connection
        self.btn_increase_speed.clicked.connect(self.increase_speed)
        self.btn_decrease_speed.clicked.connect(self.decrease_speed)
        self.btn_max_speed.clicked.connect(self.max_speed)
        self.btn_reset_speed.clicked.connect(self.reset_speed)

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

    def check_speed_value(self):
        return self.speed_factor

    def build_channel_charts(self):
        """
        Build and initialize the graphs of each channel taking into account whether the assigned distribution
        is continuous or discrete simulation
        """
        for index, channel in enumerate(self.environment.channels):
            if channel.distribution.category == 'Discrete':
                channel_chart = LineChart(
                    title=f'{channel.frequency} Channel'
                )
            else:
                channel_chart = SplineChart(
                    title=f'{channel.frequency} Channel'
                )

            self.channel_charts.append(channel_chart)
            self.chartviews[index].setChart(channel_chart)

        barchart = BarChart(
            title='Usage percentage for TV channels',
            categories=[channel.frequency for channel in self.environment.channels],
            bars=[20, 10, 30, 50, 40, 70, 90, 40, 80]
        )

        self.channel_charts.append(barchart)
        self.chartviews[9].setChart(barchart)

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

    def show_csvfile(self):
        """
        Opens a file instance for show the results of the current simulation scenario
        """
        try:
            csvfile = FileThread(
                kwargs={
                    'filepath': self.output_filepath
                }
            )
            csvfile.setDaemon(True)
            csvfile.start()
        except Exception as e:
            print(f'Error opening CSV file:\n {e}')

    def reset_settings(self):
        self.reset_speed()
        self.btn_start.setText('START')

    def start(self):
        """
        Start the simulation process
        """
        try:
            self.simulation.setDaemon(True)
            self.simulation.start()
            self._control_manager(start=False, play=False)
        except Exception as e:
            print(f'Error in starting Simulation:\n {e}')

    def resume(self):
        """
        Resume the simulation process
        :return:
        """
        try:
            self.simulation.resume()
            self._control_manager(start=False, play=False)
        except Exception as e:
            print(f'Error in resuming Simulation:\n {e}')

    def pause(self):
        """
        Pause the simulation process
        :return:
        """
        try:
            self.simulation.pause()
            self._control_manager(start=False, pause=False)
        except Exception as e:
            print(f'Error in pausing Simulation:\n {e}')

    def stop(self):
        """
        Stop the simulation process
        """
        if self.simulation.is_alive():
            if self.simulation.paused():
                self.resume()
            try:
                self.simulation.stop()
                self._control_manager(play=False, pause=False, stop=False)
            except Exception as e:
                print(f'Error in stopping Simulation:\n {e}')

    def _control_manager(self, start=True, play=True, pause=True, stop=True):
        self.btn_start.setEnabled(start)
        self.btn_play.setEnabled(play)
        self.btn_pause.setEnabled(pause)
        self.btn_stop.setEnabled(stop)

    def _speed_manager(self, increase=True, decrease=True, max=True, reset=True):
        self.btn_increase_speed.setEnabled(increase)
        self.btn_decrease_speed.setEnabled(decrease)
        self.btn_max_speed.setEnabled(max)
        self.btn_reset_speed.setEnabled(reset)

    def increase_speed(self):
        increase = max = True
        self.speed_factor *= 2
        self.speed_label.setText(self._speed_formatter())
        if self.speed_factor == MAX_SPEED:
            increase = max = False
        self._speed_manager(increase=increase, max=max)

    #
    def decrease_speed(self):
        decrease = True
        self.speed_factor /= 2
        self.speed_label.setText(self._speed_formatter())
        if self.speed_factor == MIN_SPEED:
            decrease = False
        self._speed_manager(decrease=decrease)

    def max_speed(self):
        self.speed_factor = MAX_SPEED
        self.speed_label.setText(self._speed_formatter())
        self._speed_manager(increase=False, max=False)

    def reset_speed(self):
        self.speed_factor = DEFAULT_SPEED
        self.speed_label.setText(self._speed_formatter())
        self._speed_manager()

    def _speed_formatter(self):
        if self.speed_factor >= 1:
            return f'X{int(self.speed_factor)}'
        else:
            return f'X1/{int(1/self.speed_factor)}'

    def _finished(self):
        self.reset_settings()
