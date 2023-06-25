import pandas as pd
import numpy as np

import os.path


if not os.path.isfile("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataGroupedByChem.csv"):
    data = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/2021_us.csv", low_memory=False)

    convertion = {"Grams": 0.0022}

    data = data[["34. CHEMICAL",
     "40. CLASSIFICATION",
    "41. METAL",
     "43. CARCINOGEN",
     "44. PBT",
     "45. PFAS",
     "47. UNIT OF MEASURE",
     "48. 5.1 - FUGITIVE AIR",
     "49. 5.2 - STACK AIR",
     "50. 5.3 - WATER",
     "51. 5.4 - UNDERGROUND",
     "52. 5.4.1 - UNDERGROUND CL I",
    "53. 5.4.2 - UNDERGROUND C II-V",
     "54. 5.5.1 - LANDFILLS",
     "55. 5.5.1A - RCRA C LANDFILL",
     "56. 5.5.1B - OTHER LANDFILLS",
    "57. 5.5.2 - LAND TREATMENT",
     "58. 5.5.3 - SURFACE IMPNDMNT",
     "59. 5.5.3A - RCRA SURFACE IM",
     "60. 5.5.3B - OTHER SURFACE I",
     "61. 5.5.4 - OTHER DISPOSAL",
     "62. ON-SITE RELEASE TOTAL",
     "63. 6.1 - POTW - TRNS RLSE",
     "64. 6.1 - POTW - TRNS TRT",
     "71. 6.2 - M71",
     "72. 6.2 - M81",
     "73. 6.2 - M82",
     "74. 6.2 - M72",
     "75. 6.2 - M63",
     "76. 6.2 - M66",
     "77. 6.2 - M67",
     "78. 6.2 - M64",
     "79. 6.2 - M65",
     "80. 6.2 - M73",
     "81. 6.2 - M79",
     "82. 6.2 - M90",
     "83. 6.2 - M94",
     "84. 6.2 - M99",
     "88. 6.2 - M26",
     "91. OFF-SITE RECYCLED TOTAL",
     "94. OFF-SITE ENERGY RECOVERY T",
     "101. OFF-SITE TREATED TOTAL",
     "103. 6.2 - TOTAL TRANSFER"]]

    agg_functions = {"34. CHEMICAL": "first",'40. CLASSIFICATION': 'first', '41. METAL': 'first', "43. CARCINOGEN": "first", "44. PBT": "first", "45. PFAS": "first", "47. UNIT OF MEASURE": "first", "48. 5.1 - FUGITIVE AIR": "sum", "49. 5.2 - STACK AIR": "sum", "50. 5.3 - WATER": "sum", "51. 5.4 - UNDERGROUND": "sum", "52. 5.4.1 - UNDERGROUND CL I": "sum","53. 5.4.2 - UNDERGROUND C II-V": "sum", "54. 5.5.1 - LANDFILLS": "sum", "55. 5.5.1A - RCRA C LANDFILL": "sum", "56. 5.5.1B - OTHER LANDFILLS": "sum","57. 5.5.2 - LAND TREATMENT": "sum", "58. 5.5.3 - SURFACE IMPNDMNT": "sum", "59. 5.5.3A - RCRA SURFACE IM": "sum", "60. 5.5.3B - OTHER SURFACE I": "sum", "61. 5.5.4 - OTHER DISPOSAL": "sum", "62. ON-SITE RELEASE TOTAL": "sum", "63. 6.1 - POTW - TRNS RLSE": "sum", "64. 6.1 - POTW - TRNS TRT": "sum", "71. 6.2 - M71": "sum", "72. 6.2 - M81": "sum", "73. 6.2 - M82": "sum", "74. 6.2 - M72": "sum", "75. 6.2 - M63": "sum", "76. 6.2 - M66": "sum", "77. 6.2 - M67": "sum", "78. 6.2 - M64": "sum", "79. 6.2 - M65": "sum", "80. 6.2 - M73": "sum", "81. 6.2 - M79": "sum", "82. 6.2 - M90": "sum", "83. 6.2 - M94": "sum", "84. 6.2 - M99": "sum", "88. 6.2 - M26": "sum", "91. OFF-SITE RECYCLED TOTAL": "sum", "94. OFF-SITE ENERGY RECOVERY T": "sum", "101. OFF-SITE TREATED TOTAL": "sum", "103. 6.2 - TOTAL TRANSFER": "sum"}
    data = data.groupby(data["34. CHEMICAL"]).aggregate(agg_functions)

    data.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataGroupedByChem.csv", index=False)

if not os.path.isfile("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/ChemicalsByTotal.csv"):
    data = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataGroupedByChem.csv")
    dataTotals = {"Chemical": [], "Metal": [], "Carcinogen": [], "PBT": [], "PFAS": [], "Units":[], "Air": [], "Water": [], "Landfill": [], "Underground Wells": [], "Land Treatment": [], "Surface Impoundment": [], "Recycled": []}
    for index, row in data.iterrows():
        dataTotals["Chemical"].append(row["34. CHEMICAL"])
        dataTotals["Metal"].append(row["41. METAL"])
        dataTotals["Carcinogen"].append(row["43. CARCINOGEN"])
        dataTotals["PBT"].append(row["44. PBT"])
        dataTotals["PFAS"].append(row["45. PFAS"])
        dataTotals["Units"].append(row["47. UNIT OF MEASURE"])
        dataTotals["Air"].append(row[["48. 5.1 - FUGITIVE AIR", "49. 5.2 - STACK AIR"]].sum())
        dataTotals["Water"].append(row["50. 5.3 - WATER"])
        dataTotals["Landfill"].append(row[["56. 5.5.1B - OTHER LANDFILLS", "54. 5.5.1 - LANDFILLS", "55. 5.5.1A - RCRA C LANDFILL", "74. 6.2 - M72", "78. 6.2 - M64", "79. 6.2 - M65",  "81. 6.2 - M79"]].sum())
        dataTotals["Underground Wells"].append(row[["51. 5.4 - UNDERGROUND", "52. 5.4.1 - UNDERGROUND CL I", "53. 5.4.2 - UNDERGROUND C II-V","71. 6.2 - M71", "72. 6.2 - M81", "73. 6.2 - M82",]].sum())
        dataTotals["Land Treatment"].append(row[["57. 5.5.2 - LAND TREATMENT", "80. 6.2 - M73"]].sum())
        dataTotals["Surface Impoundment"].append(row[["58. 5.5.3 - SURFACE IMPNDMNT", "59. 5.5.3A - RCRA SURFACE IM","60. 5.5.3B - OTHER SURFACE I", "75. 6.2 - M63", "76. 6.2 - M66", "77. 6.2 - M67"]].sum())
        dataTotals["Recycled"].append(row["91. OFF-SITE RECYCLED TOTAL"])
        
    dataTotals = pd.DataFrame(dataTotals)
    dataTotals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/ChemicalsByTotal.csv", index=False)


allChemicals = pd.read_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/ChemicalsByTotal.csv")

def grabTopData(data, disposalType):
    return data.sort_values(by=[disposalType], ascending=False).iloc[:20]

topAirChemicals = grabTopData(allChemicals, "Air")
topWaterChemicals = grabTopData(allChemicals, "Water")
topLandfillChemicals = grabTopData(allChemicals, "Landfill")
topUndergroundChemicals = grabTopData(allChemicals, "Underground Wells")
topLandChemicals = grabTopData(allChemicals, "Land Treatment")
topSurfaceChemicals = grabTopData(allChemicals, "Surface Impoundment")
topRecycledChemicals = grabTopData(allChemicals, "Recycled")

topAirChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topAir.csv")
topWaterChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topWater.csv")
topLandfillChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topLandfill.csv")
topUndergroundChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topUnderground.csv")
topLandChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topLand.csv")
topSurfaceChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topSurface.csv")
topRecycledChemicals.to_csv("/Users/xanderburger/dataViz/toxicsReleaseInventory/site/public/dataByDisposalType/topRecycled.csv")
