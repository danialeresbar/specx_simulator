import unittest

from faker import Faker

from src.models.distribution import DistributionParameter

fake = Faker()


class TestDistributionParameterModel(unittest.TestCase):

    def setUp(self):
        self.random_name = fake.word()
        self.default_interval = (0, 1)

    def test_create_distribution_parameter_with_default_interval(self):
        value = fake.pyfloat(min_value=self.default_interval[0], max_value=self.default_interval[1])
        distribution_parameter = DistributionParameter(
            name=self.random_name,
            interval=self.default_interval,
            value=value
        )
        self.assertEqual(distribution_parameter.name, self.random_name)
        self.assertEqual(distribution_parameter.interval, self.default_interval)
        self.assertFalse(distribution_parameter.is_boundless)
        self.assertEqual(distribution_parameter.value, value)

    def test_mutate_distribution_parameter_value(self):
        interval = (0, 0.5)
        value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        distribution_parameter = DistributionParameter(name=fake.word(), interval=interval, value=value)
        with self.assertRaises(ValueError):
            distribution_parameter.name = fake.word()

        with self.assertRaises(ValueError):
            distribution_parameter.value = fake.pyfloat(min_value=interval[1]+1)

        distribution_parameter.value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        self.assertNotEqual(distribution_parameter.value, value)

    def test_create_distribution_parameter_with_boundless_interval(self):
        interval = (None, None)
        value = fake.pyfloat()
        distribution_parameter = DistributionParameter(name=self.random_name, interval=interval, value=value)
        self.assertEqual(distribution_parameter.name, self.random_name)
        self.assertEqual(distribution_parameter.interval, interval)
        self.assertTrue(distribution_parameter.is_boundless)
        self.assertEqual(distribution_parameter.value, value)
