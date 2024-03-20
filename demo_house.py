import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe)
print(dataframe.describe())

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()