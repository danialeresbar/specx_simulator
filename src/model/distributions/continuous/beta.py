import math

from scipy import stats as st
from src.charts.stats.beta import BetaPDF
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
        """
        Generates a random variable that has a Beta distribution
        with a success probability.
        :return: Random variable following a Beta distribution
        """

        var = st.beta.rvs(self.__alpha_shape, self.__beta_shape, self.__location, self.__scale)
        return base.clean_random_variable(var)

    def pdf_chart(self):
        return BetaPDF(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
            ''',
            alpha=self.__alpha_shape.value,
            beta=self.__beta_shape.value,
            a=self.__location.value,
            b=self.__scale.value
        )
