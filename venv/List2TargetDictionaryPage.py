# List 2 Dictionary page of Target countries


import pandas as pd


#------------ListBox Country/Region/binary Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

listTwoDictionary = {"Afghanistan":{"binary": 133442057845059666670216769},
                "Afghanistan_Application_Users_India_Individuals_Middle_East":{"binary": 5547024738073957303662399576029973568509146976390336004265898740432675875991326601817987176556771282997325216339676316688169204494214088844865},
                "Africa":{"binary": 107079598761537},
                "Africa_Asia":{"binary": 117763779069479634143962689},
                "Al_Quaida":{"binary": 1796569596582678195265},
                "Application_Users":{"binary": 39284530948651148542945322099333464617025},
                "Application_Users_Individuals":{"binary": 3111807686350090077732346834447189654644633344498384566960921427079233},
                "Application_Users_Japan":{"binary": 10572363095725242809903474363794222115376060650679726145},
                "Armenia":{"binary": 27418995609924161},
                "Asia":{"binary": 1634300737},
                "Asia_Canada_Europe_Middle_East_USA":{"binary": 1936429723561952681582869571271737150404117317300876807438770316145334861458666305},
                "Asia_Europe_Middle_East_USA":{"binary": 26873360808337585803091529125126950972081670239456308127962067777},
                "Asia_Europe_North_America":{"binary": 611316441071925721528505149291982085844431624011733040460609},
                "Asia_South_America":{"binary": 8483719852624495593292136065139819009372993},
                "Asia_USA":{"binary": 4707199903676855105},
                "Australia":{"binary": 1796930728965501580609},
                "Australia_Canada_Japan_Switzerland_UK_USA":{"binary": 139534466882955655784457473920909684382362106944851677537702575567474562215766014437633627337749825},
                "Australia_Canada_New_Zealand_UK_USA":{"binary": 495726009159212053789849057507327564583030099413608231039652233206430848978550748481},
                "Austria":{"binary": 27419013041845569},
                "Austria_Germany_Switzerland":{"binary": 41314988655876265391272827414481922914912132198580508749628405057},
                "Bahrain":{"binary": 31078114690359618},
                "Belarus_Mongolia_Russia":{"binary": 9330208112349500424797783435764896148944012388223182146},
                "Belgium":{"binary": 30809868028634434},
                "Brazil":{"binary": 119200280572482},
                "Cambodia":{"binary": 7019251923789111619},
                "Canada":{"binary": 107083759247683},
                "Canada_France_Multiple_UK_USA":{"binary": 1761172573677115074610677974231769886272027516418405464348645768716611},
                "Central_America":{"binary": 505669108189612364370267082941424963},
                "Central_Asia_Eastern_Europe":{"binary": 41729666698114283016919014524090844581596341132174623587355747651},

                "Mexico":{"binary": 122472761943373},
                "Middle_East":{"binary": 140780261553827770911713613},
                "Morocco":{"binary": 31353001137565517},
                "Multiple":{"binary": 7308339893542614349},
                "Nation_State_Actor_Eastern_Europe":{"binary": 11745856961995155074459591118783721087539815469043632190606120890413099009728846},
                "Nation_State_Actor_Unlisted":{"binary": 41300645649190979956682253942903520807850576892501048304935919950},
                "Non_State_Actor_Unlisted":{"binary": 2461710312914310691158905860358686495295201354771914977102},
                "North_Korea":{"binary": 117744874465821730700160846},
                "Pakistan":{"binary": 7953766455951712592},
                "Russia":{"binary": 107105536406866},
                "Russia_Ukraine":{"binary": 2057271081577553266210956287112530},
                "Russia_Ukraine_USA":{"binary": 5690655501723968284733388360289691192489298},
                "Saudi_Arabia":{"binary": 30147447753212470604776956243},
                "South_Korea":{"binary": 117744874465821730700357459},
                "South_Korea_USA":{"binary": 339189499714501404461968594046381907},
                "State_Sponsored_Actor_Unlisted":{"binary": 692909852995937295984928817766944035748308436617603438577965161292854355},
                "Syria":{"binary": 418380937555},
                "Taiwan":{"binary": 121364894277972},
                "Taiwan_USA":{"binary": 308491052901625737339220},
                "Turkey":{"binary": 133476501321044},
                "UAE":{"binary": 4538709},
                "UK":{"binary": 19285},
                "UK_USA":{"binary": 71826170399573},
                "Unlisted":{"binary": 7234316415479344725},
                "USA":{"binary": 4281173},
                "Vietnam":{"binary": 30787899488561494},
                "Western_World":{"binary": 7956378975824997986907049911639},
                "Yemen":{"binary": 474148070745}}

pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)


print("\nList 2 Dictionary of Target countries: \n")
print(listOneDictionary)
print("\n\n")

print("In excel format: \n")
print(pdDictListOne)

# ----- output of program---------------------------------------------------------------------------------------------

#