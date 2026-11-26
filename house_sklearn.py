import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/house/house.csv")

y = df["loyer"]
x = df["surface"].values.reshape(-1, 1)

model = lm.LinearRegression()
model.fit(x, y)

score = model.score(x, y)
print(score)
print(model.coef_, model.intercept_)  # f(x) = 40.97*x - 283

xpred = np.arange(400).reshape(-1, 1)
ypred = model.predict(xpred)

plt.title('House Price')
plt.scatter(df["surface"], df["loyer"], label="Loyer")
plt.plot(xpred, ypred, color='red', label="Predicted Loyer")
plt.legend()
plt.show()




