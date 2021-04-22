import math

from scipy import stats as st
from src.model.distributions import base

LOGNORM = 'Gamma'
ALPHA_SHAPE = 'Alpha shape'
DEFAULT_ALPHA = 0.01758
DEFAULT_LOCATION = 1.86636
DEFAULT_SCALE = -5.8362


class Gamma(base.Distribution):
    """
    Class used to represent a Lognorm distribution
    """

    def __init__(self, **kwargs):
        self.__alpha_shape = base.Parameter(
            name=ALPHA_SHAPE,
            inf=0,
            sup=math.inf,
            value=kwargs.get('alpha', DEFAULT_ALPHA)
        )
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Gamma, self).__init__(
            category=base.CONTINUOUS,
            name=LOGNORM,
            parameters=[self.__alpha_shape, self.__location, self.__scale]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Lognorm distribution
        with a success probability.
        :return: Random variable following a Lognorm distribution
        """

        var = st.lognorm.rvs(self.__alpha_shape, self.__location, math.exp(self.__scale))
        return base.clean_random_variable(var)
