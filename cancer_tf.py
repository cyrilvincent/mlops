import sklearn.preprocessing as pp
import sklearn.model_selection as ms
import keras
import pandas

dataframe = pandas.read_csv("data/cancer/data.csv")
y = dataframe["diagnosis"]
x = dataframe.drop(["diagnosis", "id"], axis=1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=42)

scaler = pp.StandardScaler()  # f(x) = (x - mean) - std
scaler.fit(xtrain)  # Calcul pour chaque colonne mean + std
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

model = keras.Sequential([
    keras.layers.Dense(30, input_shape=(x.shape[1],)),
    keras.layers.Dense(20, activation="relu"),
    keras.layers.Dense(10, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
  ])

model.compile(loss="binary_crossentropy", metrics=['accuracy'])
model.summary()

model.fit(xtrain, ytrain, epochs=20, validation_data=(xtest, ytest))
score = model.evaluate(xtest, ytest)
print(score)

model.save("data/cancer/cancer_tf.h5")

# Refaire tourner ce code
# cancer_tf.h5 viewer sur netron.app
# Refaire paeil sur MNIST