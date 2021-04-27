from datetime import datetime
from PyQt5 import QtWidgets, QtGui

from src.charts import cartesian
from src.model import simulation
from src.qt.simulator import SimulatorTemplate
from src.tools import threads


# ---- Date formats ----
DATE_FORMAT = "%m-%d-%Y %H-%M-%S"

# ---- Components default values ----
DEFAULT_SPEED_FACTOR = 1
MAX_SPEED = 64
MIN_SPEED = 1/MAX_SPEED
INCREASE_STEP = 2
DECREASE_STEP = 2

# ---- Messages ----
SAVE_CHART_MESSAGE = 'Save chart'
SAVE_CHART_SUCCESS = 'Chart saved successfully'

# ---- Paths ----
PROJECT_PATH = '../'
ENVIRONMENTS_PATH = f'{PROJECT_PATH}/environments/'
SIMULATIONS_PATH = f'{PROJECT_PATH}/simulations/'


class Simulation(QtWidgets.QMainWindow, SimulatorTemplate):
    """
    Class used to simulate the use of TVWS according to
    the settings of the scenario
    """

    results_file_path = f'{SIMULATIONS_PATH}Simulation-{datetime.now().strftime(DATE_FORMAT)}.csv'

    def __init__(self, *args, **kwargs):
        self._environment = kwargs.get('environment', simulation.Environment())
        self._speed_factor = 1

        super(Simulation, self).__init__(*args)
        self.setup(self)

        self._simulation_thread = threads.SimulationThread(
            channels=self._environment.channels,
            simulation_charts=self.simulation_charts,
            percentage_chart=self.percentage_chart,
            delay=self.speed_factor,
            sample_time=self._environment.settings.get('sampling'),
            threshold=self._environment.settings.get('threshold'),
        )

        self._connect_button_signals()
        self._control_button_manager(play=False, pause=False, stop=False)
        self._setup_simulation_charts()

    @property
    def speed_factor(self):
        return self._speed_factor

    @speed_factor.setter
    def speed_factor(self, factor):
        self._speed_factor *= factor

    @classmethod
    def open_csvfile(cls):
        """
        Open a file instance for show the results of the current simulation
        """

        try:
            csvfile = threads.FileThread(filepath=cls.results_file_path)
            csvfile.setDaemon(True)
            csvfile.start()
        except Exception as e:
            print(f'Error opening CSV file:\n {e}')

    def _setup_simulation_charts(self):
        """

        """

        for chart, view in zip(self.simulation_charts, self.simulation_chartviews):
            chart = cartesian.CurvedChart(title='Test chart')
            chart.plot_series([0, 1, 2], [0, 1, 4])
            view.setChart(chart)

        self.percentage_chart = cartesian.PercentageBarChart(
            title='Usage %',
            categories=[frequency for frequency in simulation.FREQUENCIES],
            bars=[(i+1)*5 for i in range(9)]
        )
        self.percentage_bars_chartview.setChart(self.percentage_chart)

    def _connect_button_signals(self):
        """
        Button signal connection
        """

        self.btn_start.clicked.connect(self.start)
        self.btn_play.clicked.connect(self.resume)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_save_chart.clicked.connect(self.save_results)
        self.btn_open_csvfile.clicked.connect(self.open_csvfile)
        self.btn_increase_speed.clicked.connect(self._increase_speed)
        self.btn_decrease_speed.clicked.connect(self._decrease_speed)
        self.btn_reset_speed.clicked.connect(self._reset_speed)

    def _control_button_manager(self, start=True, play=True, pause=True, stop=True):
        """
        It allows you to control the interaction between the action
        buttons of the simulation in progress
        :param start:
        :param play:
        :param pause:
        :param stop:
        """

        self.btn_start.setEnabled(start)
        self.btn_play.setEnabled(play)
        self.btn_pause.setEnabled(pause)
        self.btn_stop.setEnabled(stop)

    def _speed_button_manager(self, increase=True, decrease=True, reset=True):
        """
        It allows you to control the interaction between the buttons to
        control the speed of the simulation in progress
        :param increase:
        :param decrease:
        :param reset:
        :return:
        """

        self.btn_increase_speed.setEnabled(increase)
        self.btn_decrease_speed.setEnabled(decrease)
        self.btn_reset_speed.setEnabled(reset)

    def _formatted_speed_label(self):
        """
        Formats the speed factor value for human understanding
        :return: Formatted speed factor value
        """

        if self._speed_factor >= 1:
            return f'X{int(self.speed_factor)}'
        else:
            return f'X1/{int(1/self.speed_factor)}'

    def _increase_speed(self):
        """

        """

        self._speed_factor *= INCREASE_STEP
        self.speed_label.setText(self._formatted_speed_label())
        self._speed_button_manager(increase=self._speed_factor != MAX_SPEED)

    def _decrease_speed(self):
        """

        """

        self._speed_factor /= DECREASE_STEP
        self.speed_label.setText(self._formatted_speed_label())
        self._speed_button_manager(decrease=self._speed_factor != MIN_SPEED)

    def _reset_speed(self):
        """

        """

        self._speed_factor = DEFAULT_SPEED_FACTOR
        self.speed_label.setText(self._formatted_speed_label())
        self._speed_button_manager()

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

    def save_results(self):
        """
        Save the results chart in one of the available formats
        """
        filepath, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            SAVE_CHART_MESSAGE,
            f'{self._environment.id}-{self._environment.timestamp}-chart',
            "JPG (*.jpg);;PNG (*.png)",
            options=QtWidgets.QFileDialog.Options()
        )

        if filepath:
            output = QtGui.QPixmap(self.percentage_bars_chartview.grab())
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

    def start(self):
        """
        Start the simulation process
        """

        try:
            self._simulation_thread.setDaemon(True)
            self._simulation_thread.start()
            self._control_button_manager(start=False, play=False)
        except Exception as e:
            print(f'Error in starting Simulation:\n {e}')

    def resume(self):
        """
        Resume the simulation process
        """

        try:
            self._simulation_thread.resume()
            self._control_button_manager(start=False, play=False)
        except Exception as e:
            print(f'Error in resuming Simulation:\n {e}')

    def pause(self):
        """
        Pause the simulation process
        """

        try:
            self._simulation_thread.pause()
            self._control_button_manager(start=False, pause=False)
        except Exception as e:
            print(f'Error in pausing Simulation:\n {e}')

    def stop(self):
        """
        Stop the simulation process
        """

        if self._simulation_thread.is_alive():
            if self._simulation_thread.paused():
                self.resume()
            try:
                self._simulation_thread.stop()
                self._control_button_manager(play=False, pause=False, stop=False)
            except Exception as e:
                print(f'Error in stopping Simulation:\n {e}')
