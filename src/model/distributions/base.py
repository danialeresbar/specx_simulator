import math
import time

# ---- Random Variable bounds ----
MIN_VALUE = 0
MAX_VALUE = 0.8


# System time in seconds (s)
SEED_1 = time.time()

# System time in milliseconds (ms)
SEED_2 = time.time()*1000

DEFAULT_NAME = 'Distribution'
DISCRETE = 0
CONTINUOUS = 1

LOCATION = 'Location'
SCALE = 'Scale'


def posix_mixed_congruential_generator():
    """
    Congruential generator used by JAVA and POSIX
    """
    global SEED_1
    a = 25214903917
    m = (2**48) - 1
    SEED_1 = (a*SEED_1 + 11) % m
    return SEED_1/m


def gcc_mixed_congruential_generator():
    """
    Congruential generator used by GCC
    """
    global SEED_2
    a = 1103515245
    m = (2**31) - 1
    SEED_2 = (a*SEED_2 + 12345) % m
    return SEED_2/m


def clean_random_variable(var):
    """
    Sets an existence interval for a random variable
    :param var: Random variable following any probability distribution
    :return: The value within the set range
    """

    if var < MIN_VALUE:
        return 0
    elif var > MAX_VALUE:
        return MAX_VALUE
    else:
        return var


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

    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'parameters': [parameter.to_dict() for parameter in self.parameters]
        }

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

    def to_dict(self):
        return {
            'name': self.name,
            'vale': self.value
        }

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
