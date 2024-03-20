import pandas
import pandas as pd
import sklearn.ensemble as tree

dataframe = pd.read_csv("data/cancer/data.csv", index_col="id")
y = dataframe.diagnosis
x = dataframe.drop(["diagnosis"], axis=1)

# Créer le modèle RF
# Fit
# Score
# Save
# Predire y_predict à partir
