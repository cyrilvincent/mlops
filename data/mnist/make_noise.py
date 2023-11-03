import json

import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from numpy_serializer import NumpyArrayEncoder

with np.load("mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']

x_test = x_test.astype("float32")
x_test /= 255

# Add a 4D
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# Add noise
noise_factor = 0.2
x_test_noisy = x_test + noise_factor * tf.random.normal(shape=x_test.shape)
x_test_noisy = tf.clip_by_value(x_test_noisy, clip_value_min=0., clip_value_max=1.)

n = 10

for i in range(10):
    for x, y in zip(x_test_noisy, y_test):
        if i == y:
            res = tf.squeeze(x)
            res = np.array(res) * 255
            res = res.astype(np.integer)
            with open(f"noise_{i}.json", "w") as f:
                json.dump(np.array(res), f, cls=NumpyArrayEncoder)
            break


