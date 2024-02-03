import threading
import time

from datetime import datetime, timedelta
from model import simulation


class SimulationThread(threading.Thread):
    """
    Class used for the implementation of a thread that
    will run the simulation process of random variables
    """

    def __init__(self, *args, **kwargs):
        super(SimulationThread, self).__init__(*args)

        # Simulation environment attributes
        self.channels = kwargs.get('channels', list())
        self.simulation_charts = kwargs.get('simulation_charts', list())
        self.percentage_chart = kwargs.get('percentage_chart', None)
        self.delay = kwargs.get('delay', None)
        self.energy_threshold = kwargs.get('threshold', 0.33)  # 0.33 Is the default value
        self.sample_time = kwargs.get('sample_time', 0)
        self.simulation_path = kwargs.get('filepath')

        # Thread manager attributes
        self.pause_cond = threading.Condition(threading.Lock())
        self.paused = False  # Pause indicator
        self.stop_cond = threading.Condition(threading.Lock())
        self.stopped = False  # Stop indicator
        self.finished = True  # Finished indicator

    def run(self):
        """
        Generation of Random Variables and updating of the charts
        :return:
        """

        delta = datetime.now()
        limit = simulation.RANDOM_VARIABLES_LIMIT
        for channel, chart in zip(self.channels, self.simulation_charts):
            var_count = 0

            while var_count < limit*self.sample_time and not self.stopped:
                var = channel.distribution.generate_rv()
                var_count += 1
                chart.update_series(var_count*2, var)
                time.sleep(2/self.delay())  # Time interval between the generation of random variables
                delta += timedelta(seconds=2)
                # csvhandler.write_csv(
                #     self.simulation_path,
                #     delta,
                #     channel.frequency,
                #     channel.distribution.name,
                #     var
                # )
                with self.pause_cond:
                    while self.paused:
                        self.pause_cond.wait()
            with self.stop_cond:
                if self.stopped:
                    self.finished = False
                    break

    def pause(self):
        """
        Pause the execution of the thread by setting the lock state
        of the paused condition to closed (locked)
        """

        self.paused = True
        self.pause_cond.acquire()  # Lock acquired

    def resume(self):
        """
        Resume the execution of the thread by setting the lock state
        of the paused condition to open (unlocked)
        """

        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()  # Lock released

    def stop(self):
        """
        Stop the execution of the thread by setting the lock state
        of the stopped condition to closed (locked)
        """

        self.stopped = True


class FileThread(threading.Thread):
    """
    Class that inherits from Thread to override the 'run' method
    in order to save the simulation results to file
    """

    def __init__(self, *args, **kwargs):
        self.filepath = kwargs.get('filepath')
        super(FileThread, self).__init__(*args)

    def run(self):
        """
        Open an instance of the simulation results file by subprocess
        """

        import os
        import subprocess
        path = f'{os.getcwd()}{os.path.sep}{self.filepath}'
        try:
            subprocess.call(path, shell=True)
        except OSError as e:
            print(e)
