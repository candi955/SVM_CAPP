# A page created to reference string and float comparisons
import binascii
import sys



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