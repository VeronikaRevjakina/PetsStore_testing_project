"""Files provider."""
import json


def get_json_data(file_path):
    """Get full path to json file."""
    with open(file_path + ".json") as f:
        data = json.load(f)
    return data