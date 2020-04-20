# List 1 Dictionary page of Months

import pandas as pd


#------------ListBox Country/Region/binary Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate months with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp


listMonthDictionary = {"January":{"binary": 34184235089551690}, # list option 0
                "February":{"binary": 8751164182992414022}, # list option 1
                "March":{"binary": 448345039181}, # list option 2
                "April":{"binary": 465625575489}, # list option 3
                "May":{"binary": 7954765}, # list option 4
                "June":{"binary": 1701737802}, # list option 5
                "July":{"binary": 2037151050}, # list option 6
                "August":{"binary": 128039239775553}, # list option 7
                "September":{"binary": 2110234346230949897555}, # list option 8
                "October":{"binary": 32199620796113743}, # list option 9
                "November":{"binary": 8243102914964778830},
                "December":{"binary": 8243102914963531076},
                "Unlisted":{"binary": 7234316415479344725}}


pdDictMonthList = pd.DataFrame(listMonthDictionary)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print("\nList 1 Dictionary of Origin countries: \n")
print(listMonthDictionary)
print("\n\n")

print("In excel format: \n")
print(pdDictMonthList)

# ----- output of program---------------------------------------------------------------------------------------------

# List 1 Dictionary of Months
#
# List 1 Dictionary of Origin countries:
#
# {'January': {'binary': 34184235089551690}, 'February': {'binary': 8751164182992414022}, 'March': {'binary': 448345039181}, 'April': {'binary': 465625575489}, 'May': {'binary': 7954765}, 'June': {'binary': 1701737802}, 'July': {'binary': 2037151050}, 'August': {'binary': 128039239775553}, 'September': {'binary': 2110234346230949897555}, 'October': {'binary': 32199620796113743}, 'November': {'binary': 8243102914964778830}, 'December': {'binary': 8243102914963531076}, 'Unlisted': {'binary': 7234316415479344725}}
#
#
#
# In excel format:
#
#                   January             February         March         April      May        June        July           August               September            October             November             December             Unlisted
# binary  34184235089551690  8751164182992414022  448345039181  465625575489  7954765  1701737802  2037151050  128039239775553  2110234346230949897555  32199620796113743  8243102914964778830  8243102914963531076  7234316415479344725
#
# Process finished with exit code 0