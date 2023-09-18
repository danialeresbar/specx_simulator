import json

current_config = {}
global_config = json.load(open('./config/distributions.json', 'r'))

def get_params_count(id):
    current_dist = None
    for distribution in global_config['distributions']:
        if distribution['id'] == id:
            current_dist = distribution
            break

    return len(current_dist['parameters'])

def save_config(filepath):
    filepath = filepath if filepath.endswith('.json') else '{}{}'.format(filepath, '.json')
    json.dump(current_config, open(filepath, 'a'), indent=4)

def load_config(filepath):
    global current_config
    current_config = json.load(open(filepath, 'r'))
