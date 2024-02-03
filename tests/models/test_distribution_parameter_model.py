import unittest

from faker import Faker

from src.models.distributions import DistributionParameter

fake = Faker()


class TestDistributionParameterModel(unittest.TestCase):

    def test_create_distribution_parameter_with_default_interval(self):
        name = fake.word()
        interval = (0, 1)
        value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        distribution_parameter = DistributionParameter(name=name, interval=interval, value=value)
        self.assertEqual(distribution_parameter.name, name)
        self.assertEqual(distribution_parameter.interval, interval)
        self.assertEqual(distribution_parameter.value, value)

    def test_mutate_distribution_parameter(self):
        interval = (0, 0.5)
        value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        distribution_parameter = DistributionParameter(
            name=fake.word(),
            interval=interval,
            value=value
        )
        with self.assertRaises(ValueError):
            distribution_parameter.name = fake.word()

        with self.assertRaises(ValueError):
            distribution_parameter.value = fake.pyfloat(min_value=interval[1]+1)

        distribution_parameter.value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        self.assertNotEqual(distribution_parameter.value, value)
