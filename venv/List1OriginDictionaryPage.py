# List 1 Dictionary page of Origin countries

import pandas as pd


#------------ListBox Country/Region/binary Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

listOneDictionary = {"Africa_China":{"binary": 30153525564624871856989693505},
                "Australia":{"binary": 1796930728965501580609},
                "Azerbaijan":{"binary": 521257315057726828935745},
                "Brazil":{"binary": 119200280572482},
                "China":{"binary": 418464229443},
                "China_North_Korea":{"binary": 33142235798066285977489245281315271043139},
                "China_Pakistan":{"binary": 2238786227951005213617790124648515},
                "China_Russia":{"binary": 30147528365705030538042632259},
                "Czech_Republic":{"binary": 2016311051235894369754033219271235},
                "Decentralized_International_Hacktivist_Group":{"binary": 4030061651715448937258886338687573509473192067501578500999556277764116296964663760381662969481473103717700},
                "Eastern_Europe":{"binary": 2057431415377846504395799230898501},
                "Egypt":{"binary": 500103210821},
                "Gaza":{"binary": 1635410247},
                "Gaza_Former_Soviet_Union_Lebanon":{"binary": 49951295185924953357192938129459662694624102732189565470444669956949290934599},
                "Germany":{"binary": 34179836909086023},
                "India":{"binary": 418380017225},
                "Individuals":{"binary": 139538282629009384004677193},
                "Individuals_Ukraine":{"binary": 2261993475681827677736728506999153589307600457},
                "Individuals_Unlisted":{"binary": 573161596645207770904272559636410843002082455113},
                "International":{"binary": 8586795105461350372667137748553},
                "Iran":{"binary": 1851880009},
                "Iran_North_Korea_Russia":{"binary": 9330208112349500424777135934104632250386116936128885321},
                "Iran_Russia":{"binary": 117763782678535275756483145},
                "Iran_Unlisted":{"binary": 7954215017830331842300462854729},
                "Iraq":{"binary": 1902211657},
                "ISIS":{"binary": 1397314377},
                "Israel":{"binary": 119182682387273},
                "Israel_USA":{"binary": 308491052899443525448521},
                "Lebanon":{"binary": 31084767309096268},
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


pdDictListOne = pd.DataFrame(listOneDictionary)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

print("\nList 1 Dictionary of Origin countries: \n")
print(listOneDictionary)
print("\n\n")

print("In excel format: \n")
print(pdDictListOne)

# ----- output of program---------------------------------------------------------------------------------------------

# List 1 Dictionary of Origin countries:
#
# {'Africa_China': {'binary': 30153525564624871856989693505}, 'Australia': {'binary': 1796930728965501580609}, 'Azerbaijan': {'binary': 521257315057726828935745}, 'Brazil': {'binary': 119200280572482}, 'China': {'binary': 418464229443}, 'China_North_Korea': {'binary': 33142235798066285977489245281315271043139}, 'China_Pakistan': {'binary': 2238786227951005213617790124648515}, 'China_Russia': {'binary': 30147528365705030538042632259}, 'Czech_Republic': {'binary': 2016311051235894369754033219271235}, 'Decentralized_International_Hacktivist_Group': {'binary': 4030061651715448937258886338687573509473192067501578500999556277764116296964663760381662969481473103717700}, 'Eastern_Europe': {'binary': 2057431415377846504395799230898501}, 'Egypt': {'binary': 500103210821}, 'Gaza': {'binary': 1635410247}, 'Gaza_Former_Soviet_Union_Lebanon': {'binary': 49951295185924953357192938129459662694624102732189565470444669956949290934599}, 'Germany': {'binary': 34179836909086023}, 'India': {'binary': 418380017225}, 'Individuals': {'binary': 139538282629009384004677193}, 'Individuals_Ukraine': {'binary': 2261993475681827677736728506999153589307600457}, 'Individuals_Unlisted': {'binary': 573161596645207770904272559636410843002082455113}, 'International': {'binary': 8586795105461350372667137748553}, 'Iran': {'binary': 1851880009}, 'Iran_North_Korea_Russia': {'binary': 9330208112349500424777135934104632250386116936128885321}, 'Iran_Russia': {'binary': 117763782678535275756483145}, 'Iran_Unlisted': {'binary': 7954215017830331842300462854729}, 'Iraq': {'binary': 1902211657}, 'ISIS': {'binary': 1397314377}, 'Israel': {'binary': 119182682387273}, 'Israel_USA': {'binary': 308491052899443525448521}, 'Lebanon': {'binary': 31084767309096268}, 'Mexico': {'binary': 122472761943373}, 'Middle_East': {'binary': 140780261553827770911713613}, 'Morocco': {'binary': 31353001137565517}, 'Multiple': {'binary': 7308339893542614349}, 'Nation_State_Actor_Eastern_Europe': {'binary': 11745856961995155074459591118783721087539815469043632190606120890413099009728846}, 'Nation_State_Actor_Unlisted': {'binary': 41300645649190979956682253942903520807850576892501048304935919950}, 'Non_State_Actor_Unlisted': {'binary': 2461710312914310691158905860358686495295201354771914977102}, 'North_Korea': {'binary': 117744874465821730700160846}, 'Pakistan': {'binary': 7953766455951712592}, 'Russia': {'binary': 107105536406866}, 'Russia_Ukraine': {'binary': 2057271081577553266210956287112530}, 'Russia_Ukraine_USA': {'binary': 5690655501723968284733388360289691192489298}, 'Saudi_Arabia': {'binary': 30147447753212470604776956243}, 'South_Korea': {'binary': 117744874465821730700357459}, 'South_Korea_USA': {'binary': 339189499714501404461968594046381907}, 'State_Sponsored_Actor_Unlisted': {'binary': 692909852995937295984928817766944035748308436617603438577965161292854355}, 'Syria': {'binary': 418380937555}, 'Taiwan': {'binary': 121364894277972}, 'Taiwan_USA': {'binary': 308491052901625737339220}, 'Turkey': {'binary': 133476501321044}, 'UAE': {'binary': 4538709}, 'UK': {'binary': 19285}, 'UK_USA': {'binary': 71826170399573}, 'Unlisted': {'binary': 7234316415479344725}, 'USA': {'binary': 4281173}, 'Vietnam': {'binary': 30787899488561494}, 'Western_World': {'binary': 7956378975824997986907049911639}, 'Yemen': {'binary': 474148070745}}
#
#
#
# In excel format:
#
#                          Africa_China               Australia                Azerbaijan           Brazil         China                          China_North_Korea                      China_Pakistan                   China_Russia                      Czech_Republic       Decentralized_International_Hacktivist_Group                      Eastern_Europe         Egypt        Gaza                   Gaza_Former_Soviet_Union_Lebanon            Germany         India                  Individuals                             Individuals_Ukraine                              Individuals_Unlisted                    International        Iran                            Iran_North_Korea_Russia                  Iran_Russia                    Iran_Unlisted        Iraq        ISIS           Israel                Israel_USA            Lebanon           Mexico                  Middle_East            Morocco             Multiple                  Nation_State_Actor_Eastern_Europe  \
# binary  30153525564624871856989693505  1796930728965501580609  521257315057726828935745  119200280572482  418464229443  33142235798066285977489245281315271043139  2238786227951005213617790124648515  30147528365705030538042632259  2016311051235894369754033219271235  4030061651715448937258886338687573509473192067...  2057431415377846504395799230898501  500103210821  1635410247  4995129518592495335719293812945966269462410273...  34179836909086023  418380017225  139538282629009384004677193  2261993475681827677736728506999153589307600457  573161596645207770904272559636410843002082455113  8586795105461350372667137748553  1851880009  9330208112349500424777135934104632250386116936...  117763782678535275756483145  7954215017830331842300462854729  1902211657  1397314377  119182682387273  308491052899443525448521  31084767309096268  122472761943373  140780261553827770911713613  31353001137565517  7308339893542614349  1174585696199515507445959111878372108753981546...
#
#                               Nation_State_Actor_Unlisted                           Non_State_Actor_Unlisted                  North_Korea             Pakistan           Russia                      Russia_Ukraine                           Russia_Ukraine_USA                   Saudi_Arabia                  South_Korea                       South_Korea_USA                     State_Sponsored_Actor_Unlisted         Syria           Taiwan                Taiwan_USA           Turkey      UAE     UK          UK_USA             Unlisted      USA            Vietnam                    Western_World         Yemen
# binary  4130064564919097995668225394290352080785057689...  2461710312914310691158905860358686495295201354...  117744874465821730700160846  7953766455951712592  107105536406866  2057271081577553266210956287112530  5690655501723968284733388360289691192489298  30147447753212470604776956243  117744874465821730700357459  339189499714501404461968594046381907  6929098529959372959849288177669440357483084366...  418380937555  121364894277972  308491052901625737339220  133476501321044  4538709  19285  71826170399573  7234316415479344725  4281173  30787899488561494  7956378975824997986907049911639  474148070745
#
# Process finished with exit code 0