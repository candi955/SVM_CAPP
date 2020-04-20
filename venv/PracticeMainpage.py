# Practice page for creating a main menu which would successfully bring up other pages in the program.

# reference: https://www.youtube.com/watch?reload=9&v=l4E1ntsk7rw
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

root = tk.Tk()
root.title("Practice attempt main window")
root.geometry("500x500")
frame1 = ttk.Frame(root)

def onclick(args):
    if args == 1:
        mbox.showinfo("click!")
    if args == 2:
        mbox.showinfo("Click 1")
    if args == 3:
        mbox.showinfo("Click 2")
        import LocationTarget


b1 = tk.Button(root, text="Click here", command=lambda: onclick(1), width=12, bg='purple', fg='#fff')
b1.pack()

b2 = tk.Button(root, text="Target Page", command= lambda: onclick(2), width=12, bg='purple', fg='#fff')
b2.pack()

b3 = Button(root, text="Origin Page", command= lambda: onclick(3), width=12, bg='purple', fg='#fff')
b3.pack()

mainloop()