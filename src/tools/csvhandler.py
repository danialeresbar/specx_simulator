DATE_FORMAT = "%m-%d-%Y-%H:%M:%S"


def write_csv(filepath, timestamp, frequency, distribution, value):
    """

    :param filepath:
    :param timestamp:
    :param frequency:
    :param distribution:
    :param value:
    """

    newline = "{};{};{};{}".format(
        timestamp.strftime(DATE_FORMAT),
        frequency,
        distribution,
        value
    )
    with open(filepath, 'a') as csvfile:
        csvfile.write(newline + '\n')
