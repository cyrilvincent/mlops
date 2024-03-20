import pandas
import pandas as pd
import sklearn.ensemble as tree
import pickle
import matplotlib.pyplot as plt

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

print(model.feature_importances_)
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()

from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0],
                 out_file='data/cancer/tree.dot',
                 feature_names = x.columns,
                 class_names = ["0", "1"],
                 rounded = True, proportion = False,
                 precision = 2, filled = True)

# Créer le modèle RF
# Fit
# Score
# Save
# Predire y_predict à partir
