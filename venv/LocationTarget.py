# Prediction of Attack Target page
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

# List 1 (Origin country/region)
listOriginDictionary = {"Africa_China":{"Code": 30153525564624871856989693505},
                "Australia":{"Code": 1796930728965501580609},
                "Azerbaijan":{"Code": 521257315057726828935745},
                "Brazil":{"Code": 119200280572482},
                "China":{"Code": 418464229443},
                "China_North_Korea":{"Code": 33142235798066285977489245281315271043139},
                "China_Pakistan":{"Code": 2238786227951005213617790124648515},
                "China_Russia":{"Code": 30147528365705030538042632259},
                "Czech_Republic":{"Code": 2016311051235894369754033219271235},
                "Decentralized_International_Hacktivist_Group":{"Code": 4030061651715448937258886338687573509473192067501578500999556277764116296964663760381662969481473103717700},
                "Eastern_Europe":{"Code": 2057431415377846504395799230898501},
                "Egypt":{"Code": 500103210821},
                "Gaza":{"Code": 1635410247},
                "Gaza_Former_Soviet_Union_Lebanon":{"Code": 49951295185924953357192938129459662694624102732189565470444669956949290934599},
                "Germany":{"Code": 34179836909086023},
                "India":{"Code": 418380017225},
                "Individuals":{"Code": 139538282629009384004677193},
                "Individuals_Ukraine":{"Code": 2261993475681827677736728506999153589307600457},
                "Individuals_Unlisted":{"Code": 573161596645207770904272559636410843002082455113},
                "International":{"Code": 8586795105461350372667137748553},
                "Iran":{"Code": 1851880009},
                "Iran_North_Korea_Russia":{"Code": 9330208112349500424777135934104632250386116936128885321},
                "Iran_Russia":{"Code": 117763782678535275756483145},
                "Iran_Unlisted":{"Code": 7954215017830331842300462854729},
                "Iraq":{"Code": 1902211657},
                "ISIS":{"Code": 1397314377},
                "Israel":{"Code": 119182682387273},
                "Israel_USA":{"Code": 308491052899443525448521},
                "Lebanon":{"Code": 31084767309096268},
                "Mexico":{"Code": 122472761943373},
                "Middle_East":{"Code": 140780261553827770911713613},
                "Morocco":{"Code": 31353001137565517},
                "Multiple":{"Code": 7308339893542614349},
                "Nation_State_Actor_Eastern_Europe":{"Code": 11745856961995155074459591118783721087539815469043632190606120890413099009728846},
                "Nation_State_Actor_Unlisted":{"Code": 41300645649190979956682253942903520807850576892501048304935919950},
                "Non_State_Actor_Unlisted":{"Code": 2461710312914310691158905860358686495295201354771914977102},
                "North_Korea":{"Code": 117744874465821730700160846},
                "Pakistan":{"Code": 7953766455951712592},
                "Russia":{"Code": 107105536406866},
                "Russia_Ukraine":{"Code": 2057271081577553266210956287112530},
                "Russia_Ukraine_USA":{"Code": 5690655501723968284733388360289691192489298},
                "Saudi_Arabia":{"Code": 30147447753212470604776956243},
                "South_Korea":{"Code": 117744874465821730700357459},
                "South_Korea_USA":{"Code": 339189499714501404461968594046381907},
                "State_Sponsored_Actor_Unlisted":{"Code": 692909852995937295984928817766944035748308436617603438577965161292854355},
                "Syria":{"Code": 418380937555},
                "Taiwan":{"Code": 121364894277972},
                "Taiwan_USA":{"Code": 308491052901625737339220},
                "Turkey":{"Code": 133476501321044},
                "UAE":{"Code": 4538709},
                "UK":{"Code": 19285},
                "UK_USA":{"Code": 71826170399573},
                "Unlisted":{"Code": 7234316415479344725},
                "USA":{"Code": 4281173},
                "Vietnam":{"Code": 30787899488561494},
                "Western_World":{"Code": 7956378975824997986907049911639},
                "Yemen":{"Code": 474148070745}}

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
cyberExcel = xlrd.open_workbook('FakeTargetNumsDataset SVMCAPPdataset.xlsx')
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
root.title('SVM Prediction: Target Attack')
#root.geometry("1000x1000")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')
# Tabs and Frames
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Dataset')
tab_control.add(tab2, text='Prediction Accuracy')
tab_control.add(tab3, text='Dummy Values and Target Prediction')

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
def get_selDummyOne():
    for i in List1.curselection():
        if i == 0:
            Africa_Chinalist = listOriginDictionary.get("Africa_China")
            for k, v in Africa_Chinalist.items():
                Africa_ChinaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Africa_ChinaCode))
        if i == 1:
            Australialist = listOriginDictionary.get("Australia")
            for k, v in Australialist.items():
                AustraliaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AustraliaCode))
        if i == 2:
            Azerbaijanlist = listOriginDictionary.get("Azerbaijan")
            for k, v in Azerbaijanlist.items():
                AzerbaijanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (AzerbaijanCode))
        if i == 3:
            Brazillist = listOriginDictionary.get("Brazil")
            for k, v in Brazillist.items():
                BrazilCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (BrazilCode))
        if i == 4:
            Chinalist = listOriginDictionary.get("China")
            for k, v in Chinalist.items():
                ChinaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ChinaCode))
        if i == 5:
            China_North_Korealist = listOriginDictionary.get("China_North_Korea")
            for k, v in China_North_Korealist.items():
                China_North_KoreaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_North_KoreaCode))
        if i == 6:
            China_Pakistanlist = listOriginDictionary.get("China_Pakistan")
            for k, v in China_Pakistanlist.items():
                China_PakistanCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_PakistanCode))
        if i == 7:
            China_Russialist = listOriginDictionary.get("China_Russia")
            for k, v in China_Russialist.items():
                China_RussiaCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (China_RussiaCode))
        if i == 8:
            Czech_Republiclist = listOriginDictionary.get("Czech_Republic")
            for k, v in Czech_Republiclist.items():
                Czech_RepublicCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Czech_RepublicCode))
        if i == 9:
            Decentralized_International_Hacktivist_Grouplist = listOriginDictionary.get("Decentralized_International_Hacktivist_Group")
            for k, v in Decentralized_International_Hacktivist_Grouplist.items():
                Decentralized_International_Hacktivist_GroupCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (Decentralized_International_Hacktivist_GroupCode))


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
def writeAccuracy():

    if buttonClicks == 1:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("Prediction accuracy of target prediction page")

        popUpLabel.grid(row=0, column=0)

        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=20, width=20)
        dataSetDisplay.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        dataSetDisplay.insert(4.0, str(accuracy_score(y_test, y_pred)))

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
            tab3_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break

# Below is the creation of textbox entries; however am planning to make dummy number option a label option
def clear_display_result():
    tab3_display.delete(1.0, END)
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
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
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

l1 = Label(tab1, text='Please click the button below to scroll through the original dataset model.', padx=5, pady=5)
l1.grid(row=1, column=0)
l2 = Label(tab2, text='Please click the button below to see the prediction accuracy of the model in decimal ' +
                      'format.', padx=5, pady=5)
l2.grid(row=1, column=0)

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(tab3, text='Please enter six situational choices in the cells below, and then click the Prediction button'+
                      'to see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)

#--------------------- Dummy 1 Listbox and Textbox Attack Origin-------------------------------------------------------
#Listbox of Dummy Numbers
dummyOneListBox = Listbox(tab3) # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=2, column=0, padx=5, pady=5, ipadx=250, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listOriginDictionary:
    List1.insert(END, '{}: {}'.format(key, listOriginDictionary[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(tab3, height=2, width=50)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
#Listbox of Dummy Numbers
dummyTwoListBox = Listbox(tab3, height=2, width=50, yscrollcommand=SCROLL)
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
dummyNumberTwo = Text(tab3, height=2, width=50)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(tab3, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(tab3, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 5 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberFive = Text(tab3, height=2, width=50)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 6 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberSix = Text(tab3, height=2, width=50)
dummyNumberSix.bind("<Tab>", focus_next_widget)
dummyNumberSix.grid(row=7, column=1, columnspan=1, padx=5, pady=5)

#-------Tkinter Buttons------------------------------------------------------------------------------------------------

# Tab 2
# Accuracy Button
AccuracyButton = Button(tab3, text='Prediction Accuracy', command=writeAccuracy, width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=0, column=1, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

DummyOneButtonSubmit = Button(tab3, text="Submit Attack Origin", command=lambda: get_selDummyOne(), width=20, bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=3, column=0, padx=15, pady=15)

# List 2 Origin country/region choice button

DummyTwoButtonSubmit = Button(tab3, text="Submit Month", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple', fg='#fff')
DummyTwoButtonSubmit.grid(row=5, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab3, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=6, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab3, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=1, column=1, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab3, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=0, column=0, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab3, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=8, column=0, padx=5, pady=5)

#------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results
tab1_display = ScrolledText(tab1, height=20, width=50)
tab1_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

tab2_display = ScrolledText(tab2, height=1, width=20)
tab2_display.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Prediction results window in tab 3
tab3_display = Text(tab3, height=1)
tab3_display.grid(row=7, column=0, columnspan=1, padx=5, pady=5)

# Keep window alive
mainloop()

# reference for making scroll tab