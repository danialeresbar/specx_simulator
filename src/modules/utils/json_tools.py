import json


def save(filepath, data):
    try:
        if filepath.endswith('.json'):
            with open(filepath, 'a') as outfile:
                json.dump(data, outfile, indent=4)
        else:
            filepath = f'{filepath}.json'
            with open(filepath, 'a') as outfile:
                json.dump(data, outfile, indent=4)
    except Exception as e:
        print(type(e))


def load(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(type(e))
