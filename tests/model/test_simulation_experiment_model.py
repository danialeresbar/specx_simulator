import unittest

from datetime import datetime
from faker import Faker

from src.models.simulation import (
    ChannelFrequency,
    SimulationExperiment,
    SimulationMeasurement,
    SimulationExperimentSettings,
    TVChannel
)
from src.constants.simulation import (
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX,
    ENERGY_THRESHOLD_DEFAULT
)

fake = Faker()


class TestSimulationEnvironmentModel(unittest.TestCase):

    def setUp(self):
        self.valid_settings = SimulationExperimentSettings(
            sample_interval=fake.pyint(min_value=SAMPLE_INTERVAL_MIN, max_value=SAMPLE_INTERVAL_MAX),
            energy_threshold=ENERGY_THRESHOLD_DEFAULT,
            measurement=SimulationMeasurement.ENERGY
        )

    def test_create_simulation_experiment(self):
        """
        Test that a simulation experiment can be created with valid settings
        and channels.
        """
        channels = [
            TVChannel(number=14, frequency=ChannelFrequency.CH_14),
            TVChannel(number=15, frequency=ChannelFrequency.CH_15),
            TVChannel(number=16, frequency=ChannelFrequency.CH_16),
            TVChannel(number=17, frequency=ChannelFrequency.CH_17),
            TVChannel(number=18, frequency=ChannelFrequency.CH_18),
            TVChannel(number=19, frequency=ChannelFrequency.CH_19),
            TVChannel(number=20, frequency=ChannelFrequency.CH_20),
            TVChannel(number=27, frequency=ChannelFrequency.CH_27),
            TVChannel(number=28, frequency=ChannelFrequency.CH_28)
        ]
        experiment = SimulationExperiment(settings=self.valid_settings, channels=channels)
        self.assertIsInstance(experiment.id, str)
        self.assertIsInstance(experiment.timestamp, datetime)
        self.assertEqual(experiment.settings, self.valid_settings)
        self.assertEqual(experiment.channels, channels)

    def test_create_simulation_experiment_with_no_channels(self):
        """
        Test that a simulation experiment can be created without channels.
        """
        experiment = SimulationExperiment(settings=self.valid_settings)
        self.assertIsInstance(experiment.id, str)
        self.assertIsInstance(experiment.timestamp, datetime)
        self.assertEqual(experiment.settings, self.valid_settings)
        self.assertIsNone(experiment.channels)
