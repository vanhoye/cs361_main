import json
from pathlib import Path

ride_data_file = Path("rides.json")


def load_rides():
    if ride_data_file.exists():
        with open(ride_data_file, 'r',) as f:
            return json.load(f)
    return []


def save_rides(rides):
    with open(ride_data_file, 'w') as f:
        json.dump(rides, f, indent=2)
