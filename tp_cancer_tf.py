import sklearn.preprocessing
import tensorflow as tf
import pandas


tf.random.set_seed(1)

dataframe = pandas.read_csv("data/cancer/data.csv", index_col="id")
y = dataframe.diagnosis
x = dataframe.drop("diagnosis", 1)

model = tf.keras.Sequential([
    # todo
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
  ])

model.compile(loss="binary_crossentropy", metrics=['accuracy'])
model.summary()

# Fit
# Evaluate
# Save
# Predict : cancer_tf_predict.py
# Netron view h5


