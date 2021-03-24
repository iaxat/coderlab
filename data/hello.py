import json
import numpy as np


def convert_json_numpy():
    with open('result.json') as f:
        data = json.load(f)
    print(data)
    return np.asarray(data)
