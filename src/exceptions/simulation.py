class SimulationError(Exception):
    """Base class for exceptions in this module."""
    pass


class SimulationEnvironmentExportError(SimulationError):
    """
    Exception raised for errors in the SimulationEnvironment export.
    """


class SimulationEnvironmentImportError(SimulationError):
    """
    Exception raised for errors in the SimulationEnvironment import.
    """

