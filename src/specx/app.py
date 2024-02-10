from constants.simulation import ENERGY_THRESHOLD_DEFAULT, SAMPLE_INTERVAL_DEFAULT
from models.simulation import (
    ChannelFrequency,
    SimulationExperiment,
    SimulationMeasurement,
    SimulationSettings,
    TVChannel
)

experiment: SimulationExperiment = SimulationExperiment(
    settings=SimulationSettings(
        sample_interval=SAMPLE_INTERVAL_DEFAULT,
        energy_threshold=ENERGY_THRESHOLD_DEFAULT,
        measurement=SimulationMeasurement.ENERGY
    ),
    channels=[TVChannel(number=data.name.split('_')[1], frequency=data.value) for data in ChannelFrequency]
)
