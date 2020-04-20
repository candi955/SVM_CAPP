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
cyberExcel = xlrd.open_workbook('SVMCAPPdataset8Apr2020_TargetOnly_19Apr2020_1048pm_fakeDummyNums.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
    cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

    cyberDF = pd.DataFrame(cyberSheetData)
    pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    print("\n" + "Original excel dataframe: \n")
    print(cyberDF)

    # Columns in 'object' format
    print("\n\n")
    print(cyberDF.dtypes)

    np.set_printoptions(precision=True, suppress=None)

    cyberDF[0] = pd.to_numeric(cyberDF[0], errors='coerce', downcast='integer')
    cyberDF[1] = pd.to_numeric(cyberDF[1], errors='coerce', downcast='integer')
    cyberDF[2] = pd.to_numeric(cyberDF[2], errors='coerce', downcast='integer')
    cyberDF[3] = pd.to_numeric(cyberDF[3], errors='coerce', downcast='integer')
    cyberDF[4] = pd.to_numeric(cyberDF[4], errors='coerce', downcast='integer')
    cyberDF[5] = pd.to_numeric(cyberDF[5], errors='coerce', downcast='integer')
    cyberDF[6] = pd.to_numeric(cyberDF[6], errors='coerce', downcast='integer')

    # reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html
    cyberDF[0] = np.array(cyberDF[0])#pd.to_numeric(cyberDF[0], errors='coerce', downcast='integer')
    cyberDF[1] = np.array(cyberDF[1])#pd.to_numeric(cyberDF[1], errors='coerce', downcast='integer')
    cyberDF[2] = np.array(cyberDF[2])#pd.to_numeric(cyberDF[2], errors='coerce', downcast='integer')
    cyberDF[3] = np.array(cyberDF[3])#pd.to_numeric(cyberDF[3], errors='coerce', downcast='integer')
    cyberDF[4] = np.array(cyberDF[4])#pd.to_numeric(cyberDF[4], errors='coerce', downcast='integer')
    cyberDF[5] = np.array(cyberDF[5])#pd.to_numeric(cyberDF[5], errors='coerce', downcast='integer')
    cyberDF[6] = np.array(cyberDF[6])#pd.to_numeric(cyberDF[6], errors='coerce', downcast='integer')


    # Successfully turned columns into 'float64' format
    print("\n\nUpdated cyberDF datatype:\n")
    print(cyberDF.dtypes)
    print("\n\n")
    cyberDFDataFrame = pd.DataFrame(cyberDF)
    pd.set_option('display.max_rows', 1000)  # Attempting to display all rows and columns
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 1000)
    print("Full cyberDF dataframe:\n")
    print(cyberDFDataFrame)
    print("\n\n")

# -------------------------------------------------------------------------------------------------------------------

    # Writing updated file back into project folder

    writer = pd.ExcelWriter(r'c:\Users\Hachidori\PycharmProjects\SVM_CAPP_GSIP_2nd\venv\Targetoutput.xlsx')
    # This method will truncate the data past the first decimal point
    cyberDF.to_excel(writer, 'Sheet1', float_format="%0.5f")
    writer.save()

    # pulling excel file and creating variable
    cyberExcelTwo = xlrd.open_workbook('Targetoutput.xlsx')
    # Creating variable to convert excel file to a dataframe (using pandas)
    sheets2 = cyberExcelTwo.sheets()
    for sheet in sheets2:
        cyberSheetDataAgain = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

        cyberDFAgain = pd.DataFrame(cyberSheetDataAgain)
        print("\n\nCyberDFAgain dtypes after file re-written and pulled:\n\n")
        print(cyberDFAgain.dtypes)
        print("\n\n")


        # reference for suppressing scientific notation
        # https://re-thought.com/how-to-suppress-scientific-notation-in-pandas/

# -------Finished writing and reading file, still doesn't want to read it as float--------------------------------------

        # Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
        # will only show the last column in the target data
        # iloc[row slicing, column slicing]
        # sources if first row (header) removed, then rows 0-5 included (off with row 6)
        # target is first row(header) removed, then column 6 only included
        sources = cyberDF.iloc[1:, :6]
        target = cyberDF.iloc[1:,6:]
        #sources = cyberDF[:, :-1]
        #target = cyberDF[:, len(cyberDF[0]) - 1]

        print('\n\nSources:\n\n')
        print(sources)
        print('\n\nTarget:\n\n')
        print(target)

        # Deleting header column from dataframe, both source and target data
        #sourceNoHeader = np.delete(sources, (0), axis=0)
        #targetNoHeader = np.delete(target, (0), axis=0)

        print('\n\nSources without header and datatype:\n\n')
        #print(sourceNoHeader)
        #print(type(sourceNoHeader))
        print('\n\nTarget without header and datatype:\n\n')
        #print(targetNoHeader)
        #print(type(targetNoHeader))
         # Will attempt to turn excel numbers into floats
        # https: // stackoverflow.com / questions / 44423036 / pandas - to - excel - float - format

        # https://stackoverflow.com/questions/51068361/setting-default-number-format-when-writing-to-excel-from-pandas
        # https://datascience.stackexchange.com/questions/48049/valueerror-could-not-convert-string-to-float


        X = sources
        y = target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

        model = svm.SVC(kernel='linear')
        model.fit(X_train, y_train.ravel())
        y_pred = model.predict(X_test)

        print("\n\nHere is the predication accuracy (y prediction): \n")
        print(y_pred)
        print("\n\n")

        knn = KNeighborsClassifier(n_neighbors=1)
        knn.fit(X, y)


dummyTextOne = input("Enter Dummy 1: ")
dummyTextTwo = input("Enter Dummy 2: ")
dummyTextThree = input("Enter Dummy 3: ")
dummyTextFour = input("Enter Dummy 4: ")
dummyTextFive = input("Enter Dummy 5: ")
dummyTextSix = input("Enter Dummy 6: ")

def finalPrediction():

    while True:
        try:

            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyTextOne, dummyTextTwo, dummyTextThree,
                          dummyTextFour, dummyTextFive])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            print(prediction)
        except ValueError:
            print('Error')

        else:
            break


main()


# Error output:

# Traceback (most recent call last):
#   File "C:/Users/Hachidori/PycharmProjects/SVM_CAPP_GSIP_2nd/venv/SVMPracticePage.py", line 106, in <module>
#     model.fit(X_train, y_train.ravel())
#   File "C:\Users\Hachidori\AnacondaOriginalDownload\AnacondaDownload1Aug2019\lib\site-packages\sklearn\svm\base.py", line 146, in fit
#     accept_large_sparse=False)
#   File "C:\Users\Hachidori\AnacondaOriginalDownload\AnacondaDownload1Aug2019\lib\site-packages\sklearn\utils\validation.py", line 719, in check_X_y
#     estimator=estimator)
#   File "C:\Users\Hachidori\AnacondaOriginalDownload\AnacondaDownload1Aug2019\lib\site-packages\sklearn\utils\validation.py", line 496, in check_array
#     array = np.asarray(array, dtype=dtype, order=order)
#   File "C:\Users\Hachidori\AnacondaOriginalDownload\AnacondaDownload1Aug2019\lib\site-packages\numpy\core\numeric.py", line 538, in asarray
#     return array(a, dtype, copy=False, order=order)
# ValueError: could not convert string to float: