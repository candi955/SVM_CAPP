# Mainpage

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

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('SVMCAPPdataset8Apr2020_DataSetWindow_19Apr2020_1013pm_fakeDummyNums.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
   cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 40)

# creating dataframe for tkinter
df = pd.DataFrame(cyberSheetData)

#-----Creating Tkinter Setup (root) for GUI----------------------------------------------------------------------------
root = tk.Tk()
root.title('SVM Cyber Attack Prediction Program')
root.geometry("375x200")
style = ttk.Style(root)


# Tabs and Frames
page1 = ttk.Notebook(root)


#---Creating Tkinter functions----------------------------------------------------------------------------------------

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def onButtonClick(buttonClicks):
    if buttonClicks == 1:
        import LocationTarget
    if buttonClicks == 2:
        import LocationOrigin
    if buttonClicks == 3:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("Full Cyber event Dataset used for prediction algorithm")

        popUpLabel = tk.Label(win, text="Dataset created by program authors utilizing the CSIS Significant Cyber " +
                                        "Incidents and The World Bank DataBank websites:\n\n" +
                                        "https://csis-prod.s3.amazonaws.com/s3fs-public/200306_Significant_Cyber_Events_List.pdf?qRZXF65CUUOKTOl9rLVBMJhXfXtmJZMj\n" +
                                        "https://databank.worldbank.org/home.aspx\n\n")
        popUpLabel.grid(row=0, column=0)

        # Display Boxes for Results
        dataSetDisplay = ScrolledText(win, height=35, width=150)
        dataSetDisplay.grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        dataSetDisplay.insert(1.0, pd.DataFrame(df))

    if buttonClicks == 4:
        exit()

def flush(self):
    pass

#------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

l1 = Label(page1, text='Please click on one of the following choices.', padx=5, pady=5)
l1.grid(row=1, column=0)


#-------Tkinter Buttons------------------------------------------------------------------------------------------------


TargetPageButton = tk.Button(root, text='Click for prediction of Attack Target', command=lambda: onButtonClick(1),
                             height=2, width=30, bg='purple', fg='#fff')

TargetPageButton.pack()

OriginPageButton = tk.Button(root, text='Click for prediction of Attack Origin', command= lambda: onButtonClick(2),
                             height=2, width=30, bg='purple', fg='#fff')
OriginPageButton.pack()

DataSetPageButton = tk.Button(root, text='Click to see original dataset', command= lambda: onButtonClick(3),
                             height=2, width=30, bg='blue', fg='#fff')
DataSetPageButton.pack()

ExitButton = tk.Button(root, text='Click here to exit the program',
                          command=lambda: onButtonClick(4), height=2, width=30, bg='green', fg='#fff')
ExitButton.pack()

root.mainloop()






