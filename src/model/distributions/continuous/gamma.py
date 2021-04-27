import math

from scipy import stats as st
from src.charts.stats.gamma import GammaPDF
from src.model.distributions import base

GAMMA = 'Gamma'
ALPHA_SHAPE = 'Alpha shape'
DEFAULT_ALPHA = 7.0259
DEFAULT_LOCATION = 0
DEFAULT_SCALE = 0.02008


class Gamma(base.Distribution):
    """
    Class used to represent a Gamma distribution
    """

    def __init__(self, **kwargs):
        self.__alpha_shape = base.Parameter(
            name=ALPHA_SHAPE,
            inf=0.45,
            sup=math.inf,
            value=kwargs.get('alpha', DEFAULT_ALPHA)
        )
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Gamma, self).__init__(
            category=base.CONTINUOUS,
            name=GAMMA,
            parameters=[self.__alpha_shape, self.__location, self.__scale]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Gamma distribution
        with a success probability.
        :return: Random variable following a Gamma distribution
        """

        var = st.gamma.rvs(self.__alpha_shape, self.__location, self.__scale)
        return base.clean_random_variable(var)

    def pdf_chart(self):
        return GammaPDF(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
            ''',
            alpha=self.__alpha_shape.value,
            gamma=self.__location.value,
            lambd=self.__scale.value
        )
