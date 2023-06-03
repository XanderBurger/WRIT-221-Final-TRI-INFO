import pandas as pd 
import numpy as np

dataCondensedPounds = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/DataCondensedPounds.csv")

#dataCondensedPounds["Total Underground"] = np.zeros((dataCondensedPounds["4. FACILITY NAME"].size,1))

#dataCondensedPounds = dataCondensedPounds.apply(lambda row: row["Total Underground"] + 1, axis=1, result_type="broadcast") 
totals = {"Total Underground": []}

for index, row in dataCondensedPounds.iterrows():
    total = (
        row["51. 5.4 - UNDERGROUND"] + 
        row["52. 5.4.1 - UNDERGROUND CL I"] +
        row["53. 5.4.2 - UNDERGROUND C II-V"] +
        row["71. 6.2 - M71"] +
        row["72. 6.2 - M81"] + 
        row["73. 6.2 - M82"]
    )
    totals["Total Underground"].append(total)

dataCondensedPounds["Total Underground"] = totals["Total Underground"]

print(dataCondensedPounds["Total Underground"].sum())

dataCondensedPounds = dataCondensedPounds[~(dataCondensedPounds[["Total Underground"]] == 0).all(axis=1)]


dataCondensedPounds.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/DataCondensedPoundsTotals.csv")







