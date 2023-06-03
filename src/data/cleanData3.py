import pandas as pd
import numpy as np

df = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/data/finalDataCombined.csv")

print(df["Total Underground"].sum())
roundedDf = df.copy()

roundedDf["Total Underground"] = df["Total Underground"].astype("int32")

print(roundedDf["Total Underground"].sum())
print(roundedDf.head())

roundedDf.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/src/data/finalDataCombinedRounded.csv", index=False)