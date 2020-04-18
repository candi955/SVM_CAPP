# Countries listed as binary

import binascii
import sys
import io

print('\n\n')
Africa_ChinaBytes = int.from_bytes(b'Africa_China', byteorder=sys.byteorder)  # creating an int from bytes
print(Africa_ChinaBytes)
Africa_ChinaAscii = int.to_bytes(Africa_ChinaBytes, length=12, byteorder=sys.byteorder)
print(Africa_ChinaAscii)

# output is:
# 30153525564624871856989693505
# b'Africa_China'

print('\n\n')
AustraliaBytes = int.from_bytes(b'Australia', byteorder=sys.byteorder)  # creating an int from bytes
print(AustraliaBytes)
AustraliaAscii = int.to_bytes(AustraliaBytes, length=9, byteorder=sys.byteorder)
print(AustraliaAscii)

# output is:
# 1796930728965501580609
# b'Australia'

print('\n\n')
AzerbaijanBytes = int.from_bytes(b'Azerbaijan', byteorder=sys.byteorder)  # creating an int from bytes
print(AzerbaijanBytes)
AzerbaijanAscii = int.to_bytes(AzerbaijanBytes, length=10, byteorder=sys.byteorder)
print(AzerbaijanAscii)

# output is:
# 521257315057726828935745
# b'Azerbaijan'

print('\n\n')
BrazilBytes = int.from_bytes(b'Brazil', byteorder=sys.byteorder)  # creating an int from bytes
print(BrazilBytes)
BrazilAscii = int.to_bytes(BrazilBytes, length=6, byteorder=sys.byteorder)
print(BrazilAscii)

# output is:
# 119200280572482
# b'Brazil'

print('\n\n')
ChinaBytes = int.from_bytes(b'China', byteorder=sys.byteorder)  # creating an int from bytes
print(ChinaBytes)
ChinaAscii = int.to_bytes(ChinaBytes, length=5, byteorder=sys.byteorder)
print(ChinaAscii)

# output is:
# 418464229443
# b'China'

print('\n\n')
China_North_KoreaBytes = int.from_bytes(b'China_North_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(China_North_KoreaBytes)
China_North_KoreaAscii = int.to_bytes(China_North_KoreaBytes, length=17, byteorder=sys.byteorder)
print(China_North_KoreaAscii)

# output is:
# 33142235798066285977489245281315271043139
# b'China_North_Korea'

print('\n\n')
China_PakistanBytes = int.from_bytes(b'China_Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(China_PakistanBytes)
China_PakistanAscii = int.to_bytes(China_PakistanBytes, length=14, byteorder=sys.byteorder)
print(China_PakistanAscii)

# output is:
# 2238786227951005213617790124648515
# b'China_Pakistan'

print('\n\n')
China_RussiaBytes = int.from_bytes(b'China_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(China_RussiaBytes)
China_RussiaAscii = int.to_bytes(China_RussiaBytes, length=12, byteorder=sys.byteorder)
print(China_RussiaAscii)

# output is:
# 30147528365705030538042632259
# b'China_Russia'

print('\n\n')
Czech_RepublicBytes = int.from_bytes(b'Czech_Republic', byteorder=sys.byteorder)  # creating an int from bytes
print(Czech_RepublicBytes)
Czech_RepublicAscii = int.to_bytes(Czech_RepublicBytes, length=14, byteorder=sys.byteorder)
print(Czech_RepublicAscii)

# output is:
# 2016311051235894369754033219271235
# b'Czech_Republic'

print('\n\n')
Decentralized_International_Hacktivist_GroupBytes = int.from_bytes(b'Decentralized_International_Hacktivist_Group', byteorder=sys.byteorder)  # creating an int from bytes
print(Decentralized_International_Hacktivist_GroupBytes)
Decentralized_International_Hacktivist_GroupAscii = int.to_bytes(Decentralized_International_Hacktivist_GroupBytes, length=44, byteorder=sys.byteorder)
print(Decentralized_International_Hacktivist_GroupAscii)

# output is:
# 4030061651715448937258886338687573509473192067501578500999556277764116296964663760381662969481473103717700
# b'Decentralized_International_Hacktivist_Group'

print('\n\n')
Eastern_EuropeBytes = int.from_bytes(b'Eastern_Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(Eastern_EuropeBytes)
Eastern_EuropeAscii = int.to_bytes(Eastern_EuropeBytes, length=14, byteorder=sys.byteorder)
print(Eastern_EuropeAscii)

# output is:
# 2057431415377846504395799230898501
# b'Eastern_Europe'

print('\n\n')
EgyptBytes = int.from_bytes(b'Egypt', byteorder=sys.byteorder)  # creating an int from bytes
print(EgyptBytes)
EgyptAscii = int.to_bytes(EgyptBytes, length=5, byteorder=sys.byteorder)
print(EgyptAscii)

# output is:
# 500103210821
# b'Egypt'

print('\n\n')
GazaBytes = int.from_bytes(b'Gaza', byteorder=sys.byteorder)  # creating an int from bytes
print(GazaBytes)
GazaAscii = int.to_bytes(GazaBytes, length=4, byteorder=sys.byteorder)
print(GazaAscii)

# output is:
# 1635410247
# b'Gaza'

print('\n\n')
Gaza_Former_Soviet_Union_LebanonBytes = int.from_bytes(b'Gaza_Former_Soviet_Union_Lebanon', byteorder=sys.byteorder)  # creating an int from bytes
print(Gaza_Former_Soviet_Union_LebanonBytes)
Gaza_Former_Soviet_Union_LebanonAscii = int.to_bytes(Gaza_Former_Soviet_Union_LebanonBytes, length=32, byteorder=sys.byteorder)
print(Gaza_Former_Soviet_Union_LebanonAscii)

# output is:
# 49951295185924953357192938129459662694624102732189565470444669956949290934599
# b'Gaza_Former_Soviet_Union_Lebanon'

print('\n\n')
GermanyBytes = int.from_bytes(b'Germany', byteorder=sys.byteorder)  # creating an int from bytes
print(GermanyBytes)
GermanyAscii = int.to_bytes(GermanyBytes, length=7, byteorder=sys.byteorder)
print(GermanyAscii)

# output is:
# 34179836909086023
# b'Germany'

print('\n\n')
IndiaBytes = int.from_bytes(b'India', byteorder=sys.byteorder)  # creating an int from bytes
print(IndiaBytes)
IndiaAscii = int.to_bytes(IndiaBytes, length=5, byteorder=sys.byteorder)
print(IndiaAscii)

# output is:
# 418380017225
# b'India'

print('\n\n')
BlankBytes = int.from_bytes(b'Blank', byteorder=sys.byteorder)  # creating an int from bytes
print(BlankBytes)
BlankAscii = int.to_bytes(BlankBytes, length=20, byteorder=sys.byteorder)
print(BlankAscii)

# output is:
# 