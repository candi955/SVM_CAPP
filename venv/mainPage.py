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

#-----Creating Tkinter Setup (root) for GUI----------------------------------------------------------------------------
root = tk.Tk()
root.title('SVM Prediction: Global attack by location (country)')
root.geometry("500x500")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')
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
        mbox.showinfo("Click 1")
    if buttonClicks == 3:
        mbox.showinfo("Click 2")
        import LocationTarget

def exitProgram():
    exit()

def flush(self):
    pass

#------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

l1 = Label(page1, text='Please click on one of the following choices.', padx=5, pady=5)
l1.grid(row=1, column=0)


#-------Tkinter Buttons------------------------------------------------------------------------------------------------


TargetPageButton = tk.Button(root, text='Click for prediction of Attack Target', command=lambda: onButtonClick(1), height=2, width=30, bg='purple', fg='#fff')
TargetPageButton.config(padx=5, pady=5)
TargetPageButton.pack()

b2 = tk.Button(root, text="Page 2", command= lambda: onButtonClick(2), width=12, bg='purple', fg='#fff')
b2.pack()

b3 = Button(root, text="Page 3", command= lambda: onButtonClick(3), width=12, bg='purple', fg='#fff')
b3.pack()

mainloop()







#Tab 1
# Dataset Button
datasetButton = Button(tab1, text='Click for prediction of Attack Target', command=locationTargetPageChoice(), width=12, bg='purple', fg='#fff')
datasetButton.grid(row=1, column=0, padx=15, pady=15)
datasetButton.pack()

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab_control, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=2, column=0, padx=5, pady=5)


# Keep window alive
mainloop()