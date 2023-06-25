import pandas as pd
import numpy as np

df = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/finalDataCombined.csv")

df.sort_values(by=["Total Underground"], inplace=True, ascending=False)

# print(df["Total Underground"].sum())
# roundedDf = df.copy()

# roundedDf["Total Underground"] = df["Total Underground"].astype("int32")

# print(roundedDf["Total Underground"].sum())
# print(roundedDf.head())

df.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/finalDataCombinedRounded.csv", index=False)