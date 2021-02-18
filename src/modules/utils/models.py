from . import generators as gen
from . import json_tools
from datetime import datetime


# ---- Distribution types ----
DISCRETE_TYPE = 'Discrete'
CONTINUOUS_TYPE = 'Continuous'


# ---- Bernoulli Distribution ----
BERNOULLI = 'Bernoulli'
SUCCESS_PROB = 0.8


# ---- Beta Distribution ----
BETA = 'Beta'
BETA_SHAPE_1 = 14.087
BETA_SHAPE_2 = 4.9149
BETA_LOC = 0.05
BETA_SCALE = 0.75


# ---- Gamma Distribution ----
GAMMA = 'Gamma'
GAMMA_SHAPE = 7.0259
GAMMA_LOC = 0
GAMMA_SCALE = 0.02008


# ---- Gumbel Distribution ----
GUMBEL = 'Gumbel max'
GUMBEL_LOC = 0.59583
GUMBEL_SCALE = 0.04929


# ---- Laplace Distribution ----
LAPLACE = 'Laplace'
LAPLACE_LOC = 0.56898
LAPLACE_SCALE = 0.11365703


# ---- Lognormal Distribution ----
LOGNORM = 'Lognorm'
LOGNORM_SHAPE = 0.01758
LOGNORM_LOC = 1.86636
LOGNORM_SCALE = -5.8362


# ---- Normal Distribution ----
NORM = 'Norm'
NORM_LOC = 0.60998
NORM_SCALE = 0.06172


# ---- Rayleigh Distribution ----
RAYLEIGH = 'Rayleigh'
RAYLEIGH_LOC = 0.05
RAYLEIGH_SCALE = 0.1003


# ---- Uniform Distribution ----
UNIFORM = 'Uniform'
UNIFORM_INF = 0.27671
UNIFORM_SUP = 0.61845


# ---- Weibull Distribution ----
WEIBULL = 'Weibull'
WEIBULL_SHAPE = 7.1476
WEIBULL_LOC = -0.01445
WEIBULL_SCALE = 0.58176


class Parameter(object):

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Nameless')
        self.range = kwargs.get('range', list())
        self.value = kwargs.get('value', 1)

    def set_name(self, name):
        self.name = name

    def set_range(self, range):
        self.range = range

    def set_value(self, value):
        self.value = value

    @classmethod
    def location(cls, range, value):
        return cls(
            name='Location',
            range=range,
            value=value
        )

    @classmethod
    def scale(cls, range, value):
        return cls(
            name='Scale',
            range=range,
            value=value
        )


class Distribution:
    """
    Class for the generalization of a probability distribution. It has the common attributes of a
    probability distribution
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Nameless')
        self.parameters = kwargs.get('parameters', list())
        self.category = kwargs.get('category', None)
        self.variant = kwargs.get('variant', False)
        self.rv_generator = kwargs.get('rv_generator', None)

    def set_name(self, name):
        self.name = name

    def set_type(self, category):
        self.category = category

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_rv_generator(self, rv_generator):
        self.rv_generator = rv_generator

    def generate_random_variable(self):
        return self.rv_generator([parameter.value for parameter in self.parameters])

    def distribution_as_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'parameters': {parameter.name: parameter.value for parameter in self.parameters},
        }

    def __str__(self):
        return f'Distribution: {self.name}, type: {self.category} \nparameters: {self.parameters}'


class Bernoulli(Distribution):
    """
    Class used to represent a Bernoulli distribution. Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Bernoulli, self).__init__(
            name=BERNOULLI,
            parameters=[
                Parameter(
                    name='Success probability',
                    range=[0.0, 1.0],
                    value=kwargs.get('success_probability', SUCCESS_PROB)
                )
            ],
            category=DISCRETE_TYPE,
            rv_generator=gen.bernoulli
        )


class Beta(Distribution):
    """
    Class used to represent a Beta distribution (two,three or four parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Beta, self).__init__(
            name=BETA,
            parameters=[
                Parameter(name='Alpha shape', range=[0.15, 9999], value=kwargs.get('alpha_shape', BETA_SHAPE_1)),
                Parameter(name='Beta shape', range=[0.15, 9999], value=kwargs.get('beta_shape', BETA_SHAPE_2)),
                Parameter.location(range=[-9999, 9999], value=kwargs.get('loc', BETA_LOC)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', BETA_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            rv_generator=gen.beta
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_beta()


class Gamma(Distribution):
    """
    Class used to represent a Gamma distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Gamma, self).__init__(
            name=GAMMA,
            parameters=[
                Parameter(name='Alpha shape', range=[0.0001, 9999], value=kwargs.get('alpha_shape', GAMMA_SHAPE)),
                Parameter.location(range=[-9999, 9999], value=kwargs.get('loc', GAMMA_LOC)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', GAMMA_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            variant=True,
            rv_generator=gen.gamma
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_gamma()


class Gumbel(Distribution):
    """
    Class used to represent a Gumbel distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Gumbel, self).__init__(
            name=GUMBEL,
            parameters=[
                Parameter.location(range=[0, 9999], value=kwargs.get('loc', GUMBEL_LOC)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', GUMBEL_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            rv_generator=gen.gumbel
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_gumbel()


class Laplace(Distribution):
    """
    Class used to represent a Laplace distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Laplace, self).__init__(
            name=LAPLACE,
            parameters=[
                Parameter.location(range=[0, 9999], value=kwargs.get('loc', LAPLACE_LOC)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', LAPLACE_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            rv_generator=gen.laplace
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_laplace()


class Lognorm(Distribution):
    """
    Class used to represent a Log-norm distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Lognorm, self).__init__(
            name=LOGNORM,
            parameters=[
                Parameter.location(range=[-9999, 9999], value=kwargs.get('loc', LOGNORM_LOC)),
                Parameter(name='Alpha shape', range=[0.0001, 9999], value=kwargs.get('alpha_shape', LOGNORM_SHAPE)),
                Parameter.scale(range=[-9999, 9999], value=kwargs.get('scale', LOGNORM_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            variant=True,
            rv_generator=gen.lognormal
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_lognorm()


class Norm(Distribution):
    """
    Class used to represent a Norm distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Norm, self).__init__(
            name=NORM,
            parameters=[
                Parameter.location(range=[0, 9999], value=kwargs.get('loc', NORM_LOC)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', NORM_SCALE))
            ],
            category=CONTINUOUS_TYPE,
            rv_generator=gen.normal
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_norm()


class Rayleigh(Distribution):
    """
    Class used to represent a Rayleigh distribution (one or two parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Rayleigh, self).__init__(
            name=RAYLEIGH,
            parameters=[
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', RAYLEIGH_SCALE)),
                Parameter.location(range=[0, 9999], value=kwargs.get('loc', RAYLEIGH_LOC)),
            ],
            category=CONTINUOUS_TYPE,
            variant=True,
            rv_generator=gen.rayleigh
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_rayleigh()


class Uniform(Distribution):
    """
    Class used to represent a Uniform distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Uniform, self).__init__(
            name=UNIFORM,
            parameters=[
                Parameter(name='Lower bound', range=[0, 9999], value=kwargs.get('loc', UNIFORM_INF)),
                Parameter(name='Upper bound', range=[0, 9999], value=kwargs.get('scale', UNIFORM_SUP))
            ],
            category=CONTINUOUS_TYPE,
            rv_generator=gen.uniform
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_uniform()


class Weibull(Distribution):
    """
    Class used to represent a Weibull distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Weibull, self).__init__(
            name=WEIBULL,
            parameters=[
                Parameter(name='Alpha shape', range=[0.0001, 9999], value=kwargs.get('alpha_shape', WEIBULL_SHAPE)),
                Parameter.scale(range=[0.0001, 9999], value=kwargs.get('scale', WEIBULL_SCALE)),
                Parameter.location(range=[-9999, 9999], value=kwargs.get('loc', WEIBULL_LOC))
            ],
            category=CONTINUOUS_TYPE,
            variant=True,
            rv_generator=gen.weibull
        )

    @staticmethod
    def plot_pdfchart(pdfchart):
        pdfchart.plot_weibull()


class Channel(object):
    """
    Class to represent the behavior of a channel.
    It has the attributes required for a simulation
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.frequency = kwargs.get('frequency', 0)
        self.distribution = kwargs.get('distribution', Distribution())

    def set_id(self, id):
        self.id = id

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_distribution(self, distribution):
        self.distribution = distribution

    def channel_as_dict(self):
        return {
            'id': self.id,
            'frequency': self.frequency,
            'distribution': self.distribution.distribution_as_dict(),
        }

    def __str__(self):
        return f'Channel_id: {self.id}, Frequency: {self.frequency}, {self.distribution}'


class SimulationEnvironment(object):
    """
    Class representing an environment for simulating the occupation of some channels in the UHF band
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 'Test id')
        self.timestamp = kwargs.get('timestamp', datetime.now().strftime("%m-%d-%Y-%H:%M:%S"))
        self.channels = list()
        self.settings = dict()
        self.results = list()

    def add_or_update_channel(self, new_channel):
        for channel in self.channels:
            if channel.id == new_channel.id:
                channel.frequency = new_channel.frequency
                channel.distribution = new_channel.distribution
                return
        self.channels.append(new_channel)

    def set_id(self, id):
        self.id = id

    def set_settings(self, settings):
        self.settings = settings

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def save_as_json(self, filepath):
        data = {
            'id': self.id,
            'timestamp': self.timestamp,
            'channels': [channel.channel_as_dict() for channel in self.channels],
            'settings': self.settings,
        }
        json_tools.save(filepath, data)

    def load_data(self, filepath):
        data = json_tools.load(filepath)
        try:
            self.set_id(data.get('id', None))
            self.set_timestamp(data.get('timestamp', datetime.now().strftime("%m-%d-%Y-%H:%M:%S")))
            self.set_settings(data.get('settings', dict()))
            self.build_channels(data.get('channels', list()))
            return True
        except Exception as e:
            print(e)
            return False

    def build_channels(self, channels):
        for channel in channels:
            distribution_data = channel.get('distribution')
            new_channel = Channel(
                id=channel.get('id'),
                frequency=channel.get('frequency'),
                distribution=self.build_distribution(
                    distribution_data.get('name'),
                    distribution_data.get('parameters')
                )
            )
            self.add_or_update_channel(new_channel)

    @staticmethod
    def build_distribution(name, parameters):
        distribution = distribution_selector(name)
        for parameter, value in zip(distribution.parameters, parameters.values()):
            parameter.set_value(value)
        return distribution

    def __str__(self):
        return f'Environment: {self.id}, at the: {self.timestamp} channels: \n{self.channels}'


def distribution_selector(key):
    choices = {
        BERNOULLI: Bernoulli,
        BETA: Beta,
        GAMMA: Gamma,
        GUMBEL: Gumbel,
        LAPLACE: Laplace,
        LOGNORM: Lognorm,
        NORM: Norm,
        RAYLEIGH: Rayleigh,
        UNIFORM: Uniform,
        WEIBULL: Weibull,
    }
    distribution = choices.get(key, Distribution)
    return distribution()
