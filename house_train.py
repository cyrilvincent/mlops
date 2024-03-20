import pandas as pd
import sklearn
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import pickle

print(sklearn.__version__)
df = pd.read_csv("data/house/house.csv")
print(df.describe())

x = df.surface.values.reshape(-1, 1)
y = df.loyer

model = lm.LinearRegression() # Instancier le modèle
model.fit(x, y) # Apprentissage

y_pred = model.predict(x) # Prédiction
print(model.score(x, y)) # Scoring

with open("data/house/house.pickle", "wb") as f: # Save
    pickle.dump(model, f)

plt.scatter(df.surface, df.loyer)
plt.plot(x, y_pred, color="red")
plt.show()





