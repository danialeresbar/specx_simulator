import csv
import json


def export_csv(filepath: str, data) -> None:
    """
    Export data to a CSV file.

    :param filepath: Filepath to the CSV file.
    :param data: Data to be exported.
    """
    with open(filepath, 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # Write header
        # writer.writerow(data[0].keys())
        for row in data:
            writer.writerow(row)


def export_json(filepath: str, data) -> None:
    """
    Export data to a JSON file.

    :param filepath: Filepath to the JSON file.
    :param data: Data to be exported.
    """
    with open(filepath, 'w+') as jsonfile:
        json.dump(data, jsonfile, indent=2)


def load_json(filepath: str) -> dict | list:
    """
    Load data from a JSON file.

    :param filepath: Filepath to the JSON file.
    :return: Data from the JSON file.
    """
    with open(filepath, 'r') as jsonfile:
        data = json.load(jsonfile)

    return data
