import pandas
import pandas as pd
import sklearn.ensemble as tree
import pickle

dataframe = pd.read_csv("data/cancer/data.csv", index_col="id")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis"], axis=1)

model = tree.RandomForestClassifier()
model.fit(x, y)
score = model.score(x, y)
print(score)

path = f"data/cancer/rf-{int(score*100)}.pickle" # Save
with open(path, "wb") as f:
    pickle.dump(model, f)

y_pred = model.predict(x)
print(y_pred)

# Créer le modèle RF
# Fit
# Score
# Save
# Predire y_predict à partir
