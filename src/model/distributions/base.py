import math

DEFAULT_NAME = 'Distribution'
DISCRETE = 0
CONTINUOUS = 1

LOCATION = 'Location'
SCALE = 'Scale'


class Distribution:
    """
    Class used for the most generalized representation of a probability distribution
    """

    def __init__(self, **kwargs):
        self.category = kwargs.get('category', None)
        self.name = kwargs.get('name', DEFAULT_NAME)
        self.parameters = kwargs.get('parameters', list())

    def set_category(self, category):
        self.category = category

    def set_name(self, name):
        self.name = name

    def set_parameters(self, parameters):
        self.parameters = parameters

    def generate_rv(self):
        return None


class Parameter:
    """
    Class used for the most generalized representation of a probability distribution
    parameter
    """

    def __init__(self, **kwargs):
        self.interval = self._build_interval(kwargs.get('inf'), kwargs.get('sup'))
        self.name = kwargs.get('name', 'Nameless')
        self.value = kwargs.get('value', 1)

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    @classmethod
    def location(cls, value=0):
        return cls(
            name=LOCATION,
            inf=-math.inf,
            sup=math.inf,
            value=value
        )

    @classmethod
    def scale(cls, value=1):
        return cls(
            name=SCALE,
            inf=0,
            sup=math.inf,
            value=value
        )

    @staticmethod
    def _build_interval(inf=0, sup=1):
        return tuple(inf, sup)
