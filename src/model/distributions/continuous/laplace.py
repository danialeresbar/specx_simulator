from src.model import generators
from src.model.distributions import base

LAPLACE = 'Laplace'
DEFAULT_LOCATION = 0.56898
DEFAULT_SCALE = 0.11365703


class Laplace(base.Distribution):
    """
    Class used to represent a Laplace distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Laplace, self).__init__(
            category=base.CONTINUOUS,
            name=LAPLACE,
            parameters=[self.__location, self.__scale]
        )

    def generate_rv(self):
        return generators.laplace(self.parameters)
