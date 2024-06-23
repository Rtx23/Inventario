import json
import os

def write_data_json(filename, data):
    with open(filename, 'w') as f:
        json.dump([item.to_dict() for item in data], f, indent=4)

def read_data_json(filename, cls):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [cls.from_dict(item) for item in data]
    except json.JSONDecodeError:
        return []
