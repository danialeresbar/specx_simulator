import json


def save(filepath, data):
    """
    It allows saving the information of a simulation environment in a
    file with JSON format
    :param filepath: The path of the file to save
    :param data: The simulation environment information that will be saved
    """

    try:
        if filepath.endswith('.json'):
            with open(filepath, 'a') as outfile:
                json.dump(data, outfile, indent=4)
        else:
            filepath = f'{filepath}.json'
            with open(filepath, 'a') as outfile:
                json.dump(data, outfile, indent=4)
    except Exception as e:
        print(e)
