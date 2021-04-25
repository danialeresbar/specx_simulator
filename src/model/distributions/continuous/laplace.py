from scipy import stats as st
from src.charts.stats.laplace import LaplacePDF
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
        """
        Generates a random variable that has a Laplace distribution
        with a success probability.
        :return: Random variable following a Laplace distribution
        """

        var = st.laplace.rvs(self.__location, self.__scale)
        return base.clean_random_variable(var)

    def pdf_chart(self):
        return LaplacePDF(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
            ''',
            location=self.__location.value,
            diversity=self.__scale.value
        )
