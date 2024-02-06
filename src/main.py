import sys

from PySide6.QtWidgets import QApplication

from controllers.simulator_controller import Simulator
from specx.app import simulation


def main():
    """
    Main entry point for the application. This function is called when the
    application is executed. It creates the application and the main window
    and starts the event loop.
    """
    app = QApplication(sys.argv)
    simulator = Simulator(simulation=simulation)
    simulator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
