import sys

from PySide6.QtWidgets import QApplication

from constants.simulation import ENERGY_THRESHOLD_DEFAULT, SAMPLE_INTERVAL_DEFAULT
from controllers.simulator_controller import Simulator
from models.simulation import (
    ChannelFrequency,
    SimulationEnvironment,
    SimulationMeasurement,
    SimulationSettings,
    TVChannel
)


def main():
    """
    Main entry point for the application. This function is called when the
    application is executed. It creates the application and the main window
    and starts the event loop.
    """
    simulation: SimulationEnvironment = SimulationEnvironment(
        settings=SimulationSettings(
            sample_interval=SAMPLE_INTERVAL_DEFAULT,
            energy_threshold=ENERGY_THRESHOLD_DEFAULT,
            measurement=SimulationMeasurement.ENERGY
        ),
        channels=[TVChannel(number=data.name.split('_')[1], frequency=data.value) for data in ChannelFrequency]
    )
    app = QApplication(sys.argv)
    simulator = Simulator(simulation=simulation)
    simulator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
