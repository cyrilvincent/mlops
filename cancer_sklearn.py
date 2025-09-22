import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sklearn.linear_model as lm
import numpy as np
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import pickle

print(sklearn.__version__)
#0 Load data
dataframe = pd.read_csv("data/cancer/data.csv")

#1 Create dataset
y = dataframe["diagnosis"]
x = dataframe.drop(["diagnosis", "id"], axis=1)

#2 Train test split
# Training set, testing set
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

# 4 Create model
# model = lm.LinearRegression()
# f(x) = ax + b, a = slope, b = interception, a et b sont des poids
model = rf.RandomForestClassifier()

# 5 Fit = Apprentisage
model.fit(xtrain, ytrain)

# 6 Score - Metrics
score = model.score(xtest, ytest)
print(score) # Accuracy = nb good prediction / nb prediction totale

# 7 Save
with open(f"data/cancer/cancer-rf-{score:.2f}.pickle", "wb") as f:
    pickle.dump(model, f)





from sklearn.tree import export_graphviz
export_graphviz(model.estimators_[0], out_file="data/cancer/tree.dot", feature_names=x.columns, class_names=["0", "1"])
plt.bar(x.columns, model.feature_importances_)
plt.xticks(rotation=45)
plt.show()