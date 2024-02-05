import unittest

from faker import Faker

from src.models.distribution import ProbabilityDistribution, ProbabilityDistributionCategory
from src.constants.distributions import (
    AVAILABLE_PROBABILITY_DISTRIBUTIONS,
    DISTRIBUTION_DESCRIPTION_DEFAULT,
    BERNOULLI,
    NORMAL
)

fake = Faker()


class TestProbabilityDistributionModel(unittest.TestCase):

    def test_create_probability_distribution(self):
        name = fake.random_element(AVAILABLE_PROBABILITY_DISTRIBUTIONS)
        category = fake.enum(ProbabilityDistributionCategory)
        distribution = ProbabilityDistribution(name=name, category=category)
        self.assertEqual(distribution.name, name)
        self.assertEqual(distribution.category, category.value)
        self.assertEqual(distribution.description, DISTRIBUTION_DESCRIPTION_DEFAULT)

    def test_create_continuous_probability_distribution(self):
        distribution = ProbabilityDistribution(name=NORMAL, category=ProbabilityDistributionCategory.CONTINUOUS)
        self.assertTrue(distribution.is_continuous)

    def test_create_discrete_probability_distribution(self):
        distribution = ProbabilityDistribution(name=BERNOULLI, category=ProbabilityDistributionCategory.DISCRETE)
        self.assertFalse(distribution.is_continuous)

    def test_probability_distribution_immutability(self):
        name = fake.random_element(AVAILABLE_PROBABILITY_DISTRIBUTIONS)
        category = fake.enum(ProbabilityDistributionCategory)
        distribution = ProbabilityDistribution(name=name, category=category)
        with self.assertRaises(ValueError):
            distribution.name = fake.word()

        with self.assertRaises(ValueError):
            distribution.category = ProbabilityDistributionCategory.CONTINUOUS

        with self.assertRaises(ValueError):
            distribution.description = fake.sentence()

        with self.assertRaises(ValueError):
            distribution.parameters = []

        self.assertEqual(distribution.name, name)
        self.assertEqual(distribution.category, category.value)
        self.assertEqual(distribution.description, DISTRIBUTION_DESCRIPTION_DEFAULT)
        self.assertEqual(distribution.parameters, [])
