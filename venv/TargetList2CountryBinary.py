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


print('\n\n')
Australia_Canada_Japan_Switzerland_UK_USABytes = int.from_bytes(b'Australia_Canada_Japan_Switzerland_UK_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Australia_Canada_Japan_Switzerland_UK_USABytes)
Australia_Canada_Japan_Switzerland_UK_USAAscii = int.to_bytes(Australia_Canada_Japan_Switzerland_UK_USABytes, length=41, byteorder=sys.byteorder)
print(Australia_Canada_Japan_Switzerland_UK_USAAscii)

# output is:
# 139534466882955655784457473920909684382362106944851677537702575567474562215766014437633627337749825
# b'Australia_Canada_Japan_Switzerland_UK_USA'


# Australia_Canada_New_Zealand_UK_USA
print('\n\n')
Australia_Canada_New_Zealand_UK_USABytes = int.from_bytes(b'Australia_Canada_New_Zealand_UK_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Australia_Canada_New_Zealand_UK_USABytes)
Australia_Canada_New_Zealand_UK_USAAscii = int.to_bytes(Australia_Canada_New_Zealand_UK_USABytes, length=35, byteorder=sys.byteorder)
print(Australia_Canada_New_Zealand_UK_USAAscii)

# output is:
# 495726009159212053789849057507327564583030099413608231039652233206430848978550748481
# b'Australia_Canada_New_Zealand_UK_USA'


# Austria

print('\n\n')
AustriaBytes = int.from_bytes(b'Austria', byteorder=sys.byteorder)  # creating an int from bytes
print(AustriaBytes)
AustriaAscii = int.to_bytes(AustriaBytes, length=7, byteorder=sys.byteorder)
print(AustriaAscii)

# output is:
# 27419013041845569
# b'Austria'

print('\n\n')
Austria_Germany_SwitzerlandBytes = int.from_bytes(b'Austria_Germany_Switzerland', byteorder=sys.byteorder)  # creating an int from bytes
print(Austria_Germany_SwitzerlandBytes)
Austria_Germany_SwitzerlandAscii = int.to_bytes(Austria_Germany_SwitzerlandBytes, length=27, byteorder=sys.byteorder)
print(Austria_Germany_SwitzerlandAscii)

# output is:
# 41314988655876265391272827414481922914912132198580508749628405057
# b'Austria_Germany_Switzerland'



print('\n\n')
BahrainBytes = int.from_bytes(b'Bahrain', byteorder=sys.byteorder)  # creating an int from bytes
print(BahrainBytes)
BahrainAscii = int.to_bytes(BahrainBytes, length=7, byteorder=sys.byteorder)
print(BahrainAscii)

# output is:
# 31078114690359618
# b'Bahrain'



print('\n\n')
Belarus_Mongolia_RussiaBytes = int.from_bytes(b'Belarus_Mongolia_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(Belarus_Mongolia_RussiaBytes)
Belarus_Mongolia_RussiaAscii = int.to_bytes(Belarus_Mongolia_RussiaBytes, length=23, byteorder=sys.byteorder)
print(Belarus_Mongolia_RussiaAscii)

# output is:
# 9330208112349500424797783435764896148944012388223182146
# b'Belarus_Mongolia_Russia'


print('\n\n')
BelgiumBytes = int.from_bytes(b'Belgium', byteorder=sys.byteorder)  # creating an int from bytes
print(BelgiumBytes)
BelgiumAscii = int.to_bytes(BelgiumBytes, length=7, byteorder=sys.byteorder)
print(BelgiumAscii)

# output is:
# 30809868028634434
# b'Belgium'


print('\n\n')
BrazilBytes = int.from_bytes(b'Brazil', byteorder=sys.byteorder)  # creating an int from bytes
print(BrazilBytes)
BrazilAscii = int.to_bytes(BrazilBytes, length=6, byteorder=sys.byteorder)
print(BrazilAscii)

# output is:
# 119200280572482
# b'Brazil'


print('\n\n')
CambodiaBytes = int.from_bytes(b'Cambodia', byteorder=sys.byteorder)  # creating an int from bytes
print(CambodiaBytes)
CambodiaAscii = int.to_bytes(CambodiaBytes, length=8, byteorder=sys.byteorder)
print(CambodiaAscii)

# output is:
# 7019251923789111619
# b'Cambodia'


print('\n\n')
CanadaBytes = int.from_bytes(b'Canada', byteorder=sys.byteorder)  # creating an int from bytes
print(CanadaBytes)
CanadaAscii = int.to_bytes(CanadaBytes, length=6, byteorder=sys.byteorder)
print(CanadaAscii)

# output is:
# 107083759247683
# b'Canada'


print('\n\n')
Canada_France_Multiple_UK_USABytes = int.from_bytes(b'Canada_France_Multiple_UK_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Canada_France_Multiple_UK_USABytes)
Canada_France_Multiple_UK_USAAscii = int.to_bytes(Canada_France_Multiple_UK_USABytes, length=29, byteorder=sys.byteorder)
print(Canada_France_Multiple_UK_USAAscii)

# output is:
# 1761172573677115074610677974231769886272027516418405464348645768716611
# b'Canada_France_Multiple_UK_USA'


print('\n\n')
Central_AmericaBytes = int.from_bytes(b'Central_America', byteorder=sys.byteorder)  # creating an int from bytes
print(Central_AmericaBytes)
Central_AmericaAscii = int.to_bytes(Central_AmericaBytes, length=15, byteorder=sys.byteorder)
print(Central_AmericaAscii)

# output is:
# 505669108189612364370267082941424963
# b'Central_America'


print('\n\n')
Central_Asia_Eastern_EuropeBytes = int.from_bytes(b'Central_Asia_Eastern_Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(Central_Asia_Eastern_EuropeBytes)
Central_Asia_Eastern_EuropeAscii = int.to_bytes(Central_Asia_Eastern_EuropeBytes, length=27, byteorder=sys.byteorder)
print(Central_Asia_Eastern_EuropeAscii)

# output is:
# 41729666698114283016919014524090844581596341132174623587355747651
# b'Central_Asia_Eastern_Europe'


print('\n\n')
Central_Asia_Eastern_Europe_RussiaBytes = int.from_bytes(b'Central_Asia_Eastern_Europe_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(Central_Asia_Eastern_Europe_RussiaBytes)
Central_Asia_Eastern_Europe_RussiaAscii = int.to_bytes(Central_Asia_Eastern_Europe_RussiaBytes, length=34, byteorder=sys.byteorder)
print(Central_Asia_Eastern_Europe_RussiaAscii)

# output is:
# 2887559549285678575025028014159333265348920949327583776587248794714267494332130627
# b'Central_Asia_Eastern_Europe_Russia'

# Central_Asia_Europe_USA

print('\n\n')
Central_Asia_Europe_USABytes = int.from_bytes(b'Central_Asia_Europe_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Central_Asia_Europe_USABytes)
Central_Asia_Europe_USAAscii = int.to_bytes(Central_Asia_Europe_USABytes, length=23, byteorder=sys.byteorder)
print(Central_Asia_Europe_USAAscii)

# output is:
# 6256941893813146631859154412586712377514069709544121667
# b'Central_Asia_Europe_USA'

print('\n\n')
ChileBytes = int.from_bytes(b'Chile', byteorder=sys.byteorder)  # creating an int from bytes
print(ChileBytes)
ChileAscii = int.to_bytes(ChileBytes, length=5, byteorder=sys.byteorder)
print(ChileAscii)

# output is:
# 435610544195
# b'Chile'

print('\n\n')
ChinaBytes = int.from_bytes(b'China', byteorder=sys.byteorder)  # creating an int from bytes
print(ChinaBytes)
ChinaAscii = int.to_bytes(ChinaBytes, length=5, byteorder=sys.byteorder)
print(ChinaAscii)

# output is:
# 418464229443
# b'China'

# China_Germany

print('\n\n')
China_GermanyBytes = int.from_bytes(b'China_Germany', byteorder=sys.byteorder)  # creating an int from bytes
print(China_GermanyBytes)
China_GermanyAscii = int.to_bytes(China_GermanyBytes, length=13, byteorder=sys.byteorder)
print(China_GermanyAscii)

# output is:
# 9620768797959008789195953629251
# b'China_Germany'


print('\n\n')
China_IndividualsBytes = int.from_bytes(b'China_Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(China_IndividualsBytes)
China_IndividualsAscii = int.to_bytes(China_IndividualsBytes, length=17, byteorder=sys.byteorder)
print(China_IndividualsAscii)

# output is:
# 39276534853245351046492589691522312136771
# b'China_Individuals'


print('\n\n')
China_PakistanBytes = int.from_bytes(b'China_Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(China_PakistanBytes)
China_PakistanAscii = int.to_bytes(China_PakistanBytes, length=14, byteorder=sys.byteorder)
print(China_PakistanAscii)

# output is:
# 2238786227951005213617790124648515
# b'China_Pakistan'


print('\n\n')
CSIS_USABytes = int.from_bytes(b'CSIS_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(CSIS_USABytes)
CSIS_USAAscii = int.to_bytes(CSIS_USABytes, length=8, byteorder=sys.byteorder)
print(CSIS_USAAscii)

# output is:
# 4707199903439868739
# b'CSIS_USA'


print('\n\n')
Czech_RepublicBytes = int.from_bytes(b'Czech_Republic', byteorder=sys.byteorder)  # creating an int from bytes
print(Czech_RepublicBytes)
Czech_RepublicAscii = int.to_bytes(Czech_RepublicBytes, length=14, byteorder=sys.byteorder)
print(Czech_RepublicAscii)

# output is:
# 2016311051235894369754033219271235
# b'Czech_Republic'


print('\n\n')
Czech_Republic_IndividualsBytes = int.from_bytes(b'Czech_Republic_Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(Czech_Republic_IndividualsBytes)
Czech_Republic_IndividualsAscii = int.to_bytes(Czech_Republic_IndividualsBytes, length=26, byteorder=sys.byteorder)
print(Czech_Republic_IndividualsAscii)

# output is:
# 185478191754227285249969174530609441383227936193346174183635523
# b'Czech_Republic_Individuals'


print('\n\n')
DenmarkBytes = int.from_bytes(b'Denmark', byteorder=sys.byteorder)  # creating an int from bytes
print(DenmarkBytes)
DenmarkAscii = int.to_bytes(DenmarkBytes, length=7, byteorder=sys.byteorder)
print(DenmarkAscii)

# output is:
# 30243585281385796
# b'Denmark'

print('\n\n')
East_AsiaBytes = int.from_bytes(b'East_Asia', byteorder=sys.byteorder)  # creating an int from bytes
print(East_AsiaBytes)
East_AsiaAscii = int.to_bytes(East_AsiaBytes, length=9, byteorder=sys.byteorder)
print(East_AsiaAscii)

# output is:
# 1796932664024362082629
# b'East_Asia'

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
print('\n\n')
EstoniaBytes = int.from_bytes(b'Estonia', byteorder=sys.byteorder)  # creating an int from bytes
print(EstoniaBytes)
EstoniaAscii = int.to_bytes(EstoniaBytes, length=7, byteorder=sys.byteorder)
print(EstoniaAscii)

# output is:
# 27418995778155333
# b'Estonia'


print('\n\n')
EuropeBytes = int.from_bytes(b'Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(EuropeBytes)
EuropeAscii = int.to_bytes(EuropeBytes, length=6, byteorder=sys.byteorder)
print(EuropeAscii)

# output is:
# 111533580514629
# b'Europe'

print('\n\n')
Europe_IndividualsBytes = int.from_bytes(b'Europe_Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_IndividualsBytes)
Europe_IndividualsAscii = int.to_bytes(Europe_IndividualsBytes, length=18, byteorder=sys.byteorder)
print(Europe_IndividualsAscii)

# output is:
# 10054792922430809867902102961034118644790597
# b'Europe_Individuals'



print('\n\n')
Europe_Individuals_Middle_EastBytes = int.from_bytes(b'Europe_Individuals_Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_Individuals_Middle_EastBytes)
Europe_Individuals_Middle_EastAscii = int.to_bytes(Europe_Individuals_Middle_EastBytes, length=30, byteorder=sys.byteorder)
print(Europe_Individuals_Middle_EastAscii)

# output is:
# 803713213924968946004570530890938146356423406018987839112189083435300165
# b'Europe_Individuals_Middle_East'

print('\n\n')
Europe_Japan_USABytes = int.from_bytes(b'Europe_Japan_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_Japan_USABytes)
Europe_Japan_USAAscii = int.to_bytes(Europe_Japan_USABytes, length=16, byteorder=sys.byteorder)
print(Europe_Japan_USAAscii)

# output is:
# 86832511930930819263603543771519808837
# b'Europe_Japan_USA'

# Europe_Middle_East
print('\n\n')
Europe_Middle_EastBytes = int.from_bytes(b'Europe_Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_Middle_EastBytes)
Europe_Middle_EastAscii = int.to_bytes(Europe_Middle_EastBytes, length=18, byteorder=sys.byteorder)
print(Europe_Middle_EastAscii)

# output is:
# 10144286935599035412558109646840913932219717
# b'Europe_Middle_East'

# Europe_Middle_East_North_America
print('\n\n')
Europe_Middle_East_North_AmericaBytes = int.from_bytes(b'Europe_Middle_East_North_America', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_Middle_East_North_AmericaBytes)
Europe_Middle_East_North_AmericaAscii = int.to_bytes(Europe_Middle_East_North_AmericaBytes, length=32, byteorder=sys.byteorder)
print(Europe_Middle_East_North_AmericaAscii)

# output is:
# 44049991939471719292781853637477999382754235777045428286303327005162211538245
# b'Europe_Middle_East_North_America'

print('\n\n')
Europe_NATOBytes = int.from_bytes(b'Europe_NATO', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_NATOBytes)
Europe_NATOAscii = int.to_bytes(Europe_NATOBytes, length=11, byteorder=sys.byteorder)
print(Europe_NATOAscii)

# output is:
# 95903023219825537446999365
# b'Europe_NATO'


print('\n\n')
Europe_NATO_UkraineBytes = int.from_bytes(b'Europe_NATO_Ukraine', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_NATO_UkraineBytes)
Europe_NATO_UkraineAscii = int.to_bytes(Europe_NATO_UkraineBytes, length=19, byteorder=sys.byteorder)
print(Europe_NATO_UkraineAscii)

# output is:
# 2261993475681827677693093247589969742749922629
# b'Europe_NATO_Ukraine'

# Europe_North_America
print('\n\n')
Europe_North_AmericaBytes = int.from_bytes(b'Europe_North_America', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_North_AmericaBytes)
Europe_North_AmericaAscii = int.to_bytes(Europe_North_AmericaBytes, length=20, byteorder=sys.byteorder)
print(Europe_North_AmericaAscii)

# output is:
# 555989064261598943201993414997543446447190603077
# b'Europe_North_America'

# Europe_Russia
print('\n\n')
Europe_RussiaBytes = int.from_bytes(b'Europe_Russia', byteorder=sys.byteorder)  # creating an int from bytes
print(Europe_RussiaBytes)
Europe_RussiaAscii = int.to_bytes(Europe_RussiaBytes, length=13, byteorder=sys.byteorder)
print(Europe_RussiaAscii)

# output is:
# 7717767261620487822145651635525
# b'Europe_Russia'

# Finland
print('\n\n')
FinlandBytes = int.from_bytes(b'Finland', byteorder=sys.byteorder)  # creating an int from bytes
print(FinlandBytes)
FinlandAscii = int.to_bytes(FinlandBytes, length=7, byteorder=sys.byteorder)
print(FinlandAscii)

# output is:
# 28268862381123910
# b'Finland'


print('\n\n')
FranceBytes = int.from_bytes(b'France', byteorder=sys.byteorder)  # creating an int from bytes
print(FranceBytes)
FranceAscii = int.to_bytes(FranceBytes, length=6, byteorder=sys.byteorder)
print(FranceAscii)

# output is:
# 111477728047686
# b'France'

print('\n\n')
France_Germany_JapanBytes = int.from_bytes(b'France_Germany_Japan', byteorder=sys.byteorder)  # creating an int from bytes
print(France_Germany_JapanBytes)
France_Germany_JapanAscii = int.to_bytes(France_Germany_JapanBytes, length=20, byteorder=sys.byteorder)
print(France_Germany_JapanAscii)

# output is:
# 630161946757152369395487029780148113741199798854
# b'France_Germany_Japan'



# France_Germany_UK
print('\n\n')
France_Germany_UKBytes = int.from_bytes(b'France_Germany_UK', byteorder=sys.byteorder)  # creating an int from bytes
print(France_Germany_UKBytes)
France_Germany_UKAscii = int.to_bytes(France_Germany_UKBytes, length=17, byteorder=sys.byteorder)
print(France_Germany_UKAscii)

# output is:
# 25634657629830475695080879593172735455814
# b'France_Germany_UK'

print('\n\n')
France_South_KoreaBytes = int.from_bytes(b'France_South_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(France_South_KoreaBytes)
France_South_KoreaAscii = int.to_bytes(France_South_KoreaBytes, length=18, byteorder=sys.byteorder)
print(France_South_KoreaAscii)

# output is:
# 8484412364304969210251414251757639397634630
# b'France_South_Korea'


print('\n\n')
GeorgiaBytes = int.from_bytes(b'Georgia', byteorder=sys.byteorder)  # creating an int from bytes
print(GeorgiaBytes)
GeorgiaAscii = int.to_bytes(GeorgiaBytes, length=7, byteorder=sys.byteorder)
print(GeorgiaAscii)

# output is:
# 27418965763384647
# b'Georgia'

print('\n\n')
GermanyBytes = int.from_bytes(b'Germany', byteorder=sys.byteorder)  # creating an int from bytes
print(GermanyBytes)
GermanyAscii = int.to_bytes(GermanyBytes, length=7, byteorder=sys.byteorder)
print(GermanyAscii)

# output is:
# 34179836909086023
# b'Germany'

# Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA
print('\n\n')
Germany_Israel_Jordan_Saudi_Arabia_Turkey_USABytes = int.from_bytes(b'Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Germany_Israel_Jordan_Saudi_Arabia_Turkey_USABytes)
Germany_Israel_Jordan_Saudi_Arabia_Turkey_USAAscii = int.to_bytes(Germany_Israel_Jordan_Saudi_Arabia_Turkey_USABytes, length=45, byteorder=sys.byteorder)
print(Germany_Israel_Jordan_Saudi_Arabia_Turkey_USAAscii)

# output is:
# 599295972025478897151354840582044557016535795860902688018405021916292137618025118208661378066604542240384327
# b'Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA'

# Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals
print('\n\n')
Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsBytes = int.from_bytes(b'Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsBytes)
Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsAscii = int.to_bytes(Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsBytes, length=56, byteorder=sys.byteorder)
print(Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_IndividualsAscii)

# output is:
# 327711598681358806473535046145613536099155348676132340178557461795987392748287290496883585939262089223124598924634327352459624440816967
# b'Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals'

# Germany_Turkey
print('\n\n')
Germany_TurkeyBytes = int.from_bytes(b'Germany_Turkey', byteorder=sys.byteorder)  # creating an int from bytes
print(Germany_TurkeyBytes)
Germany_TurkeyAscii = int.to_bytes(Germany_TurkeyBytes, length=14, byteorder=sys.byteorder)
print(Germany_TurkeyAscii)

# output is:
# 2462206859723460424033855417247047
# b'Germany_Turkey'

# Global_Unlisted
print('\n\n')
Global_UnlistedBytes = int.from_bytes(b'Global_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Global_UnlistedBytes)
Global_UnlistedAscii = int.to_bytes(Global_UnlistedBytes, length=15, byteorder=sys.byteorder)
print(Global_UnlistedAscii)

# output is:
# 521287435408528627617000934358346823
# b'Global_Unlisted'

print('\n\n')
IndiaBytes = int.from_bytes(b'India', byteorder=sys.byteorder)  # creating an int from bytes
print(IndiaBytes)
IndiaAscii = int.to_bytes(IndiaBytes, length=5, byteorder=sys.byteorder)
print(IndiaAscii)

# output is:
# 418380017225
# b'India'

# India_Italy_Saudi_Arabia_Scotland_UAE

print('\n\n')
India_Italy_Saudi_Arabia_Scotland_UAEBytes = int.from_bytes(b'India_Italy_Saudi_Arabia_Scotland_UAE', byteorder=sys.byteorder)  # creating an int from bytes
print(India_Italy_Saudi_Arabia_Scotland_UAEBytes)
India_Italy_Saudi_Arabia_Scotland_UAEAscii = int.to_bytes(India_Italy_Saudi_Arabia_Scotland_UAEBytes, length=37, byteorder=sys.byteorder)
print(India_Italy_Saudi_Arabia_Scotland_UAEAscii)

# output is:
# 34442224644743318243735343714622843513968332852566796037896488177251263385944346459401801
# b'India_Italy_Saudi_Arabia_Scotland_UAE'


print('\n\n')
India_PakistanBytes = int.from_bytes(b'India_Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(India_PakistanBytes)
India_PakistanAscii = int.to_bytes(India_PakistanBytes, length=14, byteorder=sys.byteorder)
print(India_PakistanAscii)

# output is:
# 2238786227951005213617790040436297
# b'India_Pakistan'

print('\n\n')
IndividualsBytes = int.from_bytes(b'Individuals', byteorder=sys.byteorder)  # creating an int from bytes
print(IndividualsBytes)
IndividualsAscii = int.to_bytes(IndividualsBytes, length=11, byteorder=sys.byteorder)
print(IndividualsAscii)

# output is:
# 139538282629009384004677193
# b'Individuals'


print('\n\n')
Individuals_IranBytes = int.from_bytes(b'Individuals_Iran', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_IranBytes)
Individuals_IranAscii = int.to_bytes(Individuals_IranBytes, length=16, byteorder=sys.byteorder)
print(Individuals_IranAscii)

# output is:
# 146721050339509918346768000002986110537
# b'Individuals_Iran'


print('\n\n')
Individuals_LatviaBytes = int.from_bytes(b'Individuals_Latvia', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_LatviaBytes)
Individuals_LatviaAscii = int.to_bytes(Individuals_LatviaBytes, length=18, byteorder=sys.byteorder)
print(Individuals_LatviaAscii)

# output is:
# 8485778837090825286018691921867596733115977
# b'Individuals_Latvia'

print('\n\n')
Individuals_MultipleBytes = int.from_bytes(b'Individuals_Multiple', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_MultipleBytes)
Individuals_MultipleAscii = int.to_bytes(Individuals_MultipleBytes, length=20, byteorder=sys.byteorder)
print(Individuals_MultipleAscii)

# output is:
# 579026340795075577836801232462293422175315848777
# b'Individuals_Multiple'

print('\n\n')
Individuals_NATO_UkraineBytes = int.from_bytes(b'Individuals_NATO_Ukraine', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_NATO_UkraineBytes)
Individuals_NATO_UkraineAscii = int.to_bytes(Individuals_NATO_UkraineBytes, length=24, byteorder=sys.byteorder)
print(Individuals_NATO_UkraineAscii)

# output is:
# 2487088128465618221363062841210218726675521088406281285193
# b'Individuals_NATO_Ukraine'

print('\n\n')
Individuals_Sri_LankaBytes = int.from_bytes(b'Individuals_Sri_Lanka', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_Sri_LankaBytes)
Individuals_Sri_LankaAscii = int.to_bytes(Individuals_Sri_LankaBytes, length=21, byteorder=sys.byteorder)
print(Individuals_Sri_LankaAscii)

# output is:
# 142378982391427591699701078127165432569250395221577
# b'Individuals_Sri_Lanka'

print('\n\n')
Individuals_USABytes = int.from_bytes(b'Individuals_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_USABytes)
Individuals_USAAscii = int.to_bytes(Individuals_USABytes, length=15, byteorder=sys.byteorder)
print(Individuals_USAAscii)

# output is:
# 339189499736294812625156247350701641
# b'Individuals_USA'

print('\n\n')
Individuals_VietnamBytes = int.from_bytes(b'Individuals_Vietnam', byteorder=sys.byteorder)  # creating an int from bytes
print(Individuals_VietnamBytes)
Individuals_VietnamAscii = int.to_bytes(Individuals_VietnamBytes, length=19, byteorder=sys.byteorder)
print(Individuals_VietnamAscii)

# output is:
# 2439268704152585959516329496284772107676839497
# b'Individuals_Vietnam'

print('\n\n')
IndonesiaBytes = int.from_bytes(b'Indonesia', byteorder=sys.byteorder)  # creating an int from bytes
print(IndonesiaBytes)
IndonesiaAscii = int.to_bytes(IndonesiaBytes, length=9, byteorder=sys.byteorder)
print(IndonesiaAscii)

# output is:
# 1796932703671120326217
# b'Indonesia'

# Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang
print('\n\n')
Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangBytes = int.from_bytes(b'Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang', byteorder=sys.byteorder)  # creating an int from bytes
print(Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangBytes)
Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangAscii = int.to_bytes(Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangBytes, length=56, byteorder=sys.byteorder)
print(Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_XinjiangAscii)

# output is:
# 293663212810770379135919508023638240622048108390492839331378670437676906065559292090827246281641117934618254935537732048405501613207113
# b'Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang'

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
print('\n\n')
Iran_Israel_Middle_EastBytes = int.from_bytes(b'Iran_Israel_Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Iran_Israel_Middle_EastBytes)
Iran_Israel_Middle_EastAscii = int.to_bytes(Iran_Israel_Middle_EastBytes, length=23, byteorder=sys.byteorder)
print(Iran_Israel_Middle_EastAscii)

# output is:
# 11153761441187306308117234849995952050181433635710792265
# b'Iran_Israel_Middle_East'

# Iran_Syria
print('\n\n')
Iran_SyriaBytes = int.from_bytes(b'Iran_Syria', byteorder=sys.byteorder)  # creating an int from bytes
print(Iran_SyriaBytes)
Iran_SyriaAscii = int.to_bytes(Iran_SyriaBytes, length=10, byteorder=sys.byteorder)
print(Iran_SyriaAscii)

# output is:
# 460014705681956933300809
# b'Iran_Syria'

# Iraq_Pakistan_Tajikistan
print('\n\n')
Iraq_Pakistan_TajikistanBytes = int.from_bytes(b'Iraq_Pakistan_Tajikistan', byteorder=sys.byteorder)  # creating an int from bytes
print(Iraq_Pakistan_TajikistanBytes)
Iraq_Pakistan_TajikistanAscii = int.to_bytes(Iraq_Pakistan_TajikistanBytes, length=24, byteorder=sys.byteorder)
print(Iraq_Pakistan_TajikistanAscii)

# output is:
# 2706526475567613707123455675952615284393656146857744757321
# b'Iraq_Pakistan_Tajikistan'

print('\n\n')
IrelandBytes = int.from_bytes(b'Ireland', byteorder=sys.byteorder)  # creating an int from bytes
print(IrelandBytes)
IrelandAscii = int.to_bytes(IrelandBytes, length=7, byteorder=sys.byteorder)
print(IrelandAscii)

# output is:
# 28268862380536393
# b'Ireland'

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
Israel_Saudi_Arabia_USABytes = int.from_bytes(b'Israel_Saudi_Arabia_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Israel_Saudi_Arabia_USABytes)
Israel_Saudi_Arabia_USAAscii = int.to_bytes(Israel_Saudi_Arabia_USABytes, length=23, byteorder=sys.byteorder)
print(Israel_Saudi_Arabia_USAAscii)

# output is:
# 6256941893723329418780205680006274667958179856383112009
# b'Israel_Saudi_Arabia_USA'

print('\n\n')
Israel_Sudan_Syria_Middle_EastBytes = int.from_bytes(b'Israel_Sudan_Syria_Middle_East', byteorder=sys.byteorder)  # creating an int from bytes
print(Israel_Sudan_Syria_Middle_EastBytes)
Israel_Sudan_Syria_Middle_EastAscii = int.to_bytes(Israel_Sudan_Syria_Middle_EastBytes, length=30, byteorder=sys.byteorder)
print(Israel_Sudan_Syria_Middle_EastAscii)

# output is:
# 803713213924968946004570530889369126979850478811228792355694693835764553
# b'Israel_Sudan_Syria_Middle_East'

print('\n\n')
ItalyBytes = int.from_bytes(b'Italy', byteorder=sys.byteorder)  # creating an int from bytes
print(ItalyBytes)
ItalyAscii = int.to_bytes(ItalyBytes, length=5, byteorder=sys.byteorder)
print(ItalyAscii)

# output is:
# 521509368905
# b'Italy'

# Italy_France_Germany_Poland_Spain_Turkey_USA
print('\n\n')
Italy_France_Germany_Poland_Spain_Turkey_USABytes = int.from_bytes(b'Italy_France_Germany_Poland_Spain_Turkey_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Italy_France_Germany_Poland_Spain_Turkey_USABytes)
Italy_France_Germany_Poland_Spain_Turkey_USAAscii = int.to_bytes(Italy_France_Germany_Poland_Spain_Turkey_USABytes, length=44, byteorder=sys.byteorder)
print(Italy_France_Germany_Poland_Spain_Turkey_USAAscii)

# output is:
# 2340999890724526941997479847528907046777487003526924268424622113184721296010098148746237170904876170966089
# b'Italy_France_Germany_Poland_Spain_Turkey_USA'

# Japan
print('\n\n')
JapanBytes = int.from_bytes(b'Japan', byteorder=sys.byteorder)  # creating an int from bytes
print(JapanBytes)
JapanAscii = int.to_bytes(JapanBytes, length=5, byteorder=sys.byteorder)
print(JapanAscii)

# output is:
# 474081157450
# b'Japan'

# Japan_Multiple_Unlisted
print('\n\n')
Japan_Multiple_UnlistedBytes = int.from_bytes(b'Japan_Multiple_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Japan_Multiple_UnlistedBytes)
Japan_Multiple_UnlistedAscii = int.to_bytes(Japan_Multiple_UnlistedBytes, length=23, byteorder=sys.byteorder)
print(Japan_Multiple_UnlistedAscii)

# output is:
# 9616055909821526137339212106786338705010904763416469834
# b'Japan_Multiple_Unlisted'

print('\n\n')
Japan_UnlistedBytes = int.from_bytes(b'Japan_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Japan_UnlistedBytes)
Japan_UnlistedAscii = int.to_bytes(Japan_UnlistedBytes, length=14, byteorder=sys.byteorder)
print(Japan_UnlistedAscii)

# output is:
# 2036279044564564951628918490685770
# b'Japan_Unlisted'

print('\n\n')
KazakhstanBytes = int.from_bytes(b'Kazakhstan', byteorder=sys.byteorder)  # creating an int from bytes
print(KazakhstanBytes)
KazakhstanAscii = int.to_bytes(KazakhstanBytes, length=10, byteorder=sys.byteorder)
print(KazakhstanAscii)

# output is:
# 521258038456151927578955
# b'Kazakhstan'


print('\n\n')
LebanonBytes = int.from_bytes(b'Lebanon', byteorder=sys.byteorder)  # creating an int from bytes
print(LebanonBytes)
LebanonAscii = int.to_bytes(LebanonBytes, length=7, byteorder=sys.byteorder)
print(LebanonAscii)

# output is:
# 31084767309096268
# b'Lebanon'

# Lebanon_UAE
print('\n\n')
Lebanon_UAEBytes = int.from_bytes(b'Lebanon_UAE', byteorder=sys.byteorder)  # creating an int from bytes
print(Lebanon_UAEBytes)
Lebanon_UAEAscii = int.to_bytes(Lebanon_UAEBytes, length=11, byteorder=sys.byteorder)
print(Lebanon_UAEAscii)

# output is:
# 83724410224598406217753932
# b'Lebanon_UAE'

# Libya
print('\n\n')
LibyaBytes = int.from_bytes(b'Libya', byteorder=sys.byteorder)  # creating an int from bytes
print(LibyaBytes)
LibyaAscii = int.to_bytes(LibyaBytes, length=5, byteorder=sys.byteorder)
print(LibyaAscii)

# output is:
# 418648320332
# b'Libya'

# Lithuania
print('\n\n')
LithuaniaBytes = int.from_bytes(b'Lithuania', byteorder=sys.byteorder)  # creating an int from bytes
print(LithuaniaBytes)
LithuaniaAscii = int.to_bytes(LithuaniaBytes, length=9, byteorder=sys.byteorder)
print(LithuaniaAscii)

# output is:
# 1796931291928138639692
# b'Lithuania'

print('\n\n')
MalaysiaBytes = int.from_bytes(b'Malaysia', byteorder=sys.byteorder)  # creating an int from bytes
print(MalaysiaBytes)
MalaysiaAscii = int.to_bytes(MalaysiaBytes, length=8, byteorder=sys.byteorder)
print(MalaysiaAscii)

# output is:
# 7019268459396358477
# b'Malaysia'

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
print('\n\n')
Middle_East_South_America_UK_USABytes = int.from_bytes(b'Middle_East_South_America_UK_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Middle_East_South_America_UK_USABytes)
Middle_East_South_America_UK_USAAscii = int.to_bytes(Middle_East_South_America_UK_USABytes, length=32, byteorder=sys.byteorder)
print(Middle_East_South_America_UK_USAAscii)

# output is:
# 29547572681856873838269706859280096340519948949106405771628223098370744674637
# b'Middle_East_South_America_UK_USA'

# Montenegro
print('\n\n')
MontenegroBytes = int.from_bytes(b'Montenegro', byteorder=sys.byteorder)  # creating an int from bytes
print(MontenegroBytes)
MontenegroAscii = int.to_bytes(MontenegroBytes, length=10, byteorder=sys.byteorder)
print(MontenegroAscii)

# output is:
# 526293058905474086104909
# b'Montenegro'

print('\n\n')
MultipleBytes = int.from_bytes(b'Multiple', byteorder=sys.byteorder)  # creating an int from bytes
print(MultipleBytes)
MultipleAscii = int.to_bytes(MultipleBytes, length=8, byteorder=sys.byteorder)
print(MultipleAscii)

# output is:
# 7308339893542614349
# b'Multiple'


print('\n\n')
Multiple_UnlistedBytes = int.from_bytes(b'Multiple_Unlisted', byteorder=sys.byteorder)  # creating an int from bytes
print(Multiple_UnlistedBytes)
Multiple_UnlistedAscii = int.to_bytes(Multiple_UnlistedBytes, length=17, byteorder=sys.byteorder)
print(Multiple_UnlistedAscii)

# output is:
# 34163093366933332139507271942542625371469
# b'Multiple_Unlisted'

# Netherlands
print('\n\n')
NetherlandsBytes = int.from_bytes(b'Netherlands', byteorder=sys.byteorder)  # creating an int from bytes
print(NetherlandsBytes)
NetherlandsAscii = int.to_bytes(NetherlandsBytes, length=11, byteorder=sys.byteorder)
print(NetherlandsAscii)

# output is:
# 139500742065929126696740174
# b'Netherlands'

# Netherlands_territory
print('\n\n')
Netherlands_territoryBytes = int.from_bytes(b'Netherlands_territory', byteorder=sys.byteorder)  # creating an int from bytes
print(Netherlands_territoryBytes)
Netherlands_territoryAscii = int.to_bytes(Netherlands_territoryBytes, length=21, byteorder=sys.byteorder)
print(Netherlands_territoryAscii)

# output is:
# 177495008588537150289569034074503311374442523026766
# b'Netherlands_territory'

# NGOs_UN
print('\n\n')
NGOs_UNBytes = int.from_bytes(b'NGOs_UN', byteorder=sys.byteorder)  # creating an int from bytes
print(NGOs_UNBytes)
NGOs_UNAscii = int.to_bytes(NGOs_UNBytes, length=7, byteorder=sys.byteorder)
print(NGOs_UNAscii)

# output is:
# 22048916628260686
# b'NGOs_UN'

# North_America_Pakistan_Russia_Saudi_Arabia_Turkey
print('\n\n')
North_America_Pakistan_Russia_Saudi_Arabia_TurkeyBytes = int.from_bytes(b'North_America_Pakistan_Russia_Saudi_Arabia_Turkey', byteorder=sys.byteorder)  # creating an int from bytes
print(North_America_Pakistan_Russia_Saudi_Arabia_TurkeyBytes)
North_America_Pakistan_Russia_Saudi_Arabia_TurkeyAscii = int.to_bytes(North_America_Pakistan_Russia_Saudi_Arabia_TurkeyBytes, length=49, byteorder=sys.byteorder)
print(North_America_Pakistan_Russia_Saudi_Arabia_TurkeyAscii)

# output is:
# 4783252672609565942086426335538687073561207333492445561892257896545894802454521445006773297625430995809981742445653838
# b'North_America_Pakistan_Russia_Saudi_Arabia_Turkey'

print('\n\n')
North_KoreaBytes = int.from_bytes(b'North_Korea', byteorder=sys.byteorder)  # creating an int from bytes
print(North_KoreaBytes)
North_KoreaAscii = int.to_bytes(North_KoreaBytes, length=11, byteorder=sys.byteorder)
print(North_KoreaAscii)

# output is:
# 117744874465821730700160846
# b'North_Korea'

# Norway
print('\n\n')
NorwayBytes = int.from_bytes(b'Norway', byteorder=sys.byteorder)  # creating an int from bytes
print(NorwayBytes)
NorwayAscii = int.to_bytes(NorwayBytes, length=6, byteorder=sys.byteorder)
print(NorwayAscii)

# output is:
# 133459522776910
# b'Norway'

# Oman_UAE
print('\n\n')
Oman_UAEBytes = int.from_bytes(b'Oman_UAE', byteorder=sys.byteorder)  # creating an int from bytes
print(Oman_UAEBytes)
Oman_UAEAscii = int.to_bytes(Oman_UAEBytes, length=8, byteorder=sys.byteorder)
print(Oman_UAEAscii)

# output is:
# 4990363730465353039
# b'Oman_UAE'

print('\n\n')
PakistanBytes = int.from_bytes(b'Pakistan', byteorder=sys.byteorder)  # creating an int from bytes
print(PakistanBytes)
PakistanAscii = int.to_bytes(PakistanBytes, length=8, byteorder=sys.byteorder)
print(PakistanAscii)

# output is:
# 7953766455951712592
# b'Pakistan'

# Philippines
print('\n\n')
PhilippinesBytes = int.from_bytes(b'Philippines', byteorder=sys.byteorder)  # creating an int from bytes
print(PhilippinesBytes)
PhilippinesAscii = int.to_bytes(PhilippinesBytes, length=11, byteorder=sys.byteorder)
print(PhilippinesAscii)

# output is:
# 139505465009996466775222352
# b'Philippines'

# Qatar
print('\n\n')
QatarBytes = int.from_bytes(b'Qatar', byteorder=sys.byteorder)  # creating an int from bytes
print(QatarBytes)
QatarAscii = int.to_bytes(QatarBytes, length=5, byteorder=sys.byteorder)
print(QatarAscii)

# output is:
# 491261288785
# b'Qatar'

# Qatar_Saudi_Arabia
print('\n\n')
Qatar_Saudi_ArabiaBytes = int.from_bytes(b'Qatar_Saudi_Arabia', byteorder=sys.byteorder)  # creating an int from bytes
print(Qatar_Saudi_ArabiaBytes)
Qatar_Saudi_ArabiaAscii = int.to_bytes(Qatar_Saudi_ArabiaBytes, length=18, byteorder=sys.byteorder)
print(Qatar_Saudi_ArabiaAscii)

# output is:
# 8485752154221198716887260754064792649752913
# b'Qatar_Saudi_Arabia'

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
print('\n\n')
Saudi_Arabia_South_Korea_USABytes = int.from_bytes(b'Saudi_Arabia_South_Korea_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Saudi_Arabia_South_Korea_USABytes)
Saudi_Arabia_South_Korea_USAAscii = int.to_bytes(Saudi_Arabia_South_Korea_USABytes, length=28, byteorder=sys.byteorder)
print(Saudi_Arabia_South_Korea_USAAscii)

# output is:
# 6879580366467208809293824059458255306814834697835999905549076750675
# b'Saudi_Arabia_South_Korea_USA'

# Saudi_Arabia_USA
print('\n\n')
Saudi_Arabia_USABytes = int.from_bytes(b'Saudi_Arabia_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(Saudi_Arabia_USABytes)
Saudi_Arabia_USAAscii = int.to_bytes(Saudi_Arabia_USABytes, length=16, byteorder=sys.byteorder)
print(Saudi_Arabia_USAAscii)

# output is:
# 86832511926917119432226067621359214931
# b'Saudi_Arabia_USA'

# Scotland
print('\n\n')
ScotlandBytes = int.from_bytes(b'Scotland', byteorder=sys.byteorder)  # creating an int from bytes
print(ScotlandBytes)
ScotlandAscii = int.to_bytes(ScotlandBytes, length=8, byteorder=sys.byteorder)
print(ScotlandAscii)

# output is:
# 7236828769668784979
# b'Scotland'

# Singapore
print('\n\n')
SingaporeBytes = int.from_bytes(b'Singapore', byteorder=sys.byteorder)  # creating an int from bytes
print(SingaporeBytes)
SingaporeAscii = int.to_bytes(SingaporeBytes, length=9, byteorder=sys.byteorder)
print(SingaporeAscii)

# output is:
# 1871367084451052808531
# b'Singapore'

# South_Africa
print('\n\n')
South_AfricaBytes = int.from_bytes(b'South_Africa', byteorder=sys.byteorder)  # creating an int from bytes
print(South_AfricaBytes)
South_AfricaAscii = int.to_bytes(South_AfricaBytes, length=12, byteorder=sys.byteorder)
print(South_AfricaAscii)

# output is:
# 30140227567590121037825929043
# b'South_Africa'

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
print('\n\n')
South_Korea_USABytes = int.from_bytes(b'South_Korea_USA', byteorder=sys.byteorder)  # creating an int from bytes
print(South_Korea_USABytes)
South_Korea_USAAscii = int.to_bytes(South_Korea_USABytes, length=15, byteorder=sys.byteorder)
print(South_Korea_USAAscii)

# output is:
# 339189499714501404461968594046381907
# b'South_Korea_USA'

# Southeast_Asia
print('\n\n')
Southeast_AsiaBytes = int.from_bytes(b'Southeast_Asia', byteorder=sys.byteorder)  # creating an int from bytes
print(Southeast_AsiaBytes)
Southeast_AsiaAscii = int.to_bytes(Southeast_AsiaBytes, length=14, byteorder=sys.byteorder)
print(Southeast_AsiaAscii)

# output is:
# 1975748358425290468427058206043987
# b'Southeast_Asia'

print('\n\n')
SwedenBytes = int.from_bytes(b'Sweden', byteorder=sys.byteorder)  # creating an int from bytes
print(SwedenBytes)
SwedenAscii = int.to_bytes(SwedenBytes, length=6, byteorder=sys.byteorder)
print(SwedenAscii)

# output is:
# 121381755123539
# b'Sweden'

# Switzerland
print('\n\n')
SwitzerlandBytes = int.from_bytes(b'Switzerland', byteorder=sys.byteorder)  # creating an int from bytes
print(SwitzerlandBytes)
SwitzerlandAscii = int.to_bytes(SwitzerlandBytes, length=11, byteorder=sys.byteorder)
print(SwitzerlandAscii)

# output is:
# 121413839423173608325347155
# b'Switzerland'

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
TehranBytes = int.from_bytes(b'Tehran', byteorder=sys.byteorder)  # creating an int from bytes
print(TehranBytes)
TehranAscii = int.to_bytes(TehranBytes, length=6, byteorder=sys.byteorder)
print(TehranAscii)

# output is:
# 121364810327380
# b'Tehran'

# Tibet
print('\n\n')
TibetBytes = int.from_bytes(b'Tibet', byteorder=sys.byteorder)  # creating an int from bytes
print(TibetBytes)
TibetAscii = int.to_bytes(TibetBytes, length=5, byteorder=sys.byteorder)
print(TibetAscii)

# output is:
# 499917154644
# b'Tibet'

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

print('\n\n')
UkraineBytes = int.from_bytes(b'Ukraine', byteorder=sys.byteorder)  # creating an int from bytes
print(UkraineBytes)
UkraineAscii = int.to_bytes(UkraineBytes, length=7, byteorder=sys.byteorder)
print(UkraineAscii)

# output is:
# 28550371533286229
# b'Ukraine'

# UN
print('\n\n')
UNBytes = int.from_bytes(b'UN', byteorder=sys.byteorder)  # creating an int from bytes
print(UNBytes)
UNAscii = int.to_bytes(UNBytes, length=2, byteorder=sys.byteorder)
print(UNAscii)

# output is:
# 20053
# b'UN'

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
print('\n\n')
USA_EuropeBytes = int.from_bytes(b'USA_Europe', byteorder=sys.byteorder)  # creating an int from bytes
print(USA_EuropeBytes)
USA_EuropeAscii = int.to_bytes(USA_EuropeBytes, length=10, byteorder=sys.byteorder)
print(USA_EuropeAscii)

# output is:
# 479033080716116002689877
# b'USA_Europe'

# USA_Western_World
print('\n\n')
USA_Western_WorldBytes = int.from_bytes(b'USA_Western_World', byteorder=sys.byteorder)  # creating an int from bytes
print(USA_Western_WorldBytes)
USA_Western_WorldAscii = int.to_bytes(USA_Western_WorldBytes, length=17, byteorder=sys.byteorder)
print(USA_Western_WorldAscii)

# output is:
# 34172387495750340973031615562330792874837
# b'USA_Western_World'

# Venezuela
print('\n\n')
VenezuelaBytes = int.from_bytes(b'Venezuela', byteorder=sys.byteorder)  # creating an int from bytes
print(VenezuelaBytes)
VenezuelaAscii = int.to_bytes(VenezuelaBytes, length=9, byteorder=sys.byteorder)
print(VenezuelaAscii)

# output is:
# 1797144953447118693718
# b'Venezuela'

print('\n\n')
Western_WorldBytes = int.from_bytes(b'Western_World', byteorder=sys.byteorder)  # creating an int from bytes
print(Western_WorldBytes)
Western_WorldAscii = int.to_bytes(Western_WorldBytes, length=13, byteorder=sys.byteorder)
print(Western_WorldAscii)

# output is:
# 7956378975824997986907049911639
# b'Western_World'

# Xinjiang
print('\n\n')
XinjiangBytes = int.from_bytes(b'Xinjiang', byteorder=sys.byteorder)  # creating an int from bytes
print(XinjiangBytes)
XinjiangAscii = int.to_bytes(XinjiangBytes, length=8, byteorder=sys.byteorder)
print(XinjiangAscii)

# output is:
# 7453001538729830744
# b'Xinjiang'



# ----- output of program---------------------------------------------------------------------------------------------


# 133442057845059666670216769
# b'Afghanistan'
#
#
#
# 5547024738073957303662399576029973568509146976390336004265898740432675875991326601817987176556771282997325216339676316688169204494214088844865
# b'Afghanistan_Application_Users_India_Individuals_Middle_East'
#
#
#
# 107079598761537
# b'Africa'
#
#
#
# 117763779069479634143962689
# b'Africa_Asia'
#
#
#
# 1796569596582678195265
# b'Al_Quaida'
#
#
#
# 39284530948651148542945322099333464617025
# b'Application_Users'
#
#
#
# 3111807686350090077732346834447189654644633344498384566960921427079233
# b'Application_Users_Individuals'
#
#
#
# 10572363095725242809903474363794222115376060650679726145
# b'Application_Users_Japan'
#
#
#
# 27418995609924161
# b'Armenia'
#
#
#
# 1634300737
# b'Asia'
#
#
#
# 1936429723561952681582869571271737150404117317300876807438770316145334861458666305
# b'Asia_Canada_Europe_Middle_East_USA'
#
#
#
# 26873360808337585803091529125126950972081670239456308127962067777
# b'Asia_Europe_Middle_East_USA'
#
#
#
# 611316441071925721528505149291982085844431624011733040460609
# b'Asia_Europe_North_America'
#
#
#
# 8483719852624495593292136065139819009372993
# b'Asia_South_America'
#
#
#
# 4707199903676855105
# b'Asia_USA'
#
#
#
# 1796930728965501580609
# b'Australia'
#
#
#
# 139534466882955655784457473920909684382362106944851677537702575567474562215766014437633627337749825
# b'Australia_Canada_Japan_Switzerland_UK_USA'
#
#
#
# 495726009159212053789849057507327564583030099413608231039652233206430848978550748481
# b'Australia_Canada_New_Zealand_UK_USA'
#
#
#
# 27419013041845569
# b'Austria'
#
#
#
# 41314988655876265391272827414481922914912132198580508749628405057
# b'Austria_Germany_Switzerland'
#
#
#
# 31078114690359618
# b'Bahrain'
#
#
#
# 9330208112349500424797783435764896148944012388223182146
# b'Belarus_Mongolia_Russia'
#
#
#
# 30809868028634434
# b'Belgium'
#
#
#
# 119200280572482
# b'Brazil'
#
#
#
# 7019251923789111619
# b'Cambodia'
#
#
#
# 107083759247683
# b'Canada'
#
#
#
# 1761172573677115074610677974231769886272027516418405464348645768716611
# b'Canada_France_Multiple_UK_USA'
#
#
#
# 505669108189612364370267082941424963
# b'Central_America'
#
#
#
# 41729666698114283016919014524090844581596341132174623587355747651
# b'Central_Asia_Eastern_Europe'
#
#
#
# 2887559549285678575025028014159333265348920949327583776587248794714267494332130627
# b'Central_Asia_Eastern_Europe_Russia'
#
#
#
# 6256941893813146631859154412586712377514069709544121667
# b'Central_Asia_Europe_USA'
#
#
#
# 435610544195
# b'Chile'
#
#
#
# 418464229443
# b'China'
#
#
#
# 9620768797959008789195953629251
# b'China_Germany'
#
#
#
# 39276534853245351046492589691522312136771
# b'China_Individuals'
#
#
#
# 2238786227951005213617790124648515
# b'China_Pakistan'
#
#
#
# 4707199903439868739
# b'CSIS_USA'
#
#
#
# 2016311051235894369754033219271235
# b'Czech_Republic'
#
#
#
# 185478191754227285249969174530609441383227936193346174183635523
# b'Czech_Republic_Individuals'
#
#
#
# 30243585281385796
# b'Denmark'
#
#
#
# 1796932664024362082629
# b'East_Asia'
#
#
#
# 2057431415377846504395799230898501
# b'Eastern_Europe'
#
#
#
# 500103210821
# b'Egypt'
#
#
#
# 27418995778155333
# b'Estonia'
#
#
#
# 111533580514629
# b'Europe'
#
#
#
# 10054792922430809867902102961034118644790597
# b'Europe_Individuals'
#
#
#
# 803713213924968946004570530890938146356423406018987839112189083435300165
# b'Europe_Individuals_Middle_East'
#
#
#
# 86832511930930819263603543771519808837
# b'Europe_Japan_USA'
#
#
#
# 10144286935599035412558109646840913932219717
# b'Europe_Middle_East'
#
#
#
# 44049991939471719292781853637477999382754235777045428286303327005162211538245
# b'Europe_Middle_East_North_America'
#
#
#
# 95903023219825537446999365
# b'Europe_NATO'
#
#
#
# 2261993475681827677693093247589969742749922629
# b'Europe_NATO_Ukraine'
#
#
#
# 555989064261598943201993414997543446447190603077
# b'Europe_North_America'
#
#
#
# 7717767261620487822145651635525
# b'Europe_Russia'
#
#
#
# 28268862381123910
# b'Finland'
#
#
#
# 111477728047686
# b'France'
#
#
#
# 630161946757152369395487029780148113741199798854
# b'France_Germany_Japan'
#
#
#
# 25634657629830475695080879593172735455814
# b'France_Germany_UK'
#
#
#
# 8484412364304969210251414251757639397634630
# b'France_South_Korea'
#
#
#
# 27418965763384647
# b'Georgia'
#
#
#
# 34179836909086023
# b'Germany'
#
#
#
# 599295972025478897151354840582044557016535795860902688018405021916292137618025118208661378066604542240384327
# b'Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA'
#
#
#
# 327711598681358806473535046145613536099155348676132340178557461795987392748287290496883585939262089223124598924634327352459624440816967
# b'Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals'
#
#
#
# 2462206859723460424033855417247047
# b'Germany_Turkey'
#
#
#
# 521287435408528627617000934358346823
# b'Global_Unlisted'
#
#
#
# 418380017225
# b'India'
#
#
#
# 34442224644743318243735343714622843513968332852566796037896488177251263385944346459401801
# b'India_Italy_Saudi_Arabia_Scotland_UAE'
#
#
#
# 2238786227951005213617790040436297
# b'India_Pakistan'
#
#
#
# 139538282629009384004677193
# b'Individuals'
#
#
#
# 146721050339509918346768000002986110537
# b'Individuals_Iran'
#
#
#
# 8485778837090825286018691921867596733115977
# b'Individuals_Latvia'
#
#
#
# 579026340795075577836801232462293422175315848777
# b'Individuals_Multiple'
#
#
#
# 2487088128465618221363062841210218726675521088406281285193
# b'Individuals_NATO_Ukraine'
#
#
#
# 142378982391427591699701078127165432569250395221577
# b'Individuals_Sri_Lanka'
#
#
#
# 339189499736294812625156247350701641
# b'Individuals_USA'
#
#
#
# 2439268704152585959516329496284772107676839497
# b'Individuals_Vietnam'
#
#
#
# 1796932703671120326217
# b'Indonesia'
#
#
#
# 293663212810770379135919508023638240622048108390492839331378670437676906065559292090827246281641117934618254935537732048405501613207113
# b'Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang'
#
#
#
# 8586795105461350372667137748553
# b'International'
#
#
#
# 1851880009
# b'Iran'
#
#
#
# 11153761441187306308117234849995952050181433635710792265
# b'Iran_Israel_Middle_East'
#
#
#
# 460014705681956933300809
# b'Iran_Syria'
#
#
#
# 2706526475567613707123455675952615284393656146857744757321
# b'Iraq_Pakistan_Tajikistan'
#
#
#
# 28268862380536393
# b'Ireland'
#
#
#
# 1397314377
# b'ISIS'
#
#
#
# 119182682387273
# b'Israel'
#
#
#
# 6256941893723329418780205680006274667958179856383112009
# b'Israel_Saudi_Arabia_USA'
#
#
#
# 803713213924968946004570530889369126979850478811228792355694693835764553
# b'Israel_Sudan_Syria_Middle_East'
#
#
#
# 521509368905
# b'Italy'
#
#
#
# 2340999890724526941997479847528907046777487003526924268424622113184721296010098148746237170904876170966089
# b'Italy_France_Germany_Poland_Spain_Turkey_USA'
#
#
#
# 474081157450
# b'Japan'
#
#
#
# 9616055909821526137339212106786338705010904763416469834
# b'Japan_Multiple_Unlisted'
#
#
#
# 2036279044564564951628918490685770
# b'Japan_Unlisted'
#
#
#
# 521258038456151927578955
# b'Kazakhstan'
#
#
#
# 31084767309096268
# b'Lebanon'
#
#
#
# 83724410224598406217753932
# b'Lebanon_UAE'
#
#
#
# 418648320332
# b'Libya'
#
#
#
# 1796931291928138639692
# b'Lithuania'
#
#
#
# 7019268459396358477
# b'Malaysia'
#
#
#
# 122472761943373
# b'Mexico'
#
#
#
# 140780261553827770911713613
# b'Middle_East'
#
#
#
# 29547572681856873838269706859280096340519948949106405771628223098370744674637
# b'Middle_East_South_America_UK_USA'
#
#
#
# 526293058905474086104909
# b'Montenegro'
#
#
#
# 7308339893542614349
# b'Multiple'
#
#
#
# 34163093366933332139507271942542625371469
# b'Multiple_Unlisted'
#
#
#
# 139500742065929126696740174
# b'Netherlands'
#
#
#
# 177495008588537150289569034074503311374442523026766
# b'Netherlands_territory'
#
#
#
# 22048916628260686
# b'NGOs_UN'
#
#
#
# 4783252672609565942086426335538687073561207333492445561892257896545894802454521445006773297625430995809981742445653838
# b'North_America_Pakistan_Russia_Saudi_Arabia_Turkey'
#
#
#
# 117744874465821730700160846
# b'North_Korea'
#
#
#
# 133459522776910
# b'Norway'
#
#
#
# 4990363730465353039
# b'Oman_UAE'
#
#
#
# 7953766455951712592
# b'Pakistan'
#
#
#
# 139505465009996466775222352
# b'Philippines'
#
#
#
# 491261288785
# b'Qatar'
#
#
#
# 8485752154221198716887260754064792649752913
# b'Qatar_Saudi_Arabia'
#
#
#
# 107105536406866
# b'Russia'
#
#
#
# 30147447753212470604776956243
# b'Saudi_Arabia'
#
#
#
# 6879580366467208809293824059458255306814834697835999905549076750675
# b'Saudi_Arabia_South_Korea_USA'
#
#
#
# 86832511926917119432226067621359214931
# b'Saudi_Arabia_USA'
#
#
#
# 7236828769668784979
# b'Scotland'
#
#
#
# 1871367084451052808531
# b'Singapore'
#
#
#
# 30140227567590121037825929043
# b'South_Africa'
#
#
#
# 117744874465821730700357459
# b'South_Korea'
#
#
#
# 339189499714501404461968594046381907
# b'South_Korea_USA'
#
#
#
# 339189499714501404461968594046381907
# b'South_Korea_USA'
#
#
#
# 1975748358425290468427058206043987
# b'Southeast_Asia'
#
#
#
# 121381755123539
# b'Sweden'
#
#
#
# 121413839423173608325347155
# b'Switzerland'
#
#
#
# 418380937555
# b'Syria'
#
#
#
# 121364894277972
# b'Taiwan'
#
#
#
# 121364810327380
# b'Tehran'
#
#
#
# 499917154644
# b'Tibet'
#
#
#
# 133476501321044
# b'Turkey'
#
#
#
# 19285
# b'UK'
#
#
#
# 71826170399573
# b'UK_USA'
#
#
#
# 28550371533286229
# b'Ukraine'
#
#
#
# 20053
# b'UN'
#
#
#
# 7234316415479344725
# b'Unlisted'
#
#
#
# 4281173
# b'USA'
#
#
#
# 479033080716116002689877
# b'USA_Europe'
#
#
#
# 34172387495750340973031615562330792874837
# b'USA_Western_World'
#
#
#
# 1797144953447118693718
# b'Venezuela'
#
#
#
# 7956378975824997986907049911639
# b'Western_World'
#
#
#
# 7453001538729830744
# b'Xinjiang'
#
# Process finished with exit code 0