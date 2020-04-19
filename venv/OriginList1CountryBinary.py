# Origin (alleged attack) countries listed as binary

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
IndividualsBytes = int.from_bytes(b'Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(IndividualsBytes)
IndividualsAscii = int.to_bytes(IndividualsBytes, length=11, byteorder=sys.byteorder)
print(IndividualsAscii)

# output is:
# 139538282629009384004677193
# b'Individuals'

print('\n\n')
Individuals_UkraineBytes = int.from_bytes(b'Individuals_Ukraine', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_UkraineBytes)
Individuals_UkraineAscii = int.to_bytes(Individuals_UkraineBytes, length=19, byteorder=sys.byteorder)
print(Individuals_UkraineAscii)

# output is: 2261993475681827677736728506999153589307600457
# b'Individuals_Ukraine'

print('\n\n')
Individuals_UnlistedBytes = int.from_bytes(b'Individuals_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_UnlistedBytes)
Individuals_UnlistedAscii = int.to_bytes(Individuals_UnlistedBytes, length=20, byteorder=sys.byteorder)
print(Individuals_UnlistedAscii)

# output is:
# 573161596645207770904272559636410843002082455113
# b'Individuals_Unlisted'

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

print('\n\n')
Iran_North_Korea_RussiaBytes = int.from_bytes(b'Iran_North_Korea_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(Iran_North_Korea_RussiaBytes)
Iran_North_Korea_RussiaAscii = int.to_bytes(Iran_North_Korea_RussiaBytes, length=23, byteorder=sys.byteorder)
print(Iran_North_Korea_RussiaAscii)

# output is:
# 9330208112349500424777135934104632250386116936128885321
# b'Iran_North_Korea_Russia'

print('\n\n')
Iran_RussiaBytes = int.from_bytes(b'Iran_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(Iran_RussiaBytes)
Iran_RussiaAscii = int.to_bytes(Iran_RussiaBytes, length=11, byteorder=sys.byteorder)
print(Iran_RussiaAscii)

# output is:
# 117763782678535275756483145
# b'Iran_Russia'

print('\n\n')
Iran_UnlistedBytes = int.from_bytes(b'Iran_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Iran_UnlistedBytes)
Iran_UnlistedAscii = int.to_bytes(Iran_UnlistedBytes, length=13, byteorder=sys.byteorder)
print(Iran_UnlistedAscii)

# output is:
# 7954215017830331842300462854729
# b'Iran_Unlisted'

print('\n\n')
IraqBytes = int.from_bytes(b'Iraq', byteorder=sys.byteorder)  # creating an int from bytes
print(IraqBytes)
IraqAscii = int.to_bytes(IraqBytes, length=4, byteorder=sys.byteorder)
print(IraqAscii)

# output is:
# 1902211657
# b'Iraq'

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

print('\n\n')
Israel_USABytes = int.from_bytes(b'Israel_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Israel_USABytes)
Israel_USAAscii = int.to_bytes(Israel_USABytes, length=10, byteorder=sys.byteorder)
print(Israel_USAAscii)

# output is:
# 308491052899443525448521
# b'Israel_USA'

print('\n\n')
LebanonBytes = int.from_bytes(b'Lebanon', byteorder=sys.byteorder)  # creating an int from bytes
print(LebanonBytes)
LebanonAscii = int.to_bytes(LebanonBytes, length=7, byteorder=sys.byteorder)
print(LebanonAscii)

# output is:
# 31084767309096268
# b'Lebanon'

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

print('\n\n')
MoroccoBytes = int.from_bytes(b'Morocco', byteorder=sys.byteorder)  # creating an int from bytes
print(MoroccoBytes)
MoroccoAscii = int.to_bytes(MoroccoBytes, length=7, byteorder=sys.byteorder)
print(MoroccoAscii)

# output is:
# 31353001137565517
# b'Morocco'

print('\n\n')
MultipleBytes = int.from_bytes(b'Multiple', byteorder=sys.byteorder)  # creating an int from bytes
print(MultipleBytes)
MultipleAscii = int.to_bytes(MultipleBytes, length=8, byteorder=sys.byteorder)
print(MultipleAscii)

# output is:
# 7308339893542614349
# b'Multiple'

print('\n\n')
Nation_State_Actor_Eastern_EuropeBytes = int.from_bytes(b'Nation_State_Actor_Eastern_Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(Nation_State_Actor_Eastern_EuropeBytes)
Nation_State_Actor_Eastern_EuropeAscii = int.to_bytes(Nation_State_Actor_Eastern_EuropeBytes, length=33, byteorder=sys.byteorder)
print(Nation_State_Actor_Eastern_EuropeAscii)

# output is:
# 11745856961995155074459591118783721087539815469043632190606120890413099009728846
# b'Nation_State_Actor_Eastern_Europe'

print('\n\n')
Nation_State_Actor_UnlistedBytes = int.from_bytes(b'Nation_State_Actor_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Nation_State_Actor_UnlistedBytes)
Nation_State_Actor_UnlistedAscii = int.to_bytes(Nation_State_Actor_UnlistedBytes, length=27, byteorder=sys.byteorder)
print(Nation_State_Actor_UnlistedAscii)

# output is:
# 41300645649190979956682253942903520807850576892501048304935919950
# b'Nation_State_Actor_Unlisted'

print('\n\n')
Non_State_Actor_UnlistedBytes = int.from_bytes(b'Non_State_Actor_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Non_State_Actor_UnlistedBytes)
Non_State_Actor_UnlistedAscii = int.to_bytes(Non_State_Actor_UnlistedBytes, length=24, byteorder=sys.byteorder)
print(Non_State_Actor_UnlistedAscii)

# output is:
# 2461710312914310691158905860358686495295201354771914977102
# b'Non_State_Actor_Unlisted'

print('\n\n')
North_KoreaBytes = int.from_bytes(b'North_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(North_KoreaBytes)
North_KoreaAscii = int.to_bytes(North_KoreaBytes, length=11, byteorder=sys.byteorder)
print(North_KoreaAscii)

# output is:
# 117744874465821730700160846
# b'North_Korea'

print('\n\n')
PakistanBytes = int.from_bytes(b'Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(PakistanBytes)
PakistanAscii = int.to_bytes(PakistanBytes, length=8, byteorder=sys.byteorder)
print(PakistanAscii)

# output is:
# 7953766455951712592
# b'Pakistan'

print('\n\n')
RussiaBytes = int.from_bytes(b'Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(RussiaBytes)
RussiaAscii = int.to_bytes(RussiaBytes, length=6, byteorder=sys.byteorder)
print(RussiaAscii)

# output is:
# 107105536406866
# b'Russia'

print('\n\n')
Russia_UkraineBytes = int.from_bytes(b'Russia_Ukraine', byteorder=sys.byteorder)  # creating an int from bytes
print(Russia_UkraineBytes)
Russia_UkraineAscii = int.to_bytes(Russia_UkraineBytes, length=14, byteorder=sys.byteorder)
print(Russia_UkraineAscii)

# output is:
# 2057271081577553266210956287112530
# b'Russia_Ukraine'

print('\n\n')
Russia_Ukraine_USABytes = int.from_bytes(b'Russia_Ukraine_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Russia_Ukraine_USABytes)
Russia_Ukraine_USAAscii = int.to_bytes(Russia_Ukraine_USABytes, length=18, byteorder=sys.byteorder)
print(Russia_Ukraine_USAAscii)

# output is:
# 5690655501723968284733388360289691192489298
# b'Russia_Ukraine_USA'

print('\n\n')
Saudi_ArabiaBytes = int.from_bytes(b'Saudi_Arabia', byteorder=sys.byteorder)  # creating an int from bytes
print(Saudi_ArabiaBytes)
Saudi_ArabiaAscii = int.to_bytes(Saudi_ArabiaBytes, length=12, byteorder=sys.byteorder)
print(Saudi_ArabiaAscii)

# output is:
# 30147447753212470604776956243
# b'Saudi_Arabia'

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

print('\n\n')
State_Sponsored_Actor_UnlistedBytes = int.from_bytes(b'State_Sponsored_Actor_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(State_Sponsored_Actor_UnlistedBytes)
State_Sponsored_Actor_UnlistedAscii = int.to_bytes(State_Sponsored_Actor_UnlistedBytes, length=30, byteorder=sys.byteorder)
print(State_Sponsored_Actor_UnlistedAscii)

# output is:
# 692909852995937295984928817766944035748308436617603438577965161292854355
# b'State_Sponsored_Actor_Unlisted'

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

print('\n\n')
Taiwan_USABytes = int.from_bytes(b'Taiwan_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Taiwan_USABytes)
Taiwan_USAAscii = int.to_bytes(Taiwan_USABytes, length=10, byteorder=sys.byteorder)
print(Taiwan_USAAscii)

# output is:
# 308491052901625737339220
# b'Taiwan_USA'

print('\n\n')
TurkeyBytes = int.from_bytes(b'Turkey', byteorder=sys.byteorder)  # creating an int from bytes
print(TurkeyBytes)
TurkeyAscii = int.to_bytes(TurkeyBytes, length=6, byteorder=sys.byteorder)
print(TurkeyAscii)

# output is:
# 133476501321044
# b'Turkey'

print('\n\n')
UAEBytes = int.from_bytes(b'UAE', byteorder=sys.byteorder)  # creating an int from bytes
print(UAEBytes)
UAEAscii = int.to_bytes(UAEBytes, length=3, byteorder=sys.byteorder)
print(UAEAscii)

# output is:
# 4538709
# b'UAE'

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

print('\n\n')
VietnamBytes = int.from_bytes(b'Vietnam', byteorder=sys.byteorder)  # creating an int from bytes
print(VietnamBytes)
VietnamAscii = int.to_bytes(VietnamBytes, length=7, byteorder=sys.byteorder)
print(VietnamAscii)

# output is:
# 30787899488561494
# b'Vietnam'


print('\n\n')
Western_WorldBytes = int.from_bytes(b'Western_World', byteorder=sys.byteorder)  # creating an int from bytes
print(Western_WorldBytes)
Western_WorldAscii = int.to_bytes(Western_WorldBytes, length=13, byteorder=sys.byteorder)
print(Western_WorldAscii)

# output is:
# 7956378975824997986907049911639
# b'Western_World'

print('\n\n')
YemenBytes = int.from_bytes(b'Yemen', byteorder=sys.byteorder)  # creating an int from bytes
print(YemenBytes)
YemenAscii = int.to_bytes(YemenBytes, length=5, byteorder=sys.byteorder)
print(YemenAscii)

# output is:
# 474148070745
# b'Yemen'