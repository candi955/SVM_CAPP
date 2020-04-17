# Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox

# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



locationDict = {"country1":{"name" : "China", "binary": 418464229443},
                "country2":{"name":"USA","binary" : 4281173},
                "country3":{"name":"Russia","binary" : 107105536406866},

                "region1":{"name":"Asia","binary" : 1634300737},
                "region2":{"name":"Europe","binary" : 111533580514629},}


pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print('\n')
print("locationDict: \n" )
print(locationDict)
print("\n\n")

print("pdDict: \n")
print(pdDict)
print("\n\n")

print("Values: \n")
print(locationDict.values())
print("\n")

print("Keys: \n")
print(locationDict.keys())
print("\n")

print("Items: \n")
print(locationDict.items())
print("\n")

print(locationDict.get("country1"))
country1list = locationDict.get("country1")
print("hello")
for k, v in country1list.items():
    print("{}".format(v))
    
# output:
# {'name': 'China', 'binary': 418464229443}
# hello
# China
# 418464229443

