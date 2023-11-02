import pandas as pd
import numpy as np
import sklearn
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import pickle

print(sklearn.__version__)
df = pd.read_csv("data/house/house.csv")
print(df.describe())

model = lm.LinearRegression()
model.fit(df.surface.values.reshape(-1, 1), df.loyer)

y_pred = model.predict(np.arange(0, 400).reshape(-1, 1))
print(model.score(df.surface.values.reshape(-1, 1), df.loyer))

with open("data/house/house.pickle", "wb") as f:
    pickle.dump(model, f)

plt.scatter(df.surface, df.loyer)
plt.plot(np.arange(0, 400).reshape(-1, 1), y_pred, color="red")
plt.show()





