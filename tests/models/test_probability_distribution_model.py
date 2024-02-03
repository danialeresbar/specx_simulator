import unittest

from faker import Faker

from src.models.distributions import ProbabilityDistribution, ProbabilityDistributionCategory
from src.constants.distributions import AVAILABLE_PROBABILITY_DISTRIBUTIONS, DISTRIBUTION_DESCRIPTION_DEFAULT

fake = Faker()


class TestProbabilityDistributionModel(unittest.TestCase):

    def test_create_probability_distribution(self):
        name = fake.random_element(AVAILABLE_PROBABILITY_DISTRIBUTIONS)
        category = fake.enum(ProbabilityDistributionCategory)
        distribution = ProbabilityDistribution(name=name, category=category)
        self.assertEqual(distribution.name, name)
        self.assertEqual(distribution.category, category.value)
        self.assertNotEqual(distribution.description, DISTRIBUTION_DESCRIPTION_DEFAULT)

    def test_mutate_probability_distribution(self):
        name = fake.random_element(AVAILABLE_PROBABILITY_DISTRIBUTIONS)
        category = fake.enum(ProbabilityDistributionCategory)
        distribution = ProbabilityDistribution(name=name, category=category)
        with self.assertRaises(ValueError):
            distribution.name = fake.word()

        with self.assertRaises(ValueError):
            distribution.category = ProbabilityDistributionCategory.CONTINUOUS

        self.assertEqual(distribution.name, name)
        self.assertEqual(distribution.category, category.value)
