# Months listed as binary

import binascii
import sys
import io


print('\n\n')
JanuaryBytes = int.from_bytes(b'January', byteorder=sys.byteorder)  # creating an int from bytes
print(JanuaryBytes)
JanuaryAscii = int.to_bytes(JanuaryBytes, length=20, byteorder=sys.byteorder)
print(JanuaryAscii)

# output is:
# 34184235089551690
# b'January\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
FebruaryBytes = int.from_bytes(b'February', byteorder=sys.byteorder)  # creating an int from bytes
print(FebruaryBytes)
FebruaryAscii = int.to_bytes(FebruaryBytes, length=20, byteorder=sys.byteorder)
print(FebruaryAscii)

# output is:
# 8751164182992414022
# b'February\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
MarchBytes = int.from_bytes(b'March', byteorder=sys.byteorder)  # creating an int from bytes
print(MarchBytes)
MarchAscii = int.to_bytes(MarchBytes, length=20, byteorder=sys.byteorder)
print(MarchAscii)

# output is:
# 448345039181
# b'March\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
AprilBytes = int.from_bytes(b'April', byteorder=sys.byteorder)  # creating an int from bytes
print(AprilBytes)
AprilAscii = int.to_bytes(AprilBytes, length=20, byteorder=sys.byteorder)
print(AprilAscii)

# output is:
# 461413379138
# b'April\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
MayBytes = int.from_bytes(b'May', byteorder=sys.byteorder)  # creating an int from bytes
print(MayBytes)
MayAscii = int.to_bytes(MayBytes, length=20, byteorder=sys.byteorder)
print(MayAscii)

# output is:
# 461413379138
# b'May\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
JuneBytes = int.from_bytes(b'June', byteorder=sys.byteorder)  # creating an int from bytes
print(JuneBytes)
JuneAscii = int.to_bytes(JuneBytes, length=20, byteorder=sys.byteorder)
print(JuneAscii)

# output is:
# 461413379138
# b'June\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
JulyBytes = int.from_bytes(b'July', byteorder=sys.byteorder)  # creating an int from bytes
print(JulyBytes)
JulyAscii = int.to_bytes(JulyBytes, length=20, byteorder=sys.byteorder)
print(JulyAscii)

# output is:
# 461413379138
# b'July\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
AugustBytes = int.from_bytes(b'August', byteorder=sys.byteorder)  # creating an int from bytes
print(AugustBytes)
AugustAscii = int.to_bytes(AugustBytes, length=20, byteorder=sys.byteorder)
print(AugustAscii)

# output is:
# 461413379138
# b'August\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
SeptemberBytes = int.from_bytes(b'September', byteorder=sys.byteorder)  # creating an int from bytes
print(SeptemberBytes)
SeptemberAscii = int.to_bytes(SeptemberBytes, length=20, byteorder=sys.byteorder)
print(SeptemberAscii)

# output is:
# 461413379138
# b'September\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
OctoberBytes = int.from_bytes(b'October', byteorder=sys.byteorder)  # creating an int from bytes
print(OctoberBytes)
OctoberAscii = int.to_bytes(OctoberBytes, length=20, byteorder=sys.byteorder)
print(OctoberAscii)

# output is:
# 461413379138
# b'October\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
NovemberBytes = int.from_bytes(b'November', byteorder=sys.byteorder)  # creating an int from bytes
print(NovemberBytes)
NovemberAscii = int.to_bytes(NovemberBytes, length=20, byteorder=sys.byteorder)
print(NovemberAscii)

# output is:
# 461413379138
# b'November\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print('\n\n')
DecemberBytes = int.from_bytes(b'December', byteorder=sys.byteorder)  # creating an int from bytes
print(DecemberBytes)
DecemberAscii = int.to_bytes(DecemberBytes, length=20, byteorder=sys.byteorder)
print(DecemberAscii)

# output is:
# 461413379138
# b'December\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'


print('\n\n')
UnlistedBytes = int.from_bytes(b'Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(UnlistedBytes)
UnlistedAscii = int.to_bytes(UnlistedBytes, length=20, byteorder=sys.byteorder)
print(UnlistedAscii)

# output is:
# 7234316415479344725
# b'Unlisted\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'