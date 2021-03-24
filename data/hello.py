import json
import numpy as np
import tensorflow as tf


def convert_json_numpy():
    with open('EmployeeData.json') as json_file:
        data = json.load(json_file)
        # print(data)
    # print(np.asarray(data))
    data = np.array(data)

    data_set = tf.data.Dataset.from_tensor_slices(data)
    print(data_set)

convert_json_numpy()
