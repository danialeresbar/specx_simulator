from datetime import datetime
from src.model.distributions import base

DATE_FORMAT = "%m-%d-%Y-%H:%M:%S"
DEFAULT_ENERGY_FLAG_VALUE = True
DEFAULT_SAMPLE_INTERVAL_VALUE = 2
DEFAULT_THRESHOLD_VALUE = 0.33
DEFAULT_USAGE_FLAG_VALUE = True


class Channel(object):
    """
    Class to represent the behavior of a channel. It has the
    attributes required for a simulation
    """

    def __init__(self, **kwargs):
        self.number = kwargs.get('number', 0)
        self.frequency = kwargs.get('frequency', 0)
        self.distribution = kwargs.get('distribution', base.Distribution())

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
            'threshold': DEFAULT_THRESHOLD_VALUE,
            'sample_interval': DEFAULT_SAMPLE_INTERVAL_VALUE,
            'energy': DEFAULT_ENERGY_FLAG_VALUE,
            'usage': DEFAULT_USAGE_FLAG_VALUE
        }

    def add_or_update_channel(self, new_channel):
        """
        Add a new channel to the simulation environment. In case the
        channel already exists, update its information
        :param new_channel: New channel information
        :return: Executed action label
        """

        for channel in self.channels:
            if channel.id == new_channel.id:
                channel.frequency = new_channel.frequency
                channel.distribution = new_channel.distribution
                return 'Update'
        self.channels.append(new_channel)
        return 'Add'

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'settings': self.settings,
            'channels': [channel.to_json() for channel in self.channels]
        }

    def __str__(self):
        return f'Simulation Environment: {self.id}, at the: {self.timestamp}'

    # def save_as_json(self, filepath):
    #     data = {
    #         'id': self.id,
    #         'timestamp': self.timestamp,
    #         'channels': [channel.channel_as_dict() for channel in self.channels],
    #         'settings': self.settings,
    #     }
    #     json_tools.save(filepath, data)

    # def load_data(self, filepath):
    #     data = json_tools.load(filepath)
    #     try:
    #         self.set_id(data.get('id', None))
    #         self.set_timestamp(data.get('timestamp', datetime.now().strftime("%m-%d-%Y-%H:%M:%S")))
    #         self.set_settings(data.get('settings', dict()))
    #         self.build_channels(data.get('channels', list()))
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False

    # def build_channels(self, channels):
    #     for channel in channels:
    #         distribution_data = channel.get('distribution')
    #         new_channel = Channel(
    #             id=channel.get('id'),
    #             frequency=channel.get('frequency'),
    #             distribution=self.build_distribution(
    #                 distribution_data.get('name'),
    #                 distribution_data.get('parameters')
    #             )
    #         )
    #         self.add_or_update_channel(new_channel)

    # @staticmethod
    # def build_distribution(name, parameters):
    #     distribution = distribution_selector(name)
    #     for parameter, value in zip(distribution.parameters, parameters.values()):
    #         parameter.set_value(value)
    #     return distribution
