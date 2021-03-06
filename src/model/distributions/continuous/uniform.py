from src.charts.stats.uniform import UniformPDF
from src.model.distributions import base

UNIFORM = 'Uniform'
DEFAULT_MINIMUM = 0.27671
DEFAULT_MAXIMUM = 0.61845


class Uniform(base.Distribution):
    """
    Class used to represent a Uniform distribution
    """

    def __init__(self, **kwargs):
        self.__minimum = base.Parameter.location(kwargs.get('minimum', DEFAULT_MINIMUM))
        self.__maximum = base.Parameter.scale(kwargs.get('maximum', DEFAULT_MAXIMUM))
        super(Uniform, self).__init__(
            category=base.CONTINUOUS,
            name=UNIFORM,
            parameters=[self.__minimum, self.__maximum]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Uniform distribution
        with a success probability. The inverse transformation method
        is used
        :return: Random variable following a Uniform distribution
        """

        u = base.gcc_mixed_congruential_generator()
        var = self.__minimum.value + (self.__maximum.value-self.__minimum.value)*u
        return base.clean_random_variable(var)

    def pdf_chart(self):
        return UniformPDF(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
            ''',
            lower=self.__minimum.value,
            upper=self.__maximum.value
        )
