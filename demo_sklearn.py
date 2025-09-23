import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sklearn.linear_model as lm
import numpy as np

print(sklearn.__version__)
#0 Load data
dataframe = pd.read_csv("data/house/house.csv")

#1 Create dataset
y = dataframe["loyer"]
x = dataframe["surface"].values.reshape(-1, 1)

#2#3

# 4 Create model
model = lm.LinearRegression()
# f(x) = ax + b, a = slope, b = interception, a et b sont des poids

# 5 Fit = Apprentisage
model.fit(x, y)

# 6 Prédiction
xnew = np.arange(400).reshape(-1, 1)
ypredicted = model.predict(xnew)

# 7 Score - Metrics
score = model.score(x, y)
print(score)

# 8 Save

plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.plot(xnew, ypredicted, color="red")
plt.show()
