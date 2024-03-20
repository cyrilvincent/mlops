import pandas
import pandas as pd
import sklearn.ensemble as tree
import sklearn.svm as svm
import sklearn.neighbors as nn
import pickle
import matplotlib.pyplot as plt
import sklearn.model_selection as ms
import sklearn.metrics as metrics

dataframe = pd.read_csv("data/cancer/data.csv", index_col="id")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis"], axis=1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, test_size=0.2, train_size=0.8)

model = tree.RandomForestClassifier()
#model = svm.SVC()
#model = nn.KNeighborsClassifier()

model.fit(xtrain, ytrain) # PAs le droit de fit sur test
score = model.score(xtrain, ytrain)
print(score)
score = model.score(xtest, ytest) # Official
print(score)

path = f"data/cancer/svm-{int(score*100)}.pickle" # Save
with open(path, "wb") as f:
    pickle.dump(model, f)

y_pred = model.predict(x)
print(y_pred)

print(metrics.confusion_matrix(y, y_pred))
print(metrics.classification_report(y, y_pred))

# print(model.feature_importances_)
# plt.bar(x.columns, model.feature_importances_)
# plt.xticks(rotation=45)
# plt.show()
#
# from sklearn.tree import export_graphviz
# export_graphviz(model.estimators_[0],
#                  out_file='data/cancer/tree.dot',
#                  feature_names = x.columns,
#                  class_names = ["0", "1"],
#                  rounded = True, proportion = False,
#                  precision = 2, filled = True)

# Créer le modèle RF
# Fit
# Score
# Save
# Predire y_predict à partir
