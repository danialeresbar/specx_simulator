from scipy import stats as st
from src.charts.stats.rayleigh import RayleighPDF
from src.model.distributions import base

RAYLEIGH = 'Rayleigh'
DEFAULT_LOCATION = 0.05
DEFAULT_SCALE = 0.1003


class Rayleigh(base.Distribution):
    """
    Class used to represent a Rayleigh distribution
    """

    def __init__(self, **kwargs):
        self.__location = base.Parameter.location(kwargs.get('location', DEFAULT_LOCATION))
        self.__scale = base.Parameter.scale(kwargs.get('scale', DEFAULT_SCALE))
        super(Rayleigh, self).__init__(
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

        var = st.rayleigh.rvs(self.__location.value, self.__scale.value)
        return base.clean_random_variable(var)

    def pdf_chart(self):
        return RayleighPDF(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
            ''',
            location=self.__location.value,
            scale=self.__scale.value
        )
