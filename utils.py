import json
import os

def write_data_json(filename, data):
    with open(filename, 'w') as f:
        json.dump([item.to_dict() for item in data], f, indent=4)

def read_data_json(filename, cls):
    try:
        if not os.path.exists(filename) or os.path.getsize(filename) == 0:
            return []
        with open(filename, 'r') as f:
            data = json.load(f)
            return [cls.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error while reading {filename}: {e}")
        return []
