from src.model import generators
from src.model.distributions import base

GUMBEL = 'Gumbel'
DEFAULT_LOCATION = 0.59583
DEFAULT_SCALE = 0.04929


class Gumbel(base.Distribution):
    """
    Class used to represent a Gumbel distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Gumbel, self).__init__(
            category=base.CONTINUOUS,
            name=GUMBEL,
            parameters=[self.__location, self.__scale]
        )

    def generate_rv(self):
        return generators.gumbel(self.parameters)
