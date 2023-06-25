import pandas as pd
import numpy as np

data = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/2021_us.csv", low_memory=False)

dataCondensed = data[["4. FACILITY NAME", 
                      "34. CHEMICAL", 
                      "51. 5.4 - UNDERGROUND",
                      "40. CLASSIFICATION",
                      "41. METAL",
                      "43. CARCINOGEN",
                      "44. PBT",
                      "45. PFAS",
                      "47. UNIT OF MEASURE",
                      "52. 5.4.1 - UNDERGROUND CL I",
                      "53. 5.4.2 - UNDERGROUND C II-V",
                      "71. 6.2 - M71",
                      "72. 6.2 - M81",
                      "73. 6.2 - M82"]]


def convertToPounds(df):
    if df["47. UNIT OF MEASURE"] == "Grams":
        df["51. 5.4 - UNDERGROUND"] *= 0.0022
        df["52. 5.4.1 - UNDERGROUND CL I"] *= 0.0022
        df["53. 5.4.2 - UNDERGROUND C II-V"] *= 0.0022
        df["71. 6.2 - M71"] *= 0.0022
        df["72. 6.2 - M81"] *= 0.0022
        df["73. 6.2 - M82"] *= 0.0022
    return df

dataCondensedPounds = dataCondensed.apply(convertToPounds, raw=True, axis=1, result_type="broadcast")

dataCondensedPounds.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/DataCondensedPounds.csv")

