# Target (alleged attack) countries listed as binary

import binascii
import sys
import io

print('\n\n')
AfghanistanBytes = int.from_bytes(b'Afghanistan', byteorder=sys.byteorder)  # creating an int from bytes
print(AfghanistanBytes)
AfghanistanAscii = int.to_bytes(AfghanistanBytes, length=11, byteorder=sys.byteorder)
print(AfghanistanAscii)

# output is:
# 133442057845059666670216769
# b'Afghanistan'


print('\n\n')
Afghanistan_Application_Users_India_Individuals_Middle_EastBytes = int.from_bytes(b'Afghanistan_Application_Users_India_Individuals_Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Afghanistan_Application_Users_India_Individuals_Middle_EastBytes)
Afghanistan_Application_Users_India_Individuals_Middle_EastAscii = int.to_bytes(Afghanistan_Application_Users_India_Individuals_Middle_EastBytes, length=59, byteorder=sys.byteorder)
print(Afghanistan_Application_Users_India_Individuals_Middle_EastAscii)

# output is:
# 5547024738073957303662399576029973568509146976390336004265898740432675875991326601817987176556771282997325216339676316688169204494214088844865
# b'Afghanistan_Application_Users_India_Individuals_Middle_East'


print('\n\n')
AfricaBytes = int.from_bytes(b'Africa', byteorder=sys.byteorder)  # creating an int from bytes
print(AfricaBytes)
AfricaAscii = int.to_bytes(AfricaBytes, length=6, byteorder=sys.byteorder)
print(AfricaAscii)

# output is:
# 107079598761537
# b'Africa'


print('\n\n')
Africa_AsiaBytes = int.from_bytes(b'Africa_Asia', byteorder=sys.byteorder)  # creating an int from bytes
print(Africa_AsiaBytes)
Africa_AsiaAscii = int.to_bytes(Africa_AsiaBytes, length=11, byteorder=sys.byteorder)
print(Africa_AsiaAscii)

# output is:
# 117763779069479634143962689
# b'Africa_Asia'


print('\n\n')
Al_QuaidaBytes = int.from_bytes(b'Al_Quaida', byteorder=sys.byteorder)  # creating an int from bytes
print(Al_QuaidaBytes)
Al_QuaidaAscii = int.to_bytes(Al_QuaidaBytes, length=9, byteorder=sys.byteorder)
print(Al_QuaidaAscii)

# output is:
# 1796569596582678195265
# b'Al_Quaida'


print('\n\n')
Application_UsersBytes = int.from_bytes(b'Application_Users', byteorder=sys.byteorder)  # creating an int from bytes
print(Application_UsersBytes)
Application_UsersAscii = int.to_bytes(Application_UsersBytes, length=17, byteorder=sys.byteorder)
print(Application_UsersAscii)

# output is:
# 39284530948651148542945322099333464617025
# b'Application_Users'


print('\n\n')
Application_Users_IndividualsBytes = int.from_bytes(b'Application_Users_Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(Application_Users_IndividualsBytes)
Application_Users_IndividualsAscii = int.to_bytes(Application_Users_IndividualsBytes, length=29, byteorder=sys.byteorder)
print(Application_Users_IndividualsAscii)

# output is:
# 3111807686350090077732346834447189654644633344498384566960921427079233
# b'Application_Users_Individuals'


print('\n\n')
Application_Users_JapanBytes = int.from_bytes(b'Application_Users_Japan', byteorder=sys.byteorder)  # creating an int from bytes
print(Application_Users_JapanBytes)
Application_Users_JapanAscii = int.to_bytes(Application_Users_JapanBytes, length=23, byteorder=sys.byteorder)
print(Application_Users_JapanAscii)

# output is:
# 10572363095725242809903474363794222115376060650679726145
# b'Application_Users_Japan'

# Armenia

print('\n\n')
ArmeniaBytes = int.from_bytes(b'Armenia', byteorder=sys.byteorder)  # creating an int from bytes
print(ArmeniaBytes)
ArmeniaAscii = int.to_bytes(ArmeniaBytes, length=7, byteorder=sys.byteorder)
print(ArmeniaAscii)

# output is:
# 27418995609924161
# b'Armenia'

print('\n\n')
AsiaBytes = int.from_bytes(b'Asia', byteorder=sys.byteorder)  # creating an int from bytes
print(AsiaBytes)
AsiaAscii = int.to_bytes(AsiaBytes, length=4, byteorder=sys.byteorder)
print(AsiaAscii)

# output is:
# 1634300737
# b'Asia'


print('\n\n')
Asia_Canada_Europe_Middle_East_USABytes = int.from_bytes(b'Asia_Canada_Europe_Middle_East_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Asia_Canada_Europe_Middle_East_USABytes)
Asia_Canada_Europe_Middle_East_USAAscii = int.to_bytes(Asia_Canada_Europe_Middle_East_USABytes, length=34, byteorder=sys.byteorder)
print(Asia_Canada_Europe_Middle_East_USAAscii)

# output is:
# 1936429723561952681582869571271737150404117317300876807438770316145334861458666305
# b'Asia_Canada_Europe_Middle_East_USA'


# Asia_Europe_Middle_East_USA

print('\n\n')
Asia_Europe_Middle_East_USABytes = int.from_bytes(b'Asia_Europe_Middle_East_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Asia_Europe_Middle_East_USABytes)
Asia_Europe_Middle_East_USAAscii = int.to_bytes(Asia_Europe_Middle_East_USABytes, length=27, byteorder=sys.byteorder)
print(Asia_Europe_Middle_East_USAAscii)

# output is:
# 26873360808337585803091529125126950972081670239456308127962067777
# b'Asia_Europe_Middle_East_USA'

print('\n\n')
Asia_Europe_North_AmericaBytes = int.from_bytes(b'Asia_Europe_North_America', byteorder=sys.byteorder)  # creating an int from bytes
print(Asia_Europe_North_AmericaBytes)
Asia_Europe_North_AmericaAscii = int.to_bytes(Asia_Europe_North_AmericaBytes, length=25, byteorder=sys.byteorder)
print(Asia_Europe_North_AmericaAscii)

# output is:
# 611316441071925721528505149291982085844431624011733040460609
# b'Asia_Europe_North_America'


print('\n\n')
Asia_South_AmericaBytes = int.from_bytes(b'Asia_South_America', byteorder=sys.byteorder)  # creating an int from bytes
print(Asia_South_AmericaBytes)
Asia_South_AmericaAscii = int.to_bytes(Asia_South_AmericaBytes, length=18, byteorder=sys.byteorder)
print(Asia_South_AmericaAscii)

# output is:
# 8483719852624495593292136065139819009372993
# b'Asia_South_America'


print('\n\n')
Asia_USABytes = int.from_bytes(b'Asia_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Asia_USABytes)
Asia_USAAscii = int.to_bytes(Asia_USABytes, length=8, byteorder=sys.byteorder)
print(Asia_USAAscii)

# output is:
# 4707199903676855105
# b'Asia_USA'


print('\n\n')
AustraliaBytes = int.from_bytes(b'Australia', byteorder=sys.byteorder)  # creating an int from bytes
print(AustraliaBytes)
AustraliaAscii = int.to_bytes(AustraliaBytes, length=9, byteorder=sys.byteorder)
print(AustraliaAscii)

# output is:
# 1796930728965501580609
# b'Australia'




# Australia_Canada_Japan_Switzerland_UK_USA
# Australia_Canada_New_Zealand_UK_USA
# Austria
# Austria_Germany_Switzerland
# Bahrain
# Belarus_Mongolia_Russia
# Belgium




print('\n\n')
BrazilBytes = int.from_bytes(b'Brazil', byteorder=sys.byteorder)  # creating an int from bytes
print(BrazilBytes)
BrazilAscii = int.to_bytes(BrazilBytes, length=6, byteorder=sys.byteorder)
print(BrazilAscii)

# output is:
# 119200280572482
# b'Brazil'


# Cambodia
# Canada
# Canada_France_Multiple_UK_USA
# Central_America
# Central_Asia_Eastern_Europe
# Central_Asia_Eastern_Europe_Russia
# Central_Asia_Europe_USA
# Chile



print('\n\n')
ChinaBytes = int.from_bytes(b'China', byteorder=sys.byteorder)  # creating an int from bytes
print(ChinaBytes)
ChinaAscii = int.to_bytes(ChinaBytes, length=5, byteorder=sys.byteorder)
print(ChinaAscii)

# output is:
# 418464229443
# b'China'



# China_Germany
# China_Individuals


print('\n\n')
China_PakistanBytes = int.from_bytes(b'China_Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(China_PakistanBytes)
China_PakistanAscii = int.to_bytes(China_PakistanBytes, length=14, byteorder=sys.byteorder)
print(China_PakistanAscii)

# output is:
# 2238786227951005213617790124648515
# b'China_Pakistan'



# CSIS_USA



print('\n\n')
Czech_RepublicBytes = int.from_bytes(b'Czech_Republic', byteorder=sys.byteorder)  # creating an int from bytes
print(Czech_RepublicBytes)
Czech_RepublicAscii = int.to_bytes(Czech_RepublicBytes, length=14, byteorder=sys.byteorder)
print(Czech_RepublicAscii)

# output is:
# 2016311051235894369754033219271235
# b'Czech_Republic'



#------ Czech_Republic_Individuals
#------ Denmark
#------ East_Asia




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




# Estonia
# Europe
# Europe_Individuals
# Europe_Individuals_Middle_East
# Europe_Japan_USA
# Europe_Middle_East
# Europe_Middle_East_North_America
# Europe_NATO
# Europe_NATO_Ukraine
# Europe_North_America
# Europe_Russia
# Finland
# France
# France_Germany_UK
# France_South_Korea
# French_German_Japanese
# Georgia



print('\n\n')
GermanyBytes = int.from_bytes(b'Germany', byteorder=sys.byteorder)  # creating an int from bytes
print(GermanyBytes)
GermanyAscii = int.to_bytes(GermanyBytes, length=7, byteorder=sys.byteorder)
print(GermanyAscii)

# output is:
# 34179836909086023
# b'Germany'




# Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA
# Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals
# Germany_Turkey
# Global_Unlisted



print('\n\n')
IndiaBytes = int.from_bytes(b'India', byteorder=sys.byteorder)  # creating an int from bytes
print(IndiaBytes)
IndiaAscii = int.to_bytes(IndiaBytes, length=5, byteorder=sys.byteorder)
print(IndiaAscii)

# output is:
# 418380017225
# b'India'



# India_Italy_Saudi_Arabia_Scotland_UAE
# India_Pakistan




print('\n\n')
IndividualsBytes = int.from_bytes(b'Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(IndividualsBytes)
IndividualsAscii = int.to_bytes(IndividualsBytes, length=11, byteorder=sys.byteorder)
print(IndividualsAscii)

# output is:
# 139538282629009384004677193
# b'Individuals'



# Individuals_Iran
# Individuals_Latvia
# Individuals_Multiple
# Individuals_NATO_Ukraine
# Individuals_Sri_Lanka
# Individuals_USA
# Individuals_Vietnam
# Indonesia
# Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang




print('\n\n')
InternationalBytes = int.from_bytes(b'International', byteorder=sys.byteorder)  # creating an int from bytes
print(InternationalBytes)
InternationalAscii = int.to_bytes(InternationalBytes, length=13, byteorder=sys.byteorder)
print(InternationalAscii)

# output is:
# 8586795105461350372667137748553
# b'International'

print('\n\n')
IranBytes = int.from_bytes(b'Iran', byteorder=sys.byteorder)  # creating an int from bytes
print(IranBytes)
IranAscii = int.to_bytes(IranBytes, length=4, byteorder=sys.byteorder)
print(IranAscii)

# output is:
# 1851880009
# b'Iran'


# Iran_Israel_Middle_East
# Iran_Syria
# Iraq_Pakistan_Tajikistan
# Ireland







print('\n\n')
ISISBytes = int.from_bytes(b'ISIS', byteorder=sys.byteorder)  # creating an int from bytes
print(ISISBytes)
ISISAscii = int.to_bytes(ISISBytes, length=4, byteorder=sys.byteorder)
print(ISISAscii)

# output is:
# 1397314377
# b'ISIS'

print('\n\n')
IsraelBytes = int.from_bytes(b'Israel', byteorder=sys.byteorder)  # creating an int from bytes
print(IsraelBytes)
IsraelAscii = int.to_bytes(IsraelBytes, length=6, byteorder=sys.byteorder)
print(IsraelAscii)

# output is:
# 119182682387273
# b'Israel'


# Israel_Saudi_Arabia_USA
# Israel_Sudan_Syria_Middle_East
# Italy
# Italy_France_Germany_Poland_Spain_Turkey_USA
# Japan
# Japan_Multiple_Unlisted
# Japan_Unlisted
# Kazakhstan





print('\n\n')
LebanonBytes = int.from_bytes(b'Lebanon', byteorder=sys.byteorder)  # creating an int from bytes
print(LebanonBytes)
LebanonAscii = int.to_bytes(LebanonBytes, length=7, byteorder=sys.byteorder)
print(LebanonAscii)

# output is:
# 31084767309096268
# b'Lebanon'



# Lebanon_UAE
# Libya
# Lithuania
# Malaysia





print('\n\n')
MexicoBytes = int.from_bytes(b'Mexico', byteorder=sys.byteorder)  # creating an int from bytes
print(MexicoBytes)
MexicoAscii = int.to_bytes(MexicoBytes, length=6, byteorder=sys.byteorder)
print(MexicoAscii)

# output is:
# 122472761943373
# b'Mexico'

print('\n\n')
Middle_EastBytes = int.from_bytes(b'Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Middle_EastBytes)
Middle_EastAscii = int.to_bytes(Middle_EastBytes, length=11, byteorder=sys.byteorder)
print(Middle_EastAscii)

# output is:
# 140780261553827770911713613
# b'Middle_East'



# Middle_East_South_America_UK_USA
# Montenegro



print('\n\n')
MultipleBytes = int.from_bytes(b'Multiple', byteorder=sys.byteorder)  # creating an int from bytes
print(MultipleBytes)
MultipleAscii = int.to_bytes(MultipleBytes, length=8, byteorder=sys.byteorder)
print(MultipleAscii)

# output is:
# 7308339893542614349
# b'Multiple'




# Multiple_Unlisted
# Netherlands
# Netherlands_territory
# NGOs_UN
# North_America_Pakistan_Russia_Saudi_Arabia_Turkey



print('\n\n')
North_KoreaBytes = int.from_bytes(b'North_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(North_KoreaBytes)
North_KoreaAscii = int.to_bytes(North_KoreaBytes, length=11, byteorder=sys.byteorder)
print(North_KoreaAscii)

# output is:
# 117744874465821730700160846
# b'North_Korea'


# Norway
# Oman_UAE



print('\n\n')
PakistanBytes = int.from_bytes(b'Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(PakistanBytes)
PakistanAscii = int.to_bytes(PakistanBytes, length=8, byteorder=sys.byteorder)
print(PakistanAscii)

# output is:
# 7953766455951712592
# b'Pakistan'


# Philippines
# Qatar
# Qatar_Saudi_Arabia



print('\n\n')
RussiaBytes = int.from_bytes(b'Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(RussiaBytes)
RussiaAscii = int.to_bytes(RussiaBytes, length=6, byteorder=sys.byteorder)
print(RussiaAscii)

# output is:
# 107105536406866
# b'Russia'




print('\n\n')
Saudi_ArabiaBytes = int.from_bytes(b'Saudi_Arabia', byteorder=sys.byteorder)  # creating an int from bytes
print(Saudi_ArabiaBytes)
Saudi_ArabiaAscii = int.to_bytes(Saudi_ArabiaBytes, length=12, byteorder=sys.byteorder)
print(Saudi_ArabiaAscii)

# output is:
# 30147447753212470604776956243
# b'Saudi_Arabia'


# Saudi_Arabia_South_Korea_USA
# Saudi_Arabia_USA
# Scotland
# Singapore
# South_Africa



print('\n\n')
South_KoreaBytes = int.from_bytes(b'South_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(South_KoreaBytes)
South_KoreaAscii = int.to_bytes(South_KoreaBytes, length=11, byteorder=sys.byteorder)
print(South_KoreaAscii)

# output is:
# 117744874465821730700357459
# b'South_Korea'

print('\n\n')
South_Korea_USABytes = int.from_bytes(b'South_Korea_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(South_Korea_USABytes)
South_Korea_USAAscii = int.to_bytes(South_Korea_USABytes, length=15, byteorder=sys.byteorder)
print(South_Korea_USAAscii)

# output is:
# 339189499714501404461968594046381907
# b'South_Korea_USA'


# South_Korea_USA
# Southeast_Asia
# Sweden
# Switzerland






print('\n\n')
SyriaBytes = int.from_bytes(b'Syria', byteorder=sys.byteorder)  # creating an int from bytes
print(SyriaBytes)
SyriaAscii = int.to_bytes(SyriaBytes, length=5, byteorder=sys.byteorder)
print(SyriaAscii)

# output is:
# 418380937555
# b'Syria'

print('\n\n')
TaiwanBytes = int.from_bytes(b'Taiwan', byteorder=sys.byteorder)  # creating an int from bytes
print(TaiwanBytes)
TaiwanAscii = int.to_bytes(TaiwanBytes, length=6, byteorder=sys.byteorder)
print(TaiwanAscii)

# output is:
# 121364894277972
# b'Taiwan'



# Tehran
# Tibet


print('\n\n')
TurkeyBytes = int.from_bytes(b'Turkey', byteorder=sys.byteorder)  # creating an int from bytes
print(TurkeyBytes)
TurkeyAscii = int.to_bytes(TurkeyBytes, length=6, byteorder=sys.byteorder)
print(TurkeyAscii)

# output is:
# 133476501321044
# b'Turkey'



print('\n\n')
UKBytes = int.from_bytes(b'UK', byteorder=sys.byteorder)  # creating an int from bytes
print(UKBytes)
UKAscii = int.to_bytes(UKBytes, length=2, byteorder=sys.byteorder)
print(UKAscii)

# output is:
# 19285
# b'UK'

print('\n\n')
UK_USABytes = int.from_bytes(b'UK_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(UK_USABytes)
UK_USAAscii = int.to_bytes(UK_USABytes, length=6, byteorder=sys.byteorder)
print(UK_USAAscii)

# output is:
# 71826170399573
# b'UK_USA'



# Ukraine
# UN



print('\n\n')
UnlistedBytes = int.from_bytes(b'Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(UnlistedBytes)
UnlistedAscii = int.to_bytes(UnlistedBytes, length=8, byteorder=sys.byteorder)
print(UnlistedAscii)

# output is:
# 7234316415479344725
# b'Unlisted'

print('\n\n')
USABytes = int.from_bytes(b'USA', byteorder=sys.byteorder)  # creating an int from bytes
print(USABytes)
USAAscii = int.to_bytes(USABytes, length=3, byteorder=sys.byteorder)
print(USAAscii)

# output is:
# 4281173
# b'USA'



# USA_Europe
# USA_Western_World
# Venezuela


print('\n\n')
Western_WorldBytes = int.from_bytes(b'Western_World', byteorder=sys.byteorder)  # creating an int from bytes
print(Western_WorldBytes)
Western_WorldAscii = int.to_bytes(Western_WorldBytes, length=13, byteorder=sys.byteorder)
print(Western_WorldAscii)

# output is:
# 7956378975824997986907049911639
# b'Western_World'


# Xinjiang


