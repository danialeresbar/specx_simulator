from . import generators as gen
from . import json_tools
from .charts import PDFChart
from datetime import datetime


# ---- Parameter attributes ----
PRECISION = 10


# ---- Distribution types ----
DISCRETE_TYPE = 'Discrete'
CONTINUOUS_TYPE = 'Continuous'


# ---- Bernoulli Distribution ----
BERNOULLI = 'Bernoulli'
SUCCESS_PROB = 0.5


# ---- Beta Distribution ----
BETA = 'Beta'
BETA_SHAPE_1_LABEL = 'Parámetro de\nforma alpha:'
BETA_SHAPE_1 = 14.087
BETA_SHAPE_2_LABEL = 'Parámetro de\nforma beta:'
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
LOGNORM = 'Lognormal'
LOGNORM_SHAPE = 0.01758
LOGNORM_LOC = 1.86636
LOGNORM_SCALE = -5.8362


# ---- Normal Distribution ----
NORM = 'Normal'
NORM_LOC = 0.60998
NORM_SCALE = 0.06172


# ---- Rayleigh Distribution ----
RAYLEIGH = 'Rayleigh'
RAYLEIGH_LOC = 0.05
RAYLEIGH_SCALE = 0.1003


# ---- Uniform Distribution ----
UNIFORM = 'Uniforme'
UNIFORM_INF_LABEL = 'Parámetro de\ncota inferior:'
UNIFORM_INF = 0.27671
UNIFORM_SUP_LABEL = 'Parámetro de\ncota superior:'
UNIFORM_SUP = 0.61845


# ---- Weibull Distribution ----
WEIBULL = 'Weibull'
WEIBULL_SHAPE = 7.1476
WEIBULL_LOC = -0.01445
WEIBULL_SCALE = 0.58176


class Distribution(object):
    """
    Class for the generalization of a probability distribution. It has the common attributes of a
    probability distribution
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Nameless')
        self.parameters = kwargs.get('parameters', dict())
        self.kind = kwargs.get('kind', 'Typeless')
        self.rv_generator = kwargs.get('rv_generator', None)
        self.chart = PDFChart()

    def set_name(self, name):
        self.name = name

    def set_type(self, kind):
        self.kind = kind

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_rv_generator(self, rv_generator):
        self.rv_generator = rv_generator

    def build_chart(self):
        self.chart = PDFChart(
            title=f'''
                    Probability Density Function
                    <center><small>{self.name} Distribution</small></center>
                ''',
            parameters=self.parameters
        )

    def serialize_distribution(self):
        serialized_distribution = {
            'name': self.name,
            'kind': self.kind,
            'parameters': self.parameters,
        }

        return serialized_distribution

    def __str__(self):
        return f'Distribution: {self.name}, type: {self.kind}, parameters: {self.parameters}'


class Bernoulli(Distribution):
    """
    Class used to represent a Bernoulli distribution. Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Bernoulli, self).__init__(
            name=BERNOULLI,
            parameters={
                'success_probability': kwargs.get('success_probability', SUCCESS_PROB),
            },
            kind=DISCRETE_TYPE,
            rv_generator=gen.bernoulli
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_bernoulli()


class Beta(Distribution):
    """
    Class used to represent a Beta distribution (two,three or four parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Beta, self).__init__(
            name=BETA,
            parameters={
                'alpha_shape': kwargs.get('alpha_shape', BETA_SHAPE_1),
                'beta_shape': kwargs.get('beta_shape', BETA_SHAPE_2),
                'location': kwargs.get('loc', BETA_LOC),
                'scale': kwargs.get('scale', BETA_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.beta
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_beta()


class Gamma(Distribution):
    """
    Class used to represent a Gamma distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Gamma, self).__init__(
            name=GAMMA,
            parameters={
                'alpha_shape': kwargs.get('alpha', GAMMA_SHAPE),
                'location': kwargs.get('loc', GAMMA_LOC),
                'scale': kwargs.get('scale', GAMMA_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.gamma
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_gamma()


class Gumbel(Distribution):
    """
    Class used to represent a Gumbel distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Gumbel, self).__init__(
            name=GUMBEL,
            parameters={
                'location': kwargs.get('loc', GUMBEL_LOC),
                'scale': kwargs.get('scale', GUMBEL_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.gumbel
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_gumbel()


class Laplace(Distribution):
    """
    Class used to represent a Laplace distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Laplace, self).__init__(
            name=LAPLACE,
            parameters={
                'location': kwargs.get('loc', LAPLACE_LOC),
                'scale': kwargs.get('scale', LAPLACE_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.laplace
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_laplace()


class Lognorm(Distribution):
    """
    Class used to represent a Log-norm distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Lognorm, self).__init__(
            name=LOGNORM,
            parameters={
                'alpha_shape': kwargs.get('alpha_shape', LOGNORM_SHAPE),
                'location': kwargs.get('loc', LOGNORM_LOC),
                'scale': kwargs.get('scale', LOGNORM_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.lognormal
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_lognorm()


class Norm(Distribution):
    """
    Class used to represent a Norm distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Norm, self).__init__(
            name=NORM,
            parameters={
                'location': kwargs.get('loc', NORM_LOC),
                'scale': kwargs.get('scale', NORM_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.normal
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_norm()


class Rayleigh(Distribution):
    """
    Class used to represent a Rayleigh distribution (one or two parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Rayleigh, self).__init__(
            name=RAYLEIGH,
            parameters={
                'location': kwargs.get('loc', RAYLEIGH_LOC),
                'scale': kwargs.get('scale', RAYLEIGH_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.rayleigh
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_rayleigh()


class Uniform(Distribution):
    """
    Class used to represent a Uniform distribution.
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Uniform, self).__init__(
            name=UNIFORM,
            parameters={
                'lower_bound': kwargs.get('loc', UNIFORM_INF),
                'upper_bound': kwargs.get('scale', UNIFORM_SUP),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.uniform
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_uniform()


class Weibull(Distribution):
    """
    Class used to represent a Weibull distribution (two or three parameters).
    Inherits the attributes of the Distribution class
    """

    def __init__(self, **kwargs):
        super(Weibull, self).__init__(
            name=WEIBULL,
            parameters={
                'alpha_shape': kwargs.get('alpha', WEIBULL_SHAPE),
                'location': kwargs.get('loc', WEIBULL_LOC),
                'scale': kwargs.get('scale', WEIBULL_SCALE),
            },
            kind=CONTINUOUS_TYPE,
            rv_generator=gen.weibull
        )

    def plot_chart(self):
        self.build_chart()
        self.chart.plot_weibull()


DISTRIBUTION_CHOICES = {
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


def find_distribution(key):
    return DISTRIBUTION_CHOICES.get(key, Distribution())


class Channel(object):
    """
    Class to represent the behavior of a channel.
    It has the attributes required for a simulation
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.frequency = kwargs.get('frequency', 0)
        self.distribution = Distribution()

    def set_id(self, id):
        self.id = id

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_distribution(self, distribution):
        self.distribution = distribution

    def serialize_channel(self):
        serialized_channel = {
            'id': self.id,
            'frequency': self.frequency,
            'distribution': self.distribution.serialize_distribution(),
        }

        return serialized_channel

    def __str__(self):
        return f'Channel_id: {self.id}, Frequency: {self.frequency}, {self.distribution}'


class SimulationEnvironment(object):
    """
    Class
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 'Test id')
        self.timestamp = datetime.now().strftime("%m-%d-%Y-%H:%M:%S")
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
            'channels': [channel.serialize_channel() for channel in self.channels],
            'settings': self.settings,
        }
        json_tools.save(filepath, data)

    def load_settings(self, filepath):
        data = json_tools.load(filepath)
        self.id = data.get('id', None)
        self.timestamp = data.get('timestamp', datetime.now().strftime("%m-%d-%Y-%H:%M:%S"))
        self.channels = data.get('channels', dict())
        self.settings = data.get('settings', dict())

    def __str__(self):
        return f'Environment: {self.id}, at the: {self.timestamp}'


if __name__ == "__main__":
    print('Success test')
