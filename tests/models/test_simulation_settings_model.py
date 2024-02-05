import unittest

from faker import Faker

from src.models.simulation import SimulationSettings
from constants.simulation import (
    SAMPLE_INTERVAL_MIN,
    SAMPLE_INTERVAL_MAX
)

fake = Faker()


class TestSimulationSettingsModel(unittest.TestCase):

    def setUp(self):
        self.default_sample_interval = fake.pyint(min_value=SAMPLE_INTERVAL_MIN, max_value=SAMPLE_INTERVAL_MAX)
        self.default_energy_threshold = fake.pyfloat(positive=True)
        self.valid_energy_measurement = fake.boolean()
        self.valid_occupancy_measurement = not self.valid_energy_measurement

    def test_create_simulation_settings(self):
        settings = SimulationSettings(
            sample_interval=self.default_sample_interval,
            energy_threshold=self.default_energy_threshold,
            energy_measurement=self.valid_energy_measurement,
            occupancy_measurement=self.valid_occupancy_measurement
        )
        self.assertEqual(settings.sample_interval, self.default_sample_interval)
        self.assertEqual(settings.energy_threshold, self.default_energy_threshold)
        self.assertEqual(settings.energy_measurement, self.valid_energy_measurement)
        self.assertEqual(settings.occupancy_measurement, self.valid_occupancy_measurement)

    def test_create_simulation_settings_with_invalid_sample_interval(self):
        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=fake.pyint(min_value=SAMPLE_INTERVAL_MAX + 1),
                energy_threshold=self.default_energy_threshold,
                energy_measurement=self.valid_energy_measurement,
                occupancy_measurement=self.valid_occupancy_measurement
            )

        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=fake.pyint(max_value=SAMPLE_INTERVAL_MIN - 1),
                energy_threshold=self.default_energy_threshold,
                energy_measurement=self.valid_energy_measurement,
                occupancy_measurement=self.valid_occupancy_measurement
            )

    def test_create_simulation_settings_with_invalid_energy_threshold(self):
        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=self.default_sample_interval,
                energy_threshold=fake.pyfloat(positive=False),
                energy_measurement=self.valid_energy_measurement,
                occupancy_measurement=self.valid_occupancy_measurement
            )

    def test_create_simulation_settings_with_bad_measurement_selection(self):
        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=self.default_sample_interval,
                energy_threshold=self.default_energy_threshold,
                energy_measurement=False,
                occupancy_measurement=False
            )

        with self.assertRaises(ValueError):
            SimulationSettings(
                sample_interval_minutes=self.default_sample_interval,
                energy_threshold=self.default_energy_threshold,
                energy_measurement=True,
                occupancy_measurement=True
            )
