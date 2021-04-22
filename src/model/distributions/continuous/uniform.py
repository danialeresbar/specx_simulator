from src.model import generators
from src.model.distributions import base

UNIFORM = 'Uniform'
DEFAULT_MINIMUM = 0.27671
DEFAULT_MAXIMUM = 0.61845


class Uniform(base.Distribution):
    """
    Class used to represent a Uniform distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('minimum', DEFAULT_MINIMUM))
        self.__scale = base.Parameter.scale(kwargs.get('maximum', DEFAULT_MAXIMUM))
        super(Uniform, self).__init__(
            category=base.CONTINUOUS,
            name=UNIFORM,
            parameters=[self.__location, self.__scale]
        )

    def generate_rv(self):
        return generators.uniform(self.parameters)
