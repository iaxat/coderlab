import json
import numpy as np
import tensorflow as tf


def convert_json_numpy():
    with open('EmployeeData.json') as json_file:
        data = json.load(json_file)
        # print(data)
    print(np.asarray(data))

    data_set =

convert_json_numpy()
