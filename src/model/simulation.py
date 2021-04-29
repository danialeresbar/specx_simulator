from datetime import datetime

FREQUENCIES = (
    '473',
    '479',
    '485',
    '491',
    '497',
    '503',
    '509',
    '551',
    '557'
)

DATE_FORMAT = "%m-%d-%Y-%H:%M:%S"
DEFAULT_ENERGY_FLAG_VALUE = True
DEFAULT_SAMPLE_INTERVAL_VALUE = 2
DEFAULT_THRESHOLD_VALUE = 0.33
DEFAULT_USAGE_FLAG_VALUE = True

RANDOM_VARIABLES_LIMIT = 60/2


class Channel(object):
    """
    Class to represent the behavior of a channel. It has the
    attributes required for a simulation
    """

    def __init__(self, **kwargs):
        self.number = kwargs.get('number', 0)
        self.frequency = kwargs.get('frequency', 0)
        self.distribution = kwargs.get('distribution', None)

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_distribution(self, distribution):
        self.distribution = distribution

    def to_json(self):
        return {
            'number': self.number,
            'frequency': self.frequency,
            'distribution': self.distribution.to_dict()
        }

    def __str__(self):
        return f'Channel: {self.number} - Frequency: {self.frequency}'


class Environment(object):
    """
    Class used to represent an environment for simulating the occupation
    of some channels in the UHF band
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 'Test id')
        self.timestamp = kwargs.get('timestamp', datetime.now().strftime(DATE_FORMAT))
        self.channels = list()
        self.settings = {
            'sample_interval': DEFAULT_SAMPLE_INTERVAL_VALUE,
            'threshold': DEFAULT_THRESHOLD_VALUE,
            'energy': DEFAULT_ENERGY_FLAG_VALUE,
            'usage': DEFAULT_USAGE_FLAG_VALUE
        }

    def __str__(self):
        return f'Simulation Environment: {self.id}, at the: {self.timestamp}'

    def add_or_update_channel(self, new_channel):
        """
        Add a new channel to the simulation environment. In case the
        channel already exists, update its information
        :param new_channel: New channel information
        :return: Executed action label
        """

        for channel in self.channels:
            if channel.number == new_channel.number:
                channel.frequency = new_channel.frequency
                channel.distribution = new_channel.distribution
                return 'Update'
        self.channels.append(new_channel)
        return 'Add'

    def update_settings(self, settings):
        """
        Update simulation environment settings
        :param settings: New setting values
        """

        for key, value in zip(self.settings.keys(), settings):
            self.settings.update({key: value})

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'settings': self.settings,
            'channels': [channel.to_json() for channel in self.channels]
        }
