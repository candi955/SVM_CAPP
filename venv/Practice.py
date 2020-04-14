import binascii
import pandas as pd
import numpy as np
import xlrd
import sys

# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
hellobin = bin(int.from_bytes('hello'.encode(), 'big'))
print(hellobin)
print('\n')


# https://docs.python.org/3/library/binascii.html

crc = binascii.crc32(b"hello")
crc = binascii.crc32(b" world", crc)
print('crc32 = {:#010x}'.format(crc))
print('\n')

# https://www.devdungeon.com/content/working-binary-data-python#format
# a_byte = b'Hello'  # 255
# i = ord(a_byte)
# bin = "{0:b}".format(i)
# print(bin)

# https://docs.python.org/3/library/io.html
f = open("NumAsFloatsDataSet_ExpWithNames_Binary.xlsx", "rb", buffering=0)
# creating dataframe
df = pd.DataFrame(f)
print(df)
print('\n')

# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
what = int.from_bytes(b'hello', byteorder=sys.byteorder)  # creating an int from bytes
again = bin(int.from_bytes(b'hello', byteorder=sys.byteorder))
print(what)
print(again)

print('\n')

# https://docs.python.org/3/library/io.html
# https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

