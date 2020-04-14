import binascii
import pandas as pd
import numpy as np
import xlrd
import sys
import io

# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
hellobin = bin(int.from_bytes('hello'.encode(), 'big'))
print(hellobin)
# output is 0b110100001100101011011000110110001101111
print('\n')


# https://docs.python.org/3/library/binascii.html

crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))
# output is crc32 = 0x0d4a1185
print('\n')

# https://www.devdungeon.com/content/working-binary-data-python#format
# a_byte = b'Hello'  # 255
# i = ord(a_byte)
# bin = "{0:b}".format(i)
# print(bin)

# https://docs.python.org/3/library/io.html
openreadbytes = open("NumAsFloatsDataSet_ExpWithNames.xlsx", "rb", buffering=0) # opening excel file as bytes for reading (from string)
dfreadbytes = pd.DataFrame(openreadbytes) # creating dataframe in bytes

pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print(dfreadbytes) # printing dataframe in bytes

# output is:

#                                                    0
# 0   b'PK\x03\x04\x14\x00\x06\x00\x08\x00\x00\x00!\...
# 1   b'3\xe7\xc1\xf2N\xe9B\xab\x88?C%\xbd*\xe6\xaa\...
# 2   b'\xc3\xdax|`\xebG\x18\xba\x9d\xe3\xae\xb6u_\x...
# 3   b'\x96\xd1\x84g}M\x1b9\x82\x08Z\x11\t\xf4\xbb\...
# 4   b'v/s\xf0:$\xc7\x14\xf4\x9e\xa93<\xb0\x12\xde\...
# 5   b'V\xd1\xabQ\xba\x1ai\xdb\x7fH\xadN\xaa\xd2\xb...
# 6   b'\x0b\xf4\x05\xb1\xc2H\xb2\x90l\xba5\x91\xa5\...
# 7   b"\xe1\x85\x19'\xbd,\xf7\xe7\xad0\xe7\xba\xe3\...
# 8   b'\xdc\xd4Y\xe2\xd4\x85\xf0U\xe6\x8f\x08\r\x1d...
# 9   b'\x00\x00\xb8?\x00\x00\x18\x00\x00\x00xl/work...
# 10  b'\xfe\xf3\xef\xf5p\x11\x0cNM~\xd8\xe6\xbb\xea...
# 11  b'\xa7\x97\\\xd15Y\xec\x99lvI\xd6\xd2U\xdf}\x9...
# 12  b"\x8c\xd2\x82\x1c\xb6!\xe8\x86\x08\x80\xa0AH\...
# 13  b"\xfdtY\xa5\x18\x01\x18\xc4\x18u^=0\x19`\xb4\...
# 14  b'n\xee#\x82\xc9 \x0f\x94\x1dL\x8c\xf9\xda\xfb...
# 15  b'\xfd CA_\xe2\x00\x06\t\x8c\x16\x06o`\x98\xc0...
# 16  b'\xce\x18\xaf\xbcs\xc6\xdc\x18\x01\xfdt\x19\x...
# 17  b'\xfd\xd8|\x9a\x00\x0c\xd2\x18}\x81\xa8\xbb\x...
# 18  b"6\x8dA\xbb\x9d1\xfe4\x10S+\x06y\xba\x8c%\xb4...
# 19  b'\xc4\x0f\x94\x9c0\\\xd3\xe7\xb3\x18w\xf2t\xf...
# 20  b't\xcd`\x0e\xaf\x0f9\xacc\xd2]\xcf\x87,\x88/\...
# 21  b't\x08\x0c0F\xa3\x0f\xed\xd6\x15\xb2\x07F\x00...
# 22  b'\x0c\xe3\x0e\xfb\x1e]\xc46\x92Kr\xe8\xd2\xb9...
# 23  b'\x0c\x17\xdd\x82\x88\x15\xfe\\D\x9d\xabZl\xe...
# 24  b'0m\x15\x15x\xe5\xf6\xe0E\xbd\xe5\x87A\xdaA\x...
# 25  b'\xce\x99Fz\x933\xa9\x99\x01Pb/3 \x8ftS\xd9\x...
# 26  b'\xb5r\xb7[\x08j%e~\xa3Y\xa8\x07\x95J;\xa8\xb...
# 27  b'\x83\xd6\xf3\xa8\xf1\x1c[\x082\xb7\xe5\x14\x...
# 28  b'x\xebV\xfd\xce\xee\xa5\xb6&R|\x1a\xbf3W\x16\...
# 29  b']7\xcc\x07(\x9a\xa4\x825P\xaeX\x0b\xbd\xa3\x...
# 30  b'\xab\xf2\x95\xb1W\xf9:\xad\xa7\xf2E\xf0\xfe\...
# 31                            b'\x88\x02\xa2\x80( \n'
# 32                            b'\x88\x02\xa2\x80( \n'
# 33                            b'\x88\x02\xa2\x80( \n'
# 34  b"\xcc\xa2\xc0-\x00\x00\x00\xff\xff\x03\x00PK\...
# 35  b"\xe51\xa17!\xa5!\x99\x17d\xc1\xe2+F\x93\xf7\...
# 36  b'\x00\x00xl/_rels/workbook.xml.relsPK\x01\x02...
# 37  b"\x00\x00\xb8?\x00\x00\x18\x00\x00\x00\x00\x0...

print('\n')

# https://kite.com/python/answers/how-to-convert-a-pandas-dataframe-column-of-strings-to-floats-in-python
#dfExpWithNames = xlrd.open_workbook("NumAsFloatsDataSet_ExpWithNames.xlsx")
# Creating variable to convert excel file to a dataframe (using pandas)
#sheets = dfExpWithNames.sheets()
#for sheet in sheets:
#    ExpWithNamesData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])
#dfReadData = pd.DataFrame(ExpWithNamesData)
#dfreadfloat = ExpWithNamesData["A"] = pd.to_numeric(df["A"], downcast="float")
#print(dfreadfloat)
#print('\n')


# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
helloIntFromBytes = int.from_bytes(b'hello', byteorder=sys.byteorder)  # creating an int from bytes
helloAsBinary = bin(int.from_bytes(b'hello', byteorder=sys.byteorder))
print(helloIntFromBytes)
# output is 478560413032
print(helloAsBinary)
# output is 0b110111101101100011011000110010101101000

helloAsStringFromBytes = ascii(helloIntFromBytes)
print(helloAsStringFromBytes)
# output is 478560413032

bit32CheckSum = binascii.crc32(b"hello world")
print(bit32CheckSum)
# output is 222957957

# https://www.datacamp.com/community/tutorials/python-data-type-conversion
print(int(helloAsBinary, 2)) # base 2 binary
# output is 478560413032
print(helloAsBinary) # binary
# output is 0b110111101101100011011000110010101101000

print('\n\n')

# https://kite.com/python/answers/how-to-convert-binary-to-string-in-python

a_binary_string_for_hello = "01101000 01100101 01101100 01101100 01101111"
binary_values = a_binary_string_for_hello.split()
print(binary_values)
# output is ['01101000', '01100101', '01101100', '01101100', '01101111']

ascii_string = ''
for binary_value in binary_values:
    an_integer = int(binary_value, 2)
    print(an_integer)

    ascii_character = chr(an_integer)
    ascii_string += ascii_character
    print(ascii_string)
    print(ascii_character)
    # output is:
    # 104
    # h
    # h
    # 101
    # he
    # e
    # 108
    # hel
    # l
    # 108
    # hell
    # l
    # 111
    # hello
    # o

print(ascii_string)
# output is hello

print('\n\n')
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
helloIntFromBytes = int.from_bytes(b'hello', byteorder=sys.byteorder)  # creating an int from bytes
helloAsBinary = bin(int.from_bytes(b'hello', byteorder=sys.byteorder))
print('hello as int from bytes: ', helloIntFromBytes)
# output is 478560413032
print('hello as binary from bytes: ', helloAsBinary)
# output is 0b110111101101100011011000110010101101000

# https://www.tutorialspoint.com/python_text_processing/python_conversion_binary_ascii.htm
text = b"Simply Easy Learning"

# Converting binary to ascii
data_b2a = binascii.b2a_uu(text)
print("**Binary to Ascii** \n")
print(data_b2a)

# Converting back from ascii to binary
data_a2b = binascii.a2b_uu(data_b2a)
print("**Ascii to Binary** \n")
print(data_a2b)

# output is:
# **Binary to Ascii**
#
# b'44VEM<&QY($5A<WD@3&5A<FYI;F< \n'
# **Ascii to Binary**
#
# b'Simply Easy Learning'

updatedhello = int.to_bytes(helloIntFromBytes, length=5, byteorder=sys.byteorder)
print(updatedhello)
updatedhelloascii = ascii(updatedhello)
print(updatedhelloascii)

# output is:
# b'hello\x00\x00\x00\x00\x00\x00\x00'
# b'hello\x00\x00\x00\x00\x00\x00\x00'


