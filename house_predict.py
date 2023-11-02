import numpy as np
import pickle

with open("data/house/house.pickle", "rb") as f:
    model = pickle.load(f)

y_res = model.predict(np.arange(0, 200, 10).reshape(-1, 1))
print(y_res)







