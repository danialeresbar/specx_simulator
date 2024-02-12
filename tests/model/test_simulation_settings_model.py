import unittest

from faker import Faker

from src.models.simulation import SimulationMeasurement, SimulationSettings
from src.constants.simulation import (
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX
)

fake = Faker()


class TestSimulationSettingsModel(unittest.TestCase):

    def setUp(self):
        self.default_sample_interval = fake.pyint(min_value=SAMPLE_INTERVAL_MIN, max_value=SAMPLE_INTERVAL_MAX)
        self.default_energy_threshold = fake.pyfloat(positive=True)
        self.default_measurement = SimulationMeasurement.ENERGY

    def test_create_simulation_settings(self):
        """
        Test that a simulation settings can be created with valid sample
        interval, energy threshold, and measurement.
        """
        settings = SimulationSettings(
            sample_interval=self.default_sample_interval,
            energy_threshold=self.default_energy_threshold,
            measurement=self.default_measurement
        )
        self.assertEqual(settings.sample_interval, self.default_sample_interval)
        self.assertEqual(settings.energy_threshold, self.default_energy_threshold)
        self.assertEqual(settings.measurement, self.default_measurement.value)

    def test_create_simulation_settings_with_invalid_sample_interval(self):
        """
        Test that a simulation settings cannot be created with an invalid
        sample interval.
        """
        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=fake.pyint(min_value=SAMPLE_INTERVAL_MAX + 1),
                energy_threshold=self.default_energy_threshold,
                measurement=self.default_measurement
            )

        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=fake.pyint(max_value=SAMPLE_INTERVAL_MIN - 1),
                energy_threshold=self.default_energy_threshold,
                measurement=self.default_measurement
            )

    def test_create_simulation_settings_with_invalid_energy_threshold(self):
        """
        Test that a simulation settings cannot be created with an invalid
        energy threshold.
        """
        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=self.default_sample_interval,
                energy_threshold=fake.pyfloat(positive=False),
                measurement=self.default_measurement
            )
