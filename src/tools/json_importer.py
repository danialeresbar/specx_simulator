import json


def load(filepath):
    """
    It allows you to load the information of a simulation scenario
    contained in a file with JSON format
    :param filepath: The path of the file to upload
    :return: The information contained in the uploaded file
    """

    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)
