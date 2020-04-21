# Main program page

# reference: https://stackoverflow.com/questions/40526496/vertical-scrollbar-for-frame-in-tkinter-python

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


# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('FullDataSetForMainMenu_CleanedUp_20Apr2020_2439pm.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
   cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth',23)

# creating dataframe for tkinter
df = pd.DataFrame(cyberSheetData)

#-----Tkinter functions----------------------------------------------------------------------------

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

#----- Creating Tkinter Setup (root) for GUI #-----


root = tk.Tk()
root.title('SVM CAPP Main Menu')

# --- create canvas with scrollbar ---

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# --- program functions ---
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


# --- add widgets in frame ---

labelOne = tk.Label(frame, text='Please click on one of the following program choices:', padx=5, pady=5, font="-size 10")
labelOne.pack()

TargetPageButton = tk.Button(frame, text='Prediction of Attack Target', command=lambda: onButtonClick(1),
                             height=2, width=30, bg='purple', fg='#fff')
TargetPageButton.pack()

OriginPageButton = tk.Button(frame, text='Prediction of Attack Origin', command= lambda: onButtonClick(2),
                             height=2, width=30, bg='purple', fg='#fff')
OriginPageButton.pack()

DataSetPageButton = tk.Button(frame, text='Original dataset', command= lambda: onButtonClick(3),
                             height=2, width=30, bg='blue', fg='#fff')
DataSetPageButton.pack()

ExitButton = tk.Button(frame, text='Exit program',
                          command=lambda: onButtonClick(4), height=2, width=30, bg='green', fg='#fff')
ExitButton.pack()

# --- start program ---

root.mainloop()