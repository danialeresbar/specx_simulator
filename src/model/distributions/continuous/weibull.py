import math

from scipy import stats as st
from src.model.distributions import base

WEIBULL = 'Weibull'
ALPHA_SHAPE = 'Alpha shape'
DEFAULT_ALPHA = 7.1476
DEFAULT_LOCATION = -0.01445
DEFAULT_SCALE = 0.58176


class Weibull(base.Distribution):
    """
    Class used to represent a Weibull distribution
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
        super(Weibull, self).__init__(
            category=base.CONTINUOUS,
            name=WEIBULL,
            parameters=[self.__alpha_shape, self.__location, self.__scale]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Weibull distribution
        with a success probability.
        :return: Random variable following a Weibull distribution
        """

        var = st.weibull_min.rvs(self.__alpha_shape, self.__location, self.__scale)
        return base.clean_random_variable(var)
