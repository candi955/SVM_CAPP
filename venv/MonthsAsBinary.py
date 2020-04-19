# Months listed as binary

import binascii
import sys
import io


print('\n\n')
JanuaryBytes = int.from_bytes(b'January', byteorder=sys.byteorder)  # creating an int from bytes
print(JanuaryBytes)
JanuaryAscii = int.to_bytes(JanuaryBytes, length=7, byteorder=sys.byteorder)
print(JanuaryAscii)


print('\n\n')
FebruaryBytes = int.from_bytes(b'February', byteorder=sys.byteorder)  # creating an int from bytes
print(FebruaryBytes)
FebruaryAscii = int.to_bytes(FebruaryBytes, length=8, byteorder=sys.byteorder)
print(FebruaryAscii)



print('\n\n')
MarchBytes = int.from_bytes(b'March', byteorder=sys.byteorder)  # creating an int from bytes
print(MarchBytes)
MarchAscii = int.to_bytes(MarchBytes, length=5, byteorder=sys.byteorder)
print(MarchAscii)



print('\n\n')
AprilBytes = int.from_bytes(b'April', byteorder=sys.byteorder)  # creating an int from bytes
print(AprilBytes)
AprilAscii = int.to_bytes(AprilBytes, length=5, byteorder=sys.byteorder)
print(AprilAscii)



print('\n\n')
MayBytes = int.from_bytes(b'May', byteorder=sys.byteorder)  # creating an int from bytes
print(MayBytes)
MayAscii = int.to_bytes(MayBytes, length=3, byteorder=sys.byteorder)
print(MayAscii)



print('\n\n')
JuneBytes = int.from_bytes(b'June', byteorder=sys.byteorder)  # creating an int from bytes
print(JuneBytes)
JuneAscii = int.to_bytes(JuneBytes, length=4, byteorder=sys.byteorder)
print(JuneAscii)



print('\n\n')
JulyBytes = int.from_bytes(b'July', byteorder=sys.byteorder)  # creating an int from bytes
print(JulyBytes)
JulyAscii = int.to_bytes(JulyBytes, length=4, byteorder=sys.byteorder)
print(JulyAscii)



print('\n\n')
AugustBytes = int.from_bytes(b'August', byteorder=sys.byteorder)  # creating an int from bytes
print(AugustBytes)
AugustAscii = int.to_bytes(AugustBytes, length=6, byteorder=sys.byteorder)
print(AugustAscii)



print('\n\n')
SeptemberBytes = int.from_bytes(b'September', byteorder=sys.byteorder)  # creating an int from bytes
print(SeptemberBytes)
SeptemberAscii = int.to_bytes(SeptemberBytes, length=9, byteorder=sys.byteorder)
print(SeptemberAscii)


print('\n\n')
OctoberBytes = int.from_bytes(b'October', byteorder=sys.byteorder)  # creating an int from bytes
print(OctoberBytes)
OctoberAscii = int.to_bytes(OctoberBytes, length=7, byteorder=sys.byteorder)
print(OctoberAscii)


print('\n\n')
NovemberBytes = int.from_bytes(b'November', byteorder=sys.byteorder)  # creating an int from bytes
print(NovemberBytes)
NovemberAscii = int.to_bytes(NovemberBytes, length=8, byteorder=sys.byteorder)
print(NovemberAscii)


print('\n\n')
DecemberBytes = int.from_bytes(b'December', byteorder=sys.byteorder)  # creating an int from bytes
print(DecemberBytes)
DecemberAscii = int.to_bytes(DecemberBytes, length=8, byteorder=sys.byteorder)
print(DecemberAscii)



print('\n\n')
UnlistedBytes = int.from_bytes(b'Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(UnlistedBytes)
UnlistedAscii = int.to_bytes(UnlistedBytes, length=8, byteorder=sys.byteorder)
print(UnlistedAscii)


# 34184235089551690
# b'January'
#
# #
# 8751164182992414022
# b'February'
#
# #
# 448345039181
# b'March'
#
# #
# 465625575489
# b'April'
#
# #
# 7954765
# b'May'
#
# #
# 1701737802
# b'June'
#
# #
# 2037151050
# b'July'
#
# #
# 128039239775553
# b'August'
#
# #
# 2110234346230949897555
# b'September'
#
# #
# 32199620796113743
# b'October'
#
# #
# 8243102914964778830
# b'November'
#
# #
# 8243102914963531076
# b'December'
#
# #
# 7234316415479344725
# b'Unlisted'