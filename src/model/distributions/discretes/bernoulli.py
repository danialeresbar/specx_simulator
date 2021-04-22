from src.model import generators
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
        return generators.bernoulli(self.parameters)
