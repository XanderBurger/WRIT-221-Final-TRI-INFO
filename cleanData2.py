import pandas as pd
import numpy as np
from thefuzz import fuzz, process

dataCondensedPounds = pd.read_csv("toxicsReleaseInventory/site/public/DataCondensedPoundsTotals.csv")

finalData = {"Chemical": [], "Type": [], "Total Underground": []}

for index, row in dataCondensedPounds.iterrows():
    if row["34. CHEMICAL"] not in finalData["Chemical"]:
        finalData["Chemical"].append(row["34. CHEMICAL"])
        finalData["Type"].append(row["40. CLASSIFICATION"])
        finalData["Total Underground"].append(0)

finalData = pd.DataFrame(finalData)
for fIndex, fRow in finalData.iterrows():
    for dIndex, dRow in dataCondensedPounds.iterrows():
        if fRow["Chemical"] == dRow["34. CHEMICAL"]:
            finalData.at[fIndex, "Total Underground"] += dRow["Total Underground"]

def is_close_match(name, unique_names, threshold=93):
    return True if fuzz.partial_ratio(name, unique_names) > threshold else False

names = finalData['Chemical']
unique_names = []

for index, row in finalData.iterrows():
    for name in names:
        if is_close_match(row["Chemical"], name) and name not in unique_names:
            unique_names.append(name)

dataCombined = finalData.copy()

for name in unique_names:
    for index, row in dataCombined.iterrows():
        if is_close_match(name, row["Chemical"]):
            dataCombined.at[index, "Chemical"] = name

finalData.sort_values(by=["Chemical"], inplace=True)
dataCombined.sort_values(by=["Chemical"], inplace=True)
finalData.to_csv("toxicsReleaseInventory/site/public/finalData.csv")

agg_functions = {'Type': 'first', 'Total Underground': 'sum'}
dataCombined = dataCombined.groupby(dataCombined["Chemical"]).aggregate(agg_functions)
dataCombined.to_csv("toxicsReleaseInventory/site/public/finalDataCombined.csv")

print(dataCombined["Total Underground"].sum())
print(finalData["Total Underground"].sum())
