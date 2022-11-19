import pandas as pd

data = pd.read_csv("TEST.csv")
print(data["sentence1"].iloc[0])
