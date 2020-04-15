# A page created to reference string and float comparisons
import binascii
import sys
import pandas as pd


#----------------------------------Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

locationDict = {"country1":{"name" : "China", "binary": 418464229443},
                "country2":{"name":"USA","binary" : 4281173},
                "country3":{"name":"Russia","binary" : 107105536406866},

                "region1":{"name":"Asia","binary" : 1634300737},
                "region2":{"name":"Europe","binary" : 111533580514629},}


pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print('\n\n')
print(pdDict)


#---------------------------------------------Countries------------------------------------------------------------
# China
print('\n\n')
ChinaBytes = int.from_bytes(b'China', byteorder=sys.byteorder)  # creating an int from bytes
print(ChinaBytes)
ChinaAscii = int.to_bytes(ChinaBytes, length=20, byteorder=sys.byteorder)
print(ChinaAscii)

# output is:
# 418464229443
# b'China\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
USABytes = int.from_bytes(b'USA', byteorder=sys.byteorder)  # creating an int from bytes
print(USABytes)
USAAscii = int.to_bytes(USABytes, length=30, byteorder=sys.byteorder)
print(USAAscii)

# output is:
# 4281173
# b'USA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Russia
print('\n\n')
RussiaBytes = int.from_bytes(b'Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(RussiaBytes)
RussiaAscii = int.to_bytes(RussiaBytes, length=30, byteorder=sys.byteorder)
print(RussiaAscii)

# output is:
# 107105536406866
# b'Russia\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# -------------------------------- Regions----------------------------------------------------------------------------

# Asia
print('\n\n')
AsiaBytes = int.from_bytes(b'Asia', byteorder=sys.byteorder)  # creating an int from bytes
print(AsiaBytes)
AsiaAscii = int.to_bytes(AsiaBytes, length=20, byteorder=sys.byteorder)
print(AsiaAscii)

# output is:
# 1634300737
# b'Asia\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# Europe
print('\n\n')
EuropeBytes = int.from_bytes(b'Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(EuropeBytes)
EuropeAscii = int.to_bytes(EuropeBytes, length=20, byteorder=sys.byteorder)
print(EuropeAscii)

# output is:
# 111533580514629
# b'Europe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
