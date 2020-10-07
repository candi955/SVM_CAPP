# White Ball 1 prediction page
# reference: https://stackoverflow.com/questions/40526496/vertical-scrollbar-for-frame-in-tkinter-python

# ---------Imports----------------------------------------------------------------------------------------------------
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

# ------------ListBox Country/Region/Code Dictionaries--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated Code
# reference: https://www.w3schools.com/python/python_dictionaries.asp

# List 1 (Target country/region)
listWhiteBall1 = {"Sunday": {"Code": 1},
                        "Monday": {"Code": 2},
                        "Tuesday": {"Code": 3},
                        "Wednesday": {"Code": 4},
                        "Thursday": {"Code": 5},
                        "Friday": {"Code": 6},
                        "Saturday": {"Code": 7}}



# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictOne = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# List 2 (Month of attack in Code numbers)

listMonthDictionary = {"January": {"code": 1},  # list option 0
                       "February": {"Code": 2},  # list option 1
                       "March": {"Code": 3},  # list option 2
                       "April": {"Code": 4},  # list option 3
                       "May": {"Code": 5},  # list option 4
                       "June": {"Code": 6},  # list option 5
                       "July": {"Code": 7},  # list option 6
                       "August": {"Code": 8},  # list option 7
                       "September": {"Code": 9},  # list option 8
                       "October": {"Code": 10},  # list option 9
                       "November": {"Code": 11},  # list option 10
                       "December": {"Code": 12}}  # list option 11


# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictTwo = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
whiteBall1Excel = xlrd.open_workbook('WhiteBall1Pred.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = whiteBall1Excel.sheets()
for sheet in sheets:
    whiteBall1SheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

    # Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
    # will only show the last column in the target data
    sources = whiteBall1SheetData[:, :-1]
    target = whiteBall1SheetData[:, len(whiteBall1SheetData[0]) - 1]

    # Deleting header column from dataframe, both source and target data
    sourceNoHeader = np.delete(sources, (0), axis=0)
    targetNoHeader = np.delete(target, (0), axis=0)

    X = sourceNoHeader
    y = targetNoHeader

    print(X)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

    model = svm.SVC(kernel='linear')
    model.fit(X_train, y_train.ravel())
    y_pred = model.predict(X_test)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)


# ---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
# List 1 function to place list and then transfer answer to textbox, for White Ball 1 choice
def get_selDummyOneTarget():
    for i in List1.curselection():
        if i == 0:
            Sundaylist = listSunday.get("Sunday")
            for k, v in listSunday.items():
                SundayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (SundayCode))
        if i == 1:
            MondayList = listMonday.get("Monday")
            for k, v in listMonday.items():
                MondayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (MondayCode))
        if i == 2:
            Tuesdaylist = listTuesday.get("Tuesday")
            for k, v in Tuesdaylist.items():
                TuesdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (TuesdayCode))
        if i == 3:
            Wednesdaylist = listWednesday.get("Wednesday")
            for k, v in Wednesdaylist.items():
                WednesdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (WednesdayCode))
        if i == 4:
            Thursdaylist = listThursday.get("Thursday")
            for k, v in Thursdaylist.items():
                ThursdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (ThursdayCode))
        if i == 5:
            Fridaylist = listFriday.get("Friday")
            for k, v in Fridaylist.items():
                FridayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (FridayCode))
        if i == 6:
            Saturdaylist = listSaturday.get("Saturday")
            for k, v in Saturdaylist.items():
                SaturdayCode = "{}".format(v)
                dummyNumberOne.insert(1.0, (SaturdayCode))




# the accuracy score method
def writeAccuracy(buttonClicks):
    if buttonClicks == 1:
        # Creating pop up window for dataset
        # reference: https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
        win = tk.Toplevel()
        win.wm_title("White Ball 1 prediction page")

        popUpLabel = tk.Label(win,
                              text="Please see the accuracy percentage of the WhiteBall 1 Prediction algorithm below:\n")
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
    return ("break")


# ---- Creating functions to run the main prediction program ----------------------------------------------------------

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


            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = float(dummyTextOne)
            dummyValues.dummyTextTwo = float(dummyTextTwo)
            dummyValues.dummyTextThree = float(dummyTextThree)
            dummyValues.dummyTextFour = float(dummyTextFour)


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
            # calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            frame_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break


# Below is the creation of textbox entries; however am planning to make dummy number option a label option
def clear_display_result():
    frame_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)

    # when boxes are cleared, bringing the option focus for the user back to the initial textbox
    dummyNumberOne.focus()


def mainMenu():
    while True:
        try:

            # Creating a messagebox for when the user clicks to exit the program, with exception prevention
            if mbox.askokcancel("Quit", "Do you want to quit?"):
                # root.destroy()
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


# ----- Creating Tkinter Setup (root) for GUI #-----


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(yscrollcommand=yscrollbar.set, scrollregion=canvas.bbox(ALL))


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


root = tk.Tk()
root.title('White Ball 1 Prediction Page')

# --- create canvas with scrollbar ---

canvas = ResizingCanvas(root, width=650, height=590, bg="black", highlightthickness=0)
canvas.pack(fill=BOTH, expand=YES)

yscrollbar = tk.Scrollbar(root, command=canvas.yview, orient="vertical")
yscrollbar.pack(side=tk.LEFT, fill=tk.Y)

# update scrollregion after starting 'mainloop'
# when all widgets are in canvas
canvas.bind('<Configure>', on_configure)

# --- put frame in canvas ---

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

# --- add widgets in frame ---
# ------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(frame, text='Please enter choices in the cells below, and then click the Prediction button ' +
                       'to see your prediction results:', padx=5, pady=5)
l3.grid(row=0, column=0)

# Label year
labelTarget = Label(frame, text="Choose and submit the projected weekday:")
labelTarget.grid(row=2, column=0)

labelMonth = Label(frame, text="Choose and submit the projected month:")
labelMonth.grid(row=6, column=0)

labelYear = Label(frame, text="Enter the day of the month:")
labelYear.grid(row=10, column=0)

labelGrossPSD = Label(frame, text="Enter the year projected event in format 'YYYY':")
labelGrossPSD.grid(row=12, column=0)



predictionLabel = Label(frame, text="Prediction results White Ball 1:")
predictionLabel.grid(row=20, column=0)
# --------------------- Dummy 1 Listbox and Textbox White Ball 1-------------------------------------------------------
# Listbox of Dummy Numbers
dummyOneListBox = Listbox(frame)  # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget)  # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=3, column=0, padx=5, pady=5, ipadx=250, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listWhiteBall1:
    List1.insert(END, '{}: {}'.format(key, listWhiteBall1[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(frame, height=2, width=50)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
# Listbox of Dummy Numbers
dummyTwoListBox = Listbox(frame, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget)  # for user to tab between listboxes/textboxes
dummyTwoListBox.grid(row=7, column=0, columnspan=1, padx=5, pady=5, ipadx=250, ipady=0)

List2 = Listbox(dummyTwoListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listMonthDictionary:
    List2.insert(END, '{}: {}'.format(key, listMonthDictionary[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = Text(frame, height=2, width=50)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=9, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(frame, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=11, column=0, columnspan=1, padx=5, pady=5)

# --------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(frame, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=13, column=0, columnspan=1, padx=5, pady=5)



# -------Tkinter Buttons------------------------------------------------------------------------------------------------

# Tab 2
# Accuracy Button
AccuracyButton = Button(frame, text='Prediction Accuracy', command=lambda: writeAccuracy(1), width=20, bg='purple',
                        fg='#fff')
AccuracyButton.grid(row=19, column=0, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

# List 1 White Ball 1  choice buttons
DummyOneButtonSubmit = Button(frame, text="Submit Day of Week", command=lambda: get_selDummyOneTarget(), width=20,
                              bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=4, column=0, padx=15, pady=15)

# List 2 White Ball 1  choice button
DummyTwoButtonSubmit = Button(frame, text="Submit Month", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple',
                              fg='#fff')
DummyTwoButtonSubmit.grid(row=8, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(frame, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=18, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(frame, text='Clear results and start over', command=clear_display_result, width=25,
                             bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=22, column=0, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(frame, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=23, column=0, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(frame, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=24, column=0, padx=5, pady=5)

# ------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results

# Prediction results window in tab 3
frame_display = Text(frame, height=1)
frame_display.grid(row=21, column=0, columnspan=1, padx=5, pady=5)

# --- start program ---

root.mainloop()