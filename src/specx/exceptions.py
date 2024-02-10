class SimulationError(Exception):
    """Base class for exceptions in this module."""
    pass


class SimulationExperimentExportError(SimulationError):
    """
    Exception raised for errors in the SimulationExperiment export.
    """


class SimulationExperimentImportError(SimulationError):
    """
    Exception raised for errors in the SimulationExperiment import.
    """

