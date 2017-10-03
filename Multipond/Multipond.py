import pandas as pd
import os

from MultipondFunctions import *
from pandas import DataFrame
from os.path import expanduser

# Let's assume the location of the files we want is in a folder
# called 16094 on the user's desktop. This will get the path.

print(expanduser("~"))
print(os.name)

# Check operating system

if os.name == "nt":
    delimeter = chr(92)    
    documentFolder = expanduser("~") + r"\Desktop\16094"
else:
    delimeter = r"/"    
    documentFolder = expanduser("~") + r"/Desktop/16094"

#Now let's import the HY8 table, storage table and hydrograph time series data

hy8 = pd.read_csv(documentFolder + delimeter + r"HY8.csv")
hydrographA = pd.read_csv(documentFolder + delimeter + r"A.csv")
hydrographB = pd.read_csv(documentFolder + delimeter + r"B.csv")
hydrographC = pd.read_csv(documentFolder + delimeter + r"C.csv")
hydrographD = pd.read_csv(documentFolder + delimeter + r"D.csv")
hydrographE = pd.read_csv(documentFolder + delimeter + r"E.csv")
hydrographF = pd.read_csv(documentFolder + delimeter + r"F.csv")
hydrographG = pd.read_csv(documentFolder + delimeter + r"G.csv")
hydrographH = pd.read_csv(documentFolder + delimeter + r"H.csv")
hydrographI = pd.read_csv(documentFolder + delimeter + r"I.csv")
hydrographJ = pd.read_csv(documentFolder + delimeter + r"J.csv")
hydrographK = pd.read_csv(documentFolder + delimeter + r"K.csv")
hydrographL = pd.read_csv(documentFolder + delimeter + r"L.csv")
hydrographM = pd.read_csv(documentFolder + delimeter + r"M.csv")
hydrographN = pd.read_csv(documentFolder + delimeter + r"N.csv")
hydrographO = pd.read_csv(documentFolder + delimeter + r"O.csv")
hydrographP = pd.read_csv(documentFolder + delimeter + r"P.csv")
hydrographQ = pd.read_csv(documentFolder + delimeter + r"Q.csv")

eastPondInflows = [hydrographA, hydrographB, hydrographC, hydrographD, hydrographF, hydrographG, hydrographM, hydrographN, hydrographO]
westPondInflows = [hydrographH, hydrographI, hydrographJ, hydrographK, hydrographL]

# Create the main tables we'll be populating

mainColumns = ['Timestep', 'East Flow', 'West Flow', 'East Volume Inflow', 'West Volume Inflow', 'East Start Volume', 'West Start Volume', 'Outflow', 'West Mid Volume', 'West Elevation', 
               'East Elevation', 'Cross Flow Direction', 'Cross Flow Amount', 'East End Volume', 'West End Volume']

# This will call the sumHydrographs function to add all the inflows together in the appropriate pond column

resultsTable = DataFrame(0.0, index = hydrographA.index, columns = mainColumns)
resultsTable = sumHydrographs(resultsTable, eastPondInflows, 'East')
resultsTable = sumHydrographs(resultsTable, westPondInflows, 'West')

for index, row in resultsTable.iterrows():
    if index > 550.0 and index < 650:
        print(str(resultsTable.loc[index, 'East Flow']) + "........." + str(resultsTable.loc[index, 'West Flow']))

# Now we calculate the volume increments. All volumes are done in units of acre-feet,
# to both respect the traditions of civil engineering and irritate physicists.


# Whole hell of a bunch of TODO beyond this point, along with some proof of concept
# Stuff to use later...

# Given the above, we now have our headwater, tailwater and
# directional conditions. Lets now look up the flow rate


headwater = 2.0
tailwater = 1.0
direction = 'east'


x,y = hy8Interpolation(hy8, headwater, tailwater)

print(str(x) + " " + str(y))
