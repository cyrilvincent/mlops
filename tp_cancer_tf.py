import sklearn.preprocessing
import tensorflow as tf
import pandas


tf.random.set_seed(1)

dataframe = pandas.read_csv("data/cancer/data.csv", index_col="id")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis"], axis=1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(30, input_shape=(x.shape[1],)),
    tf.keras.layers.Dense(25, activation=tf.nn.relu),
    tf.keras.layers.Dense(20, activation=tf.nn.relu),
    tf.keras.layers.Dense(15, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.relu),
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)
  ])

model.compile(loss="binary_crossentropy", metrics=['accuracy'])
model.summary()

model.fit(x, y, epochs=20, validation_split=0.2)
score = model.evaluate(x, y)
model.save("data/cancer/cancer-mlp.h5")
# Predict : cancer_tf_predict.py
# Netron view h5


