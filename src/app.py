import sys

from PySide6.QtWidgets import QApplication

from controllers.simulator_controller import Simulator
from models.simulation import SimulationEnvironment


def main():
    app = QApplication(sys.argv)
    simulator = Simulator(SimulationEnvironment())
    simulator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
