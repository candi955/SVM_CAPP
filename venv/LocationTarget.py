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

#------------ListBox Country/Region/binary Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

locationDict = {"China":{"binary": 418464229443},
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}}


pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('NumAsFloatsDataSet_ExpWithNames_Binary.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
   cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# creating dataframe for tkinter
df = pd.DataFrame(cyberSheetData)

# Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
# will only show the last column in the target data
sources = cyberSheetData[:, :-2]
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
root.title('SVM Prediction: Global attack by location (country)')
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
listbox.pack()

#---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
def get_selDummyOne():

    for i in List1.curselection():
        if i == 0:
            Chinalist = locationDict.get("China")
            for k, v in Chinalist.items():
                ChinaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (ChinaBinary))

def change_opt():
    entry = E.get()
    change = entry.split(" ")
    print("Change")
    listbox.insert(int(change[0]),change[1])
    root.update()

# the dataframe method, tab 1
def writeDataset():
    tab1_display.insert(1.0, pd.DataFrame(df))

# the accuracy score method, tab 2
def writeAccuracy():
    tab2_display.insert(4.0, str(accuracy_score(y_test, y_pred)))

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
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive])

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
l3 = Label(tab3, text='Please enter five dummy numbers in the cells below,\n and then click the Prediction button to ' +
                      'see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)

#--------------------- Dummy 1 Listbox and Textbox ---------------------------------------------------------------------
#Listbox of Dummy Numbers
dummyOneListBox = Listbox(tab3) # height=1, width=50, yscrollcommand=TRUE)

# the next piece of code is calling from the focus_next_widget method so that the user can tab from textbox to textbox,
# rather than clicking
dummyOneListBox.bind("<Tab>", focus_next_widget)
dummyOneListBox.grid(row=2, column=0, columnspan=1, padx=5, pady=5, ipadx=86, ipady=1)


List1 = Listbox(dummyOneListBox)
for key in locationDict:
    List1.insert(END, '{}: {}'.format(key, locationDict[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = ScrolledText(tab3, height=2, width=50)
# the next piece of code is calling from the focus_next_widget method so that the user can tab from textbox to textbox,
# rather than clicking
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=2, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 2 Listbox and Textbox ---------------------------------------------------------------------
#Listbox of Dummy Numbers
dummyTwoListBox = Listbox(tab3, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget)
dummyTwoListBox.grid(row=3, column=0, columnspan=1, padx=5, pady=5, ipadx=86, ipady=10)

List2 = Listbox(dummyTwoListBox)

# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in locationDict:
    List2.insert(END, '{}: {}'.format(key, locationDict[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = ScrolledText(tab3, height=2, width=50)
# the next piece of code is calling from the focus_next_widget method so that the user can tab from textbox to textbox,
# rather than clicking
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=2, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 3 Listbox and Textbox ---------------------------------------------------------------------

dummyThreeListBox = Listbox(tab3, height=2, width=50)
dummyThreeListBox.bind("<Tab>", focus_next_widget)
dummyThreeListBox.grid(row=4, column=0, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 4 Listbox and Textbox ---------------------------------------------------------------------

dummyFourListBox = Listbox(tab3, height=2, width=50)
dummyFourListBox.bind("<Tab>", focus_next_widget)
dummyFourListBox.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 5 Listbox and Textbox ---------------------------------------------------------------------

dummyFiveListBox = Listbox(tab3, height=2, width=50)
dummyFiveListBox.bind("<Tab>", focus_next_widget)
dummyFiveListBox.grid(row=6, column=0, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 6 Listbox and Textbox ---------------------------------------------------------------------

dummySixListBox = Listbox(tab3, height=2, width=50)
dummySixListBox.bind("<Tab>", focus_next_widget)
dummySixListBox.grid(row=7, column=0, columnspan=1, padx=5, pady=5)

#-------Tkinter Buttons------------------------------------------------------------------------------------------------
#Tab 1
# Dataset Button
datasetButton = Button(tab1, text='Dataset', command=writeDataset, width=12, bg='purple', fg='#fff')
datasetButton.grid(row=3, column=0, padx=15, pady=15)

# Tab 2
# Accuracy Button
AccuracyButton = Button(tab2, text='Prediction Accuracy', command=writeAccuracy, width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=15, column=0, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

DummyOneButtonChange = Button(tab3, text="Change", command = change_opt, width=20, bg='purple', fg='#fff')
DummyOneButtonChange.grid(row=1, column=4, padx=15, pady=15)
DummyOneButtonSubmit = Button(tab3, text="Submit", command=lambda: get_selDummyOne(), width=20, bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=2, column=4, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab3, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='purple', fg='#fff')
PredictionButton.grid(row=9, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab3, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=9, column=2, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=3, column=3, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=4, column=3, padx=5, pady=5)

#------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results
tab1_display = ScrolledText(tab1, height=20, width=50)
tab1_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

tab2_display = ScrolledText(tab2, height=1, width=20)
tab2_display.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

tab3_display = ScrolledText(tab3, height=1)
tab3_display.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Keep window alive
mainloop()