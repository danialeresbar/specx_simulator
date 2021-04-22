
from datetime import datetime
from src.model.distributions import base

DATE_FORMAT = "%m-%d-%Y-%H:%M:%S"


class Channel(object):
    """
    Class to represent the behavior of a channel. It has the
    attributes required for a simulation
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 0)
        self.frequency = kwargs.get('frequency', 0)
        self.distribution = kwargs.get('distribution', base.Distribution())

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_distribution(self, distribution):
        self.distribution = distribution

    def __str__(self):
        return f'Channel: {self.id} - Frequency: {self.frequency}'


class Environment(object):
    """
    Class representing an environment for simulating the occupation of
    some channels in the UHF band
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', 'Test id')
        self.timestamp = kwargs.get('timestamp', datetime.now().strftime(DATE_FORMAT))
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

    def set_settings(self, settings):
        self.settings = settings

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

    def __str__(self):
        return f'Environment: {self.id}, at the: {self.timestamp}'
