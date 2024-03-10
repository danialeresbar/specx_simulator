import unittest

from faker import Faker

from src.constants.simulation import DECIMAL_PLACES
from src.models.distribution import DistributionParameter

fake = Faker()


class TestDistributionParameterModel(unittest.TestCase):

    def setUp(self):
        self.random_name = fake.word()
        self.default_interval = (0, 1)

    def test_create_distribution_parameter_with_default_interval(self):
        """
        Test that a distribution parameter can be created with the default interval
        and a valid value.
        """
        value = fake.pyfloat(
            right_digits=DECIMAL_PLACES,
            min_value=self.default_interval[0],
            max_value=self.default_interval[1]
        )
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
        """
        Test that a distribution parameter value can be mutated. The new value
        must be within the interval.
        """
        interval = (0, 0.5)
        valid_value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        distribution_parameter = DistributionParameter(name=fake.word(), interval=interval, value=valid_value)
        with self.assertRaises(ValueError):
            distribution_parameter.name = fake.word()

        with self.assertRaises(ValueError):
            distribution_parameter.value = fake.pyfloat(min_value=interval[1]+1)

        distribution_parameter.value = fake.pyfloat(min_value=interval[0], max_value=interval[1])
        self.assertNotEqual(distribution_parameter.value, valid_value)

    def test_distribution_parameter_immutable_name(self):
        """
        Test that a distribution parameter name is immutable.
        """
        name = fake.word()
        distribution_parameter = DistributionParameter(name=name, interval=self.default_interval, value=0)
        with self.assertRaises(ValueError):
            distribution_parameter.name = fake.word()

        self.assertEqual(distribution_parameter.name, name)

    def test_create_distribution_parameter_with_boundless_interval(self):
        """
        Test that a distribution parameter can be created with a boundless
        interval and a valid value. The interval is boundless if both lower
        and upper bounds are None.
        """
        interval = (None, None)
        value = fake.pyfloat(right_digits=DECIMAL_PLACES)
        distribution_parameter = DistributionParameter(name=self.random_name, interval=interval, value=value)
        self.assertEqual(distribution_parameter.interval, interval)
        self.assertTrue(distribution_parameter.is_boundless)
        self.assertEqual(distribution_parameter.value, value)

    def test_create_distribution_parameter_with_lower_bound_interval(self):
        """
        Test that a distribution parameter can be created with a lower bound
        interval and a valid value.
        """
        interval = (0, None)
        valid_value = fake.pyfloat(right_digits=DECIMAL_PLACES, min_value=interval[0])
        distribution_parameter = DistributionParameter(name=self.random_name, interval=interval, value=valid_value)
        self.assertEqual(distribution_parameter.interval, interval)
        self.assertFalse(distribution_parameter.is_boundless)
        self.assertEqual(distribution_parameter.value, valid_value)
        with self.assertRaises(ValueError):
            distribution_parameter.value = fake.pyfloat(max_value=interval[0]-1)

    def test_create_distribution_parameter_with_upper_bound_interval(self):
        """
        Test that a distribution parameter can be created with an upper bound
        interval and a valid value.
        """
        interval = (None, 1)
        valid_value = fake.pyfloat(right_digits=DECIMAL_PLACES, max_value=interval[1])
        distribution_parameter = DistributionParameter(name=self.random_name, interval=interval, value=valid_value)
        self.assertEqual(distribution_parameter.interval, interval)
        self.assertFalse(distribution_parameter.is_boundless)
        self.assertEqual(distribution_parameter.value, valid_value)
        with self.assertRaises(ValueError):
            distribution_parameter.value = fake.pyfloat(min_value=interval[1]+1)

    def test_create_distribution_parameter_with_invalid_interval(self):
        """
        Test that a distribution parameter cannot be created with an invalid
        interval. The lower bound must be less than the upper bound.
        """
        interval = (1, 0)
        with self.assertRaises(ValueError):
            DistributionParameter(name=self.random_name, interval=interval, value=0)
