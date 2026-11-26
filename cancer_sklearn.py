import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import sklearn.preprocessing as pp
import pickle

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/cancer/data.csv")
print(df.describe())

y = df['diagnosis']
x = df.drop(['diagnosis', "id"], axis=1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, test_size=0.2, train_size=0.8, random_state=42)

# TP
# Créer le modèle
# Apprentissage
# Score (mauvais)

scaler = pp.StandardScaler()  # f(x) = (x - mean) - std
scaler.fit(xtrain)  # Caclul pour chaque colonne mean + std
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)

# model = lm.LinearRegression()
model = rf.RandomForestClassifier()
model.fit(xtrain, ytrain)
# print(model.coef_)
# print(model.intercept_)
score = model.score(xtest, ytest)
print(score)

print(model.feature_importances_)

from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0], out_file="data/cancer/tree.dot", feature_names=x.columns, class_names=["0", "1"])

with open(f"data/cancer/cancer_rf_{score:.2f}.pkl", "wb") as f:
    pickle.dump(model, f)

plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()



