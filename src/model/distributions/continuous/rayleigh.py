from scipy import stats as st
from src.model.distributions import base

RAYLEIGH = 'Rayleigh'
DEFAULT_LOCATION = 0.05
DEFAULT_SCALE = 0.1003


class Rayeigh(base.Distribution):
    """
    Class used to represent a Rayleigh distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Rayeigh, self).__init__(
            category=base.CONTINUOUS,
            name=RAYLEIGH,
            parameters=[self.__location, self.__scale]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Rayleigh distribution
        with a success probability.
        :return: Random variable following a Rayleigh distribution
        """

        var = st.rayleigh.rvs(self.__location, self.__scale)
        return base.clean_random_variable(var)
