# Prediction of Attack Origin page
# Support Vector Machine Cyber-Attack Prediction Program (SVM CAPP)__

# A GUI program (through Tkinter) utilizing SKLearn, SVM algorithm, to predict cybersecurity data via a Supervised
# dataset made of source and target data.  At this time the data is not made of completely real data, and the
# project is in the build/test phases.

# About Support Vector Machine (SVM)
# A support vector machine (SVM) is a type of Supervised machine learning classification algorithm.
# SVM differs from the other classification algorithms in the way that it chooses the decision boundary that maximizes
# the distance from the nearest data points of all the classes. An SVM doesn't merely find a decision boundary; it
# finds the most optimal decision boundary.
# (https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/)

# Utilizing SKlearn, pandas, numpy, xlrd APIs and also using a subclass of exception: import warnings (to prevent a
# Future Error warning from popping up; appears is due to possible future updates).

# Resources for original template build:
# https://www.youtube.com/watch?reload=9&v=bwZ3Qiuj3i8
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
# https://github.com/candi955/LottoProject   (my initial SVM project build and template for this project)

# Resources utilized for dataset creation:
# https://datacatalog.worldbank.org/dataset/world-development-indicators
# https://datacatalog.worldbank.org/dataset/global-economic-monitor
# https://csis-prod.s3.amazonaws.com/s3fs-public/190904_Significant_Cyber_Events_List.pdf
# https://www.csis.org/programs/technology-policy-program/significant-cyber-incidents



#---------Imports----------------------------------------------------------------------------------------------------
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

#------------ListBox Country/Region/Code Dictionaries--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated Code
# reference: https://www.w3schools.com/python/python_dictionaries.asp

# List 1 (Target country/region)
listTargetDictionary = {"Afghanistan":{"Code": 2},
                "Afghanistan_Application_Users_India_Individuals_Middle_East":{"Code": 3},
                "Africa":{"Code": 4},
                "Africa_Asia":{"Code": 5},
                "Al_Quaida":{"Code": 7},
                "Application_Users":{"Code": 8},
                "Application_Users_Individuals":{"Code": 9},
                "Application_Users_Japan":{"Code": 10},
                "Armenia":{"Code": 11},
                "Asia":{"Code": 12},
                "Asia_Canada_Europe_Middle_East_USA":{"Code": 13},
                "Asia_Europe_Middle_East_USA":{"Code": 14},
                "Asia_Europe_North_America":{"Code": 15},
                "Asia_South_America":{"Code": 16},
                "Asia_USA":{"Code": 17},
                "Australia":{"Code": 18},
                "Australia_Canada_Japan_Switzerland_UK_USA":{"Code": 19},
                "Australia_Canada_New_Zealand_UK_USA":{"Code": 20},
                "Austria":{"Code": 21},
                "Austria_Germany_Switzerland":{"Code": 22},
                "Bahrain":{"Code": 24},
                "Belarus_Mongolia_Russia":{"Code": 25},
                "Belgium":{"Code": 26},
                "Brazil":{"Code": 27},
                "Cambodia":{"Code": 28},
                "Canada":{"Code": 29},
                "Canada_France_Multiple_UK_USA":{"Code": 30},
                "Central_America":{"Code": 31},
                "Central_Asia_Eastern_Europe":{"Code": 32},
                "Central_Asia_Eastern_Europe_Russia":{"Code": 33},
                "Central_Asia_Europe_USA":{"Code": 34},
                "Chile":{"Code": 35},
                "China":{"Code": 36},
                "China_Germany":{"Code": 37},
                "China_Individuals":{"Code": 38},
                "China_Pakistan":{"Code": 40},
                "CSIS_USA":{"Code": 42},
                "Czech_Republic":{"Code": 43},
                "Czech_Republic_Individuals":{"Code": 44},
                "Denmark":{"Code": 46},
                "East_Asia":{"Code": 47},
                "Eastern_Europe":{"Code": 48},
                "Egypt":{"Code": 49},
                "Estonia":{"Code": 50},
                "Europe":{"Code": 51},
                "Europe_Individuals":{"Code": 52},
                "Europe_Individuals_Middle_East":{"Code": 53},
                "Europe_Japan_USA":{"Code": 54},
                "Europe_Middle_East":{"Code": 55},
                "Europe_Middle_East_North_America":{"Code": 56},
                "Europe_NATO":{"Code": 57},
                "Europe_NATO_Ukraine":{"Code": 58},
                "Europe_North_America":{"Code": 59},
                "Europe_Russia":{"Code": 60},
                "Finland":{"Code": 61},
                "France":{"Code": 62},
                "France_Germany_Japan":{"Code": 63},
                "France_Germany_UK": {"Code": 64},
                "France_South_Korea": {"Code": 65},
                "Georgia": {"Code": 68},
                "Germany": {"Code": 69},
                "Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA": {"Code": 70},
                "Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals": {"Code": 71},
                "Global_Unlisted": {"Code": 72},
                "Germany_Turkey": {"Code": 73},
                "India": {"Code": 74},
                "India_Italy_Saudi_Arabia_Scotland_UAE": {"Code": 75},
                "India_Pakistan": {"Code": 76},
                "Individuals": {"Code": 77},
                "Individuals_Iran": {"Code": 78},
                "Individuals_Latvia": {"Code": 79},
                "Individuals_Multiple": {"Code": 80},
                "Individuals_NATO_Ukraine": {"Code": 81},
                "Individuals_Sri_Lanka": {"Code": 82},
                "Individuals_USA": {"Code": 85},
                "Individuals_Vietnam": {"Code": 86},
                "Indonesia": {"Code": 87},
                "Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang": {"Code": 88},
                "International": {"Code": 89},
                "Iran": {"Code": 90},
                "Iran_Israel_Middle_East": {"Code": 91},
                "Iran_Syria": {"Code": 94},
                "Iraq_Pakistan_Tajikistan": {"Code": 97},
                "Ireland": {"Code": 98},
                "ISIS": {"Code": 99},
                "Israel": {"Code": 100},
                "Israel_Saudi_Arabia_USA": {"Code": 101},
                "Israel_Sudan_Syria_Middle_East": {"Code": 102},
                "Italy": {"Code": 104},
                "Italy_France_Germany_Poland_Spain_Turkey_USA": {"Code": 105},
                "Japan": {"Code": 106},
                "Japan_Multiple_Unlisted": {"Code": 107},
                "Japan_Unlisted": {"Code": 108},
                "Kazakhstan": {"Code": 109},
                "Lebanon": {"Code": 110},
                "Lebanon_UAE": {"Code": 111},
                "Libya": {"Code": 112},
                "Lithuania": {"Code": 113},
                "Malaysia": {"Code": 114},
                "Mexico": {"Code": 115},
                "Middle_East": {"Code": 116},
                "Middle_East_South_America_UK_USA": {"Code": 117},
                "Montenegro": {"Code": 118},
                "Multiple": {"Code": 120},
                "Multiple_Unlisted": {"Code": 121},
                "Netherlands": {"Code": 124},
                "Netherlands_territory": {"Code": 125},
                "NGOs_UN": {"Code": 126},
                "North_America_Pakistan_Russia_Saudi_Arabia_Turkey": {"Code": 128},
                "North_Korea": {"Code": 129},
                "Norway": {"Code": 130},
                "Oman_UAE": {"Code": 131},
                "Pakistan": {"Code": 132},
                "Philippines": {"Code": 133},
                "Qatar": {"Code": 134},
                "Qatar_Saudi_Arabia": {"Code": 135},
                "Russia": {"Code": 136},
                "Saudi_Arabia": {"Code": 139},
                "Saudi_Arabia_South_Korea_USA": {"Code": 140},
                "Saudi_Arabia_USA": {"Code": 141},
                "Scotland": {"Code": 142},
                "Singapore": {"Code": 143},
                "South_Africa": {"Code": 144},
                "South_Korea": {"Code": 145},
                "South_Korea_USA": {"Code": 146},
                "Southeast_Asia": {"Code": 147},
                "Sweden": {"Code": 149},
                "Switzerland": {"Code": 150},
                "Syria": {"Code": 151},
                "Taiwan": {"Code": 152},
                "Tehran": {"Code": 154},
                "Tibet": {"Code": 155},
                "Turkey": {"Code": 156},
                "UK": {"Code": 158},
                "UK_USA": {"Code": 159},
                "Ukraine": {"Code": 160},
                "UN": {"Code": 161},
                "Unlisted": {"Code": 1},
                "USA": {"Code": 162},
                "USA_Europe": {"Code": 163},
                "USA_Western_World": {"Code": 164},
                "Venezuela": {"Code": 165},
                "Western_World": {"Code": 167},
                "Xinjiang": {"Code": 168}}

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictOne = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# List 2 (Month of attack in Code numbers)

listMonthDictionary = {"January":{"code": 1}, # list option 0
                "February":{"Code": 2}, # list option 1
                "March":{"Code": 3}, # list option 2
                "April":{"Code": 4}, # list option 3
                "May":{"Code": 5}, # list option 4
                "June":{"Code": 6}, # list option 5
                "July":{"Code": 7}, # list option 6
                "August":{"Code": 8}, # list option 7
                "September":{"Code": 9}, # list option 8
                "October":{"Code": 10}, # list option 9
                "November":{"Code": 11}, # list option 10
                "December":{"Code": 12}, # list option 11
                "Unlisted":{"Code": 13}} # list option 12

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
#pdDictTwo = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('OriginAttackPredictionDataWithCodes_CleanedUp_20Apr2020_2400pm.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
    cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])


    # Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
    # will only show the last column in the target data
    sources = cyberSheetData[:, :-1]
    target = cyberSheetData[:, len(cyberSheetData[0]) - 1]

    # Deleting header column from dataframe, both source and target data
    sourceNoHeader = np.delete(sources, (0), axis=0)
    targetNoHeader = np.delete(target, (0), axis=0)

    X = sourceNoHeader
    y = targetNoHeader

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

    model = svm.SVC(kernel='linear')
    model.fit(X_train, y_train.ravel())
    y_pred = model.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)


#-----Creating Tkinter Setup (root) for GUI----------------------------------------------------------------------------
root = tk.Tk()
root.title('SVM Prediction: Attack Origin')
#root.geometry("1000x1000")

scrollBar = Scrollbar(root)
scrollBar.pack(side=RIGHT, fill=Y)


style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

# Tabs and Frames
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Attack Origin Prediction')

tab_control.pack(expand=1, fill='both')

# Tkinter listbox with root functions
# reference: http://effbot.org/tkinterbook/listbox.htm
listbox = Listbox(root, selectmode=SINGLE)


#---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
# List 1 function to place list and then transfer answer to textbox, for origin country/region choice
def get_selDummyOneTarget():
    for i in List1.curselection():
        if i == 0:
            Afghanistanlist = listTargetDictionary.get("Afghanistan")
            for k, v in Afghanistanlist.items():
                AfghanistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AfghanistanCode))
        if i == 1:
            Afghanistan_Application_Users_India_Individuals_Middle_Eastlist = listTargetDictionary.get(
                "Afghanistan_Application_Users_India_Individuals_Middle_East")
            for k, v in Afghanistan_Application_Users_India_Individuals_Middle_Eastlist.items():
                Afghanistan_Application_Users_India_Individuals_Middle_EastCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Afghanistan_Application_Users_India_Individuals_Middle_EastCode))
        if i == 2:
            Africalist = listTargetDictionary.get("Africa")
            for k, v in Africalist.items():
                AfricaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AfricaCode))
        if i == 3:
            Africa_Asialist = listTargetDictionary.get("Africa_Asia")
            for k, v in Africa_Asialist.items():
                Africa_AsiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Africa_AsiaCode))
        if i == 4:
            Al_Quaidalist = listTargetDictionary.get("Al_Quaida")
            for k, v in Al_Quaidalist.items():
                Al_QuaidaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Al_QuaidaCode))
        if i == 5:
            Application_Userslist = listTargetDictionary.get("Application_Users")
            for k, v in Application_Userslist.items():
                Application_UsersCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_UsersCode))
        if i == 6:
            Application_Users_Individualslist = listTargetDictionary.get("Application_Users_Individuals")
            for k, v in Application_Users_Individualslist.items():
                Application_Users_IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_Users_IndividualsCode))
        if i == 7:
            Application_Users_Japanlist = listTargetDictionary.get("Application_Users_Japan")
            for k, v in Application_Users_Japanlist.items():
                Application_Users_JapanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_Users_JapanCode))
        if i == 8:
            Armenialist = listTargetDictionary.get("Armenia")
            for k, v in Armenialist.items():
                ArmeniaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ArmeniaCode))
        if i == 9:
            Asialist = listTargetDictionary.get("Asia")
            for k, v in Asialist.items():
                AsiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AsiaCode))
        if i == 10:
            Asia_Canada_Europe_Middle_East_USAlist = listTargetDictionary.get("Asia_Canada_Europe_Middle_East_USA")
            for k, v in Asia_Canada_Europe_Middle_East_USAlist.items():
                Asia_Canada_Europe_Middle_East_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Asia_Canada_Europe_Middle_East_USACode))
        if i == 11:
            Asia_Europe_Middle_East_USAlist = listTargetDictionary.get("Asia_Europe_Middle_East_USA")
            for k, v in Asia_Europe_Middle_East_USAlist.items():
                Asia_Europe_Middle_East_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Asia_Europe_Middle_East_USACode))
        if i == 12:
            Asia_Europe_North_Americalist = listTargetDictionary.get("Asia_Europe_North_America")
            for k, v in Asia_Europe_North_Americalist.items():
                Asia_Europe_North_AmericaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Asia_Europe_North_AmericaCode))
        if i == 13:
            Asia_South_Americalist = listTargetDictionary.get("Asia_South_America")
            for k, v in Asia_South_Americalist.items():
                Asia_South_AmericaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Asia_South_AmericaCode))
        if i == 14:
            Asia_USAlist = listTargetDictionary.get("Asia_USA")
            for k, v in Asia_USAlist.items():
                Asia_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Asia_USACode))
        if i == 15:
            Australialist = listTargetDictionary.get("Australia")
            for k, v in Australialist.items():
                AustraliaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AustraliaCode))
        if i == 16:
            Australia_Canada_Japan_Switzerland_UK_USAlist = listTargetDictionary.get("Australia_Canada_Japan_Switzerland_UK_USA")
            for k, v in Australia_Canada_Japan_Switzerland_UK_USAlist.items():
                Australia_Canada_Japan_Switzerland_UK_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Australia_Canada_Japan_Switzerland_UK_USACode))
        if i == 17:
            Australia_Canada_New_Zealand_UK_USAlist = listTargetDictionary.get("Australia_Canada_New_Zealand_UK_USA")
            for k, v in Australia_Canada_New_Zealand_UK_USAlist.items():
                Australia_Canada_New_Zealand_UK_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Australia_Canada_New_Zealand_UK_USACode))
        if i == 18:
            Austrialist = listTargetDictionary.get("Austria")
            for k, v in Austrialist.items():
                AustriaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AustriaCode))
        if i == 19:
            Austria_Germany_Switzerlandlist = listTargetDictionary.get("Austria_Germany_Switzerland")
            for k, v in Austria_Germany_Switzerlandlist.items():
                Austria_Germany_SwitzerlandCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Austria_Germany_SwitzerlandCode))
        if i == 20:
            Bahrainlist = listTargetDictionary.get("Bahrain")
            for k, v in Bahrainlist.items():
                BahrainCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (BahrainCode))
        if i == 21:
            Belarus_Mongolia_Russialist = listTargetDictionary.get("Belarus_Mongolia_Russia")
            for k, v in Belarus_Mongolia_Russialist.items():
                Belarus_Mongolia_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Belarus_Mongolia_RussiaCode))
        if i == 22:
            Belgiumlist = listTargetDictionary.get("Belgium")
            for k, v in Belgiumlist.items():
                BelgiumCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (BelgiumCode))
        if i == 23:
            Brazillist = listTargetDictionary.get("Brazil")
            for k, v in Brazillist.items():
                BrazilCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (BrazilCode))
        if i == 24:
            Cambodialist = listTargetDictionary.get("Cambodia")
            for k, v in Cambodialist.items():
                CambodiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (CambodiaCode))
        if i == 25:
            Canadalist = listTargetDictionary.get("Canada")
            for k, v in Canadalist.items():
                CanadaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (CanadaCode))
        if i == 26:
            Canada_France_Multiple_UK_USAlist = listTargetDictionary.get("Canada_France_Multiple_UK_USA")
            for k, v in Canada_France_Multiple_UK_USAlist.items():
                Canada_France_Multiple_UK_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Canada_France_Multiple_UK_USACode))
        if i == 27:
            Central_Americalist = listTargetDictionary.get("Central_America")
            for k, v in Central_Americalist.items():
                Central_AmericaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Central_AmericaCode))
        if i == 28:
            Central_Asia_Eastern_Europelist = listTargetDictionary.get("Central_Asia_Eastern_Europe")
            for k, v in Central_Asia_Eastern_Europelist.items():
                Central_Asia_Eastern_EuropeCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Central_Asia_Eastern_EuropeCode))
        if i == 29:
            Central_Asia_Eastern_Europe_Russialist = listTargetDictionary.get("Central_Asia_Eastern_Europe_Russia")
            for k, v in Central_Asia_Eastern_Europe_Russialist.items():
                Central_Asia_Eastern_Europe_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Central_Asia_Eastern_Europe_RussiaCode))
        if i == 30:
            Central_Asia_Europe_USAlist = listTargetDictionary.get("Central_Asia_Europe_USA")
            for k, v in Central_Asia_Europe_USAlist.items():
                Central_Asia_Europe_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Central_Asia_Europe_USACode))
        if i == 31:
            Chilelist = listTargetDictionary.get("Chile")
            for k, v in Chilelist.items():
                ChileCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ChileCode))
        if i == 32:
            Chinalist = listTargetDictionary.get("China")
            for k, v in Chinalist.items():
                ChinaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ChinaCode))
        if i == 33:
            China_Germanylist = listTargetDictionary.get("China_Germany")
            for k, v in China_Germanylist.items():
                China_GermanyCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_GermanyCode))
        if i == 34:
            China_Individualslist = listTargetDictionary.get("China_Individuals")
            for k, v in China_Individualslist.items():
                China_IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_IndividualsCode))
        if i == 35:
            China_Pakistanlist = listTargetDictionary.get("China_Pakistan")
            for k, v in China_Pakistanlist.items():
                China_PakistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_PakistanCode))
        if i == 36:
            CSIS_USAlist = listTargetDictionary.get("CSIS_USA")
            for k, v in CSIS_USAlist.items():
                CSIS_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (CSIS_USACode))
        if i == 37:
            Czech_Republiclist = listTargetDictionary.get("Czech_Republic")
            for k, v in Czech_Republiclist.items():
                Czech_RepublicCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Czech_RepublicCode))
        if i == 38:
            Czech_Republic_Individualslist = listTargetDictionary.get("Czech_Republic_Individuals")
            for k, v in Czech_Republic_Individualslist.items():
                Czech_Republic_IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Czech_Republic_IndividualsCode))
        if i == 39:
            Denmarklist = listTargetDictionary.get("Denmark")
            for k, v in Denmarklist.items():
                DenmarkCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (DenmarkCode))
        if i == 40:
            East_Asialist = listTargetDictionary.get("East_Asia")
            for k, v in East_Asialist.items():
                East_AsiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (East_AsiaCode))
        if i == 41:
            Eastern_Europelist = listTargetDictionary.get("Eastern_Europe")
            for k, v in Eastern_Europelist.items():
                Eastern_EuropeCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Eastern_EuropeCode))
        if i == 42:
            Egyptlist = listTargetDictionary.get("Egypt")
            for k, v in Egyptlist.items():
                EgyptCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (EgyptCode))
        if i == 43:
            Estonialist = listTargetDictionary.get("Estonia")
            for k, v in Estonialist.items():
                EstoniaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (EstoniaCode))
        if i == 44:
            Europelist = listTargetDictionary.get("Europe")
            for k, v in Europelist.items():
                EuropeCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (EuropeCode))
        if i == 45:
            Europe_Individualslist = listTargetDictionary.get("Europe_Individuals")
            for k, v in Europe_Individualslist.items():
                Europe_IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_IndividualsCode))
        if i == 46:
            Europe_Individuals_Middle_Eastlist = listTargetDictionary.get("Europe_Individuals_Middle_East")
            for k, v in Europe_Individuals_Middle_Eastlist.items():
                Europe_Individuals_Middle_EastCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_Individuals_Middle_EastCode))
        if i == 47:
            Europe_Japan_USAlist = listTargetDictionary.get("Europe_Japan_USA")
            for k, v in Europe_Japan_USAlist.items():
                Europe_Japan_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_Japan_USACode))
        if i == 48:
            Europe_Middle_Eastlist = listTargetDictionary.get("Europe_Middle_East")
            for k, v in Europe_Middle_Eastlist.items():
                Europe_Middle_EastCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_Middle_EastCode))
        if i == 49:
            Europe_Middle_East_North_Americalist = listTargetDictionary.get("Europe_Middle_East_North_America")
            for k, v in Europe_Middle_East_North_Americalist.items():
                Europe_Middle_East_North_AmericaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_Middle_East_North_AmericaCode))
        if i == 50:
            Europe_NATOlist = listTargetDictionary.get("Europe_NATO")
            for k, v in Europe_NATOlist.items():
                Europe_NATOCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_NATOCode))
        if i == 51:
            Europe_NATO_Ukrainelist = listTargetDictionary.get("Europe_NATO_Ukraine")
            for k, v in Europe_NATO_Ukrainelist.items():
                Europe_NATO_UkraineCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_NATO_UkraineCode))
        if i == 52:
            Europe_North_Americalist = listTargetDictionary.get("Europe_North_America")
            for k, v in Europe_North_Americalist.items():
                Europe_North_AmericaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_North_AmericaCode))
        if i == 53:
            Europe_Russialist = listTargetDictionary.get("Europe_Russia")
            for k, v in Europe_Russialist.items():
                Europe_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Europe_RussiaCode))
        if i == 54:
            Finlandlist = listTargetDictionary.get("Finland")
            for k, v in Finlandlist.items():
                FinlandCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (FinlandCode))
        if i == 55:
            Francelist = listTargetDictionary.get("France")
            for k, v in Francelist.items():
                FranceCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (FranceCode))
        if i == 56:
            France_Germany_Japanlist = listTargetDictionary.get("France_Germany_Japan")
            for k, v in France_Germany_Japanlist.items():
                France_Germany_JapanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (France_Germany_JapanCode))
        if i == 57:
            France_Germany_UKlist = listTargetDictionary.get("France_Germany_UK")
            for k, v in France_Germany_UKlist.items():
                France_Germany_UKCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (France_Germany_UKCode))
        if i == 58:
            France_South_Korealist = listTargetDictionary.get("France_South_Korea")
            for k, v in France_South_Korealist.items():
                France_South_KoreaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (France_South_KoreaCode))
        if i == 59:
            Georgialist = listTargetDictionary.get("Georgia")
            for k, v in Georgialist.items():
                GeorgiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (GeorgiaCode))
        if i == 60:
            Germanylist = listTargetDictionary.get("Germany")
            for k, v in Germanylist.items():
                GermanyCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (GermanyCode))
        if i == 61:
            Germany_Israel_Jordan_Saudi_Arabia_Turkey_USAlist = listTargetDictionary.get("Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA")
            for k, v in Germany_Israel_Jordan_Saudi_Arabia_Turkey_USAlist.items():
                Germany_Israel_Jordan_Saudi_Arabia_Turkey_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Germany_Israel_Jordan_Saudi_Arabia_Turkey_USACode))
        if i == 62:
            Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individualslist = listTargetDictionary.get("Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals")
            for k, v in Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individualslist.items():
                Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsCode))
        if i == 63:
            Global_Unlistedlist = listTargetDictionary.get("Global_Unlisted")
            for k, v in Global_Unlistedlist.items():
                Global_UnlistedCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Global_UnlistedCode))
        if i == 64:
            Germany_Turkeylist = listTargetDictionary.get("Germany_Turkey")
            for k, v in Germany_Turkeylist.items():
                Germany_TurkeyCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Germany_TurkeyCode))
        if i == 65:
            Indialist = listTargetDictionary.get("India")
            for k, v in Indialist.items():
                IndiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IndiaCode))
        if i == 66:
            India_Italy_Saudi_Arabia_Scotland_UAElist = listTargetDictionary.get("India_Italy_Saudi_Arabia_Scotland_UAE")
            for k, v in India_Italy_Saudi_Arabia_Scotland_UAElist.items():
                India_Italy_Saudi_Arabia_Scotland_UAECode = "{}".format(v)
                dummyNumberOne.insert(1.0, (India_Italy_Saudi_Arabia_Scotland_UAECode))
        if i == 67:
            India_Pakistanlist = listTargetDictionary.get("India_Pakistan")
            for k, v in India_Pakistanlist.items():
                India_PakistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (India_PakistanCode))
        if i == 68:
            Individualslist = listTargetDictionary.get("Individuals")
            for k, v in Individualslist.items():
                IndividualsCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IndividualsCode))
        if i == 69:
            Individuals_Iranlist = listTargetDictionary.get("Individuals_Iran")
            for k, v in Individuals_Iranlist.items():
                Individuals_IranCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_IranCode))
        if i == 70:
            Individuals_Latvialist = listTargetDictionary.get("Individuals_Latvia")
            for k, v in Individuals_Latvialist.items():
                Individuals_LatviaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_LatviaCode))
        if i == 71:
            Individuals_Multiplelist = listTargetDictionary.get("Individuals_Multiple")
            for k, v in Individuals_Multiplelist.items():
                Individuals_MultipleCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_MultipleCode))
        if i == 72:
            Individuals_NATO_Ukrainelist = listTargetDictionary.get("Individuals_NATO_Ukraine")
            for k, v in Individuals_NATO_Ukrainelist.items():
                Individuals_NATO_UkraineCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_NATO_UkraineCode))
        if i == 73:
            Individuals_Sri_Lankalist = listTargetDictionary.get("Individuals_Sri_Lanka")
            for k, v in Individuals_Sri_Lankalist.items():
                Individuals_Sri_LankaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_Sri_LankaCode))
        if i == 74:
            Individuals_USAlist = listTargetDictionary.get("Individuals_USA")
            for k, v in Individuals_USAlist.items():
                Individuals_USACode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_USACode))
        if i == 75:
            Individuals_Vietnamlist = listTargetDictionary.get("Individuals_Vietnam")
            for k, v in Individuals_Vietnamlist.items():
                Individuals_VietnamCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Individuals_VietnamCode))
        if i == 76:
            Indonesialist = listTargetDictionary.get("Indonesia")
            for k, v in Indonesialist.items():
                IndonesiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (IndonesiaCode))
        if i == 77:
            Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjianglist = listTargetDictionary.get("Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang")
            for k, v in Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjianglist.items():
                Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangCode))
        if i == 78:
            Internationallist = listTargetDictionary.get("International")
            for k, v in Internationallist.items():
                InternationalCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (InternationalCode))



#                 "Iran": {"Code": 90},
#                 "Iran_Israel_Middle_East": {"Code": 91},
#                 "Iran_Syria": {"Code": 94},
#                 "Iraq_Pakistan_Tajikistan": {"Code": 97},
#                 "Ireland": {"Code": 98},
#                 "ISIS": {"Code": 99},
#                 "Israel": {"Code": 100},
#                 "Israel_Saudi_Arabia_USA": {"Code": 101},
#                 "Israel_Sudan_Syria_Middle_East": {"Code": 102},
#                 "Italy": {"Code": 104},
#                 "Italy_France_Germany_Poland_Spain_Turkey_USA": {"Code": 105},
#                 "Japan": {"Code": 106},
#                 "Japan_Multiple_Unlisted": {"Code": 107},
#                 "Japan_Unlisted": {"Code": 108},
#                 "Kazakhstan": {"Code": 109},
#                 "Lebanon": {"Code": 110},
#                 "Lebanon_UAE": {"Code": 111},
#                 "Libya": {"Code": 112},
#                 "Lithuania": {"Code": 113},
#                 "Malaysia": {"Code": 114},
#                 "Mexico": {"Code": 115},
#                 "Middle_East": {"Code": 116},
#                 "Middle_East_South_America_UK_USA": {"Code": 117},
#                 "Montenegro": {"Code": 118},
#                 "Multiple": {"Code": 120},
#                 "Multiple_Unlisted": {"Code": 121},
#                 "Netherlands": {"Code": 124},
#                 "Netherlands_territory": {"Code": 125},
#                 "NGOs_UN": {"Code": 126},
#                 "North_America_Pakistan_Russia_Saudi_Arabia_Turkey": {"Code": 128},
#                 "North_Korea": {"Code": 129},
#                 "Norway": {"Code": 130},
#                 "Oman_UAE": {"Code": 131},
#                 "Pakistan": {"Code": 132},
#                 "Philippines": {"Code": 133},
#                 "Qatar": {"Code": 134},
#                 "Qatar_Saudi_Arabia": {"Code": 135},
#                 "Russia": {"Code": 136},
#                 "Saudi_Arabia": {"Code": 139},
#                 "Saudi_Arabia_South_Korea_USA": {"Code": 140},
#                 "Saudi_Arabia_USA": {"Code": 141},
#                 "Scotland": {"Code": 142},
#                 "Singapore": {"Code": 143},
#                 "South_Africa": {"Code": 144},
#                 "South_Korea": {"Code": 145},
#                 "South_Korea_USA": {"Code": 146},
#                 "Southeast_Asia": {"Code": 147},
#                 "Sweden": {"Code": 149},
#                 "Switzerland": {"Code": 150},
#                 "Syria": {"Code": 151},
#                 "Taiwan": {"Code": 152},
#                 "Tehran": {"Code": 154},
#                 "Tibet": {"Code": 155},
#                 "Turkey": {"Code": 156},
#                 "UK": {"Code": 158},
#                 "UK_USA": {"Code": 159},
#                 "Ukraine": {"Code": 160},
#                 "UN": {"Code": 161},
#                 "Unlisted": {"Code": 1},
#                 "USA": {"Code": 162},
#                 "USA_Europe": {"Code": 163},
#                 "USA_Western_World": {"Code": 164},
#                 "Venezuela": {"Code": 165},
#                 "Western_World": {"Code": 167},
#                 "Xinjiang": {"Code": 168}}










# List 2 function to place list and then transfer answer to textbox, for Month choice
def get_selDummyTwoMonth():
    for i in List2.curselection():
        if i == 0:
            Januarylist = listMonthDictionary.get("January")
            for k, v in Januarylist.items():
                JanuaryCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JanuaryCode))
        if i == 1:
            Februarylist = listMonthDictionary.get("February")
            for k, v in Februarylist.items():
                FebruaryCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (FebruaryCode))
        if i == 2:
            Marchlist = listMonthDictionary.get("March")
            for k, v in Marchlist.items():
                MarchCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MarchCode))
        if i == 3:
            Aprillist = listMonthDictionary.get("April")
            for k, v in Aprillist.items():
                AprilCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AprilCode))
        if i == 4:
            Maylist = listMonthDictionary.get("May")
            for k, v in Maylist.items():
                MayCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MayCode))
        if i == 5:
            Junelist = listMonthDictionary.get("June")
            for k, v in Junelist.items():
                JuneCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JuneCode))
        if i == 6:
            Julylist = listMonthDictionary.get("July")
            for k, v in Julylist.items():
                JulyCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JulyCode))
        if i == 7:
            Augustlist = listMonthDictionary.get("August")
            for k, v in Augustlist.items():
                AugustCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AugustCode))
        if i == 8:
            Septemberlist = listMonthDictionary.get("September")
            for k, v in Septemberlist.items():
                SeptemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (SeptemberCode))
        if i == 9:
            Octoberlist = listMonthDictionary.get("October")
            for k, v in Octoberlist.items():
                OctoberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (OctoberCode))
        if i == 10:
            Novemberlist = listMonthDictionary.get("November")
            for k, v in Novemberlist.items():
                NovemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (NovemberCode))
        if i == 11:
            Decemberlist = listMonthDictionary.get("December")
            for k, v in Decemberlist.items():
                DecemberCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (DecemberCode))
        if i == 12:
            Unlistedlist = listMonthDictionary.get("Unlisted")
            for k, v in Unlistedlist.items():
                UnlistedCode = "{}".format(v)
                dummyNumberTwo.insert(1.0, (UnlistedCode))


# the accuracy score method
def writeAccuracy(buttonClicks):
    if buttonClicks == 1:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("Prediction accuracy of target prediction page")

        popUpLabel = tk.Label(win,
                              text="Please see the accuracy percentage of the Target Prediction algorithm below:\n")
        popUpLabel.grid(row=0, column=0)

        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=2, width=30)
        dataSetDisplay.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        # decimal form of predication accuracy percentage
        # dataSetDisplay.insert(4.0, str(accuracy_score(y_test, y_pred)))
        # percentage form of predication accuracy percentage
        acc = accuracy_score(y_test, y_pred)
        dataSetDisplay.insert(4.0, str("%.0f%%" % (acc * 100)))

    else:
        mbox.showerror("Error", "Returning to the main menu.")
        import mainPage

# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

#---- Creating functions to run the main prediction program ----------------------------------------------------------

# the dummy number value method, for tab 3 input entries from the user
def dummyValues():
    while True:
        try:
            # Getting user-input for dummy numbers to be used in the algorithm
            # Dummy User Choice 1 -
            dummyTextOne = dummyNumberOne.get('1.0', tk.END)
            # Dummy User Choice 2 -
            dummyTextTwo = dummyNumberTwo.get('1.0', tk.END)
            # Dummy User Choice 3 -
            dummyTextThree = dummyNumberThree.get('1.0', tk.END)
            # Dummy User Choice 4 -
            dummyTextFour = dummyNumberFour.get('1.0', tk.END)
            # Dummy User Choice 5 -
            dummyTextFive = dummyNumberFive.get('1.0', tk.END)
            # Dummy 6 User Choice 6 -
            dummyTextSix = dummyNumberSix.get('1.0', tk.END)

            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = float(dummyTextOne)
            dummyValues.dummyTextTwo = float(dummyTextTwo)
            dummyValues.dummyTextThree = float(dummyTextThree)
            dummyValues.dummyTextFour = float(dummyTextFour)
            dummyValues.dummyTextFive = float(dummyTextFive)
            dummyValues.dummyTextSix = float(dummyTextSix)

        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        # Removed the if statements for exception due to planning to change this option to list-option

        else:
            # breaking the loop to avoid infinite loop
            break

# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():

    while True:
        try:
            #calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive, dummyValues.dummyTextSix])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            tab1_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break

# Below is the creation of textbox entries; however am planning to make dummy number option a label option
def clear_display_result():
    tab1_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)
    dummyNumberFive.delete(1.0, END)
    dummyNumberSix.delete(1.0, END)
    # when boxes are cleared, bringing the option focus for the user back to the initial textbox
    dummyNumberOne.focus()

def mainMenu():

    while True:
        try:

            # Creating a messagebox for when the user clicks to exit the program, with exception prevention
            if mbox.askokcancel("Quit", "Do you want to quit?"):
                #root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
                root.destroy()
                import mainPage


        except ValueError:
            import mainPage
        else:
            break

def exitProgram():
    exit()

def flush(self):
    pass

#------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(tab1, text='Please enter six situational choices in the cells below, and then click the Prediction button'+
                      'to see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)

#--------------------- Dummy 1 Listbox and Textbox Attack Origin-------------------------------------------------------
#Listbox of Dummy Numbers
dummyOneListBox = Listbox(tab1) # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=2, column=0, padx=5, pady=5, ipadx=250, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listTargetDictionary:
    List1.insert(END, '{}: {}'.format(key, listTargetDictionary[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(tab1, height=2, width=50)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
#Listbox of Dummy Numbers
dummyTwoListBox = Listbox(tab1, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyTwoListBox.grid(row=4, column=0, columnspan=1, padx=5, pady=5, ipadx=250, ipady=0)

List2 = Listbox(dummyTwoListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listMonthDictionary:
    List2.insert(END, '{}: {}'.format(key, listMonthDictionary[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = Text(tab1, height=2, width=50)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(tab1, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(tab1, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 5 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberFive = Text(tab1, height=2, width=50)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 6 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberSix = Text(tab1, height=2, width=50)
dummyNumberSix.bind("<Tab>", focus_next_widget)
dummyNumberSix.grid(row=7, column=1, columnspan=1, padx=5, pady=5)

#-------Tkinter Buttons------------------------------------------------------------------------------------------------

# Tab 2
# Accuracy Button
AccuracyButton = Button(tab1, text='Prediction Accuracy', command=lambda:writeAccuracy(1), width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=0, column=1, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

# List 1 Origin country/region choice buttons
DummyOneButtonSubmit = Button(tab1, text="Submit Attack Origin", command=lambda: get_selDummyOneTarget(), width=20, bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=3, column=0, padx=15, pady=15)

# List 2 Origin country/region choice button
DummyTwoButtonSubmit = Button(tab1, text="Submit Month", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple', fg='#fff')
DummyTwoButtonSubmit.grid(row=5, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab1, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=6, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab1, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=1, column=1, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=0, column=0, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=8, column=0, padx=5, pady=5)

#------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results

# Prediction results window in tab 3
tab1_display = Text(tab1, height=1)
tab1_display.grid(row=7, column=0, columnspan=1, padx=5, pady=5)

# Keep window alive
mainloop()