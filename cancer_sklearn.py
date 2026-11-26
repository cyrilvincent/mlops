import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/cancer/data.csv")
print(df.describe())

y = df['diagnosis']
x = df.drop(['diagnosis', "id"], axis=1)

# TP
# Créer le modèle
# Apprentissage
# Score (mauvais)

model = lm.LinearRegression()
model.fit(x, y)
print(model.coef_)
print(model.intercept_)
print(model.score(x, y))

