from src.model.distributions import base

BERNOULLI = 'Bernoulli'
SUCCESS_PROBABILITY = 'Success probability'
DEFAULT_SUCCESS = 0.5


class Bernoulli(base.Distribution):
    """
    Class used to represent a Bernoulli distribution.
    """

    def __init__(self, **kwargs):
        self.__success_probability = base.Parameter(
            name=SUCCESS_PROBABILITY,
            value=kwargs.get('success', DEFAULT_SUCCESS),
            inf=0,
            sup=1
        )
        super(Bernoulli, self).__init__(
            category=base.DISCRETE,
            name=BERNOULLI,
            parameters=[self.__success_probability]
        )

    def generate_rv(self):
        """
        Generates a random variable that has a Bernoulli distribution
        with a success probability. The inverse transformation method
        is used
        :return: Random variable following a Bernoulli distribution
        """

        u = base.posix_mixed_congruential_generator()
        return 1 if u < self.__success_probability else 0
