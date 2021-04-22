from src.model import generators
from src.model.distributions import base

NORMAL = 'Normal'
DEFAULT_LOCATION = 0.60998
DEFAULT_SCALE = 0.06172


class Normal(base.Distribution):
    """
    Class used to represent a Normal distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Normal, self).__init__(
            category=base.CONTINUOUS,
            name=NORMAL,
            parameters=[self.__location, self.__scale]
        )

    def generate_rv(self):
        return generators.normal(self.parameters)
