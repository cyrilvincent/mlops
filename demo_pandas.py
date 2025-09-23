import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
dataframe["loyer_m2"] = dataframe["loyer"] / dataframe["surface"]
print(dataframe)
print(dataframe.describe())
dataframe.to_html("data/house/house.html")

plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.show()
