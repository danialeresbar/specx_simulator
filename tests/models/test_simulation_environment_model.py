import unittest

from datetime import datetime
from faker import Faker

from src.models.simulation import ChannelFrequency, SimulationSettings, SimulationEnvironment, TVChannel
from constants.simulation import (
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX
)

fake = Faker()


class TestSimulationEnvironmentModel(unittest.TestCase):

    def setUp(self):
        self.valid_settings = SimulationSettings(
            sample_interval=fake.pyint(min_value=SAMPLE_INTERVAL_MIN, max_value=SAMPLE_INTERVAL_MAX),
            energy_threshold=fake.pyfloat(positive=True),
            energy_measurement=True,
            occupancy_measurement=False
        )

    def test_create_simulation_environment(self):
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
        environment = SimulationEnvironment(settings=self.valid_settings, channels=channels)
        self.assertIsInstance(environment.id, str)
        self.assertIsInstance(environment.timestamp, datetime)
        self.assertEqual(environment.settings, self.valid_settings)
        self.assertEqual(environment.channels, channels)

    def test_create_simulation_environment_with_no_channels(self):
        environment = SimulationEnvironment(settings=self.valid_settings)
        self.assertIsInstance(environment.id, str)
        self.assertIsInstance(environment.timestamp, datetime)
        self.assertEqual(environment.settings, self.valid_settings)
        self.assertIsNone(environment.channels)
