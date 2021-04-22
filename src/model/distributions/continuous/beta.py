import math

from src.model import generators
from src.model.distributions import base

BETA = 'Beta'
ALPHA_SHAPE = 'Alpha shape'
DEFAULT_ALPHA = 14.087
BETA_SHAPE = 'Beta shape'
DEFAULT_BETA = 4.9149
DEFAULT_LOCATION = 0.05
DEFAULT_SCALE = 0.75


class Beta(base.Distribution):
    """
    Class used to represent a Beta distribution
    """

    def __init__(self, **kwargs):
        self.__alpha_shape = base.Parameter(
            name=ALPHA_SHAPE,
            inf=0.5,
            sup=math.inf,
            value=kwargs.get('alpha', DEFAULT_ALPHA)
        )
        self.__beta_shape = base.Parameter(
            name=BETA_SHAPE,
            inf=0.5,
            sup=math.inf,
            value=kwargs.get('beta', DEFAULT_BETA)
        )
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Beta, self).__init__(
            category=base.CONTINUOUS,
            name=BETA,
            parameters=[self.__alpha_shape, self.__beta_shape, self.__location, self.__scale]
        )

    def generate_rv(self):
        return generators.beta(self.parameters)
