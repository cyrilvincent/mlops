import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/house/house.csv")
print(df.head(5))
print(df.describe())

plt.subplot(2, 1, 1)
plt.title('House Price')
plt.scatter(df["surface"], df["loyer"])
plt.subplot(2, 1, 2)
plt.title('House Distribution')
plt.hist(df["loyer"], bins=30)
plt.show()


