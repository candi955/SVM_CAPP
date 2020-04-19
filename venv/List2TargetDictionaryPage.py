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
                "Central_Asia_Eastern_Europe_Russia":{"binary": 2887559549285678575025028014159333265348920949327583776587248794714267494332130627},
                "Central_Asia_Europe_USA":{"binary": 6256941893813146631859154412586712377514069709544121667},
                "Chile":{"binary": 435610544195},
                "China":{"binary": 418464229443},
                "China_Germany":{"binary": 9620768797959008789195953629251},
                "China_Individuals":{"binary": 39276534853245351046492589691522312136771},
                "China_Pakistan":{"binary": 2238786227951005213617790124648515},
                "CSIS_USA":{"binary": 4707199903439868739},
                "Czech_Republic":{"binary": 2016311051235894369754033219271235},
                "Czech_Republic_Individuals":{"binary": 185478191754227285249969174530609441383227936193346174183635523},
                "Denmark":{"binary": 30243585281385796},
                "East_Asia":{"binary": 1796932664024362082629},
                "Eastern_Europe":{"binary": 2057431415377846504395799230898501},
                "Egypt":{"binary": 500103210821},
                "Estonia":{"binary": 27418995778155333},
                "Europe":{"binary": 111533580514629},
                "Europe_Individuals":{"binary": 10054792922430809867902102961034118644790597},
                "Europe_Individuals_Middle_East":{"binary": 803713213924968946004570530890938146356423406018987839112189083435300165},
                "Europe_Japan_USA":{"binary": 86832511930930819263603543771519808837},
                "Europe_Middle_East":{"binary": 10144286935599035412558109646840913932219717},
                "Europe_Middle_East_North_America":{"binary": 44049991939471719292781853637477999382754235777045428286303327005162211538245},
                "Europe_NATO":{"binary": 95903023219825537446999365},
                "Europe_NATO_Ukraine":{"binary": 2261993475681827677693093247589969742749922629},
                "Europe_North_America":{"binary": 555989064261598943201993414997543446447190603077},
                "Europe_Russia":{"binary": 7717767261620487822145651635525},
                "Finland":{"binary": 28268862381123910},
                "France":{"binary": 111477728047686},
                "France_Germany_Japan":{"binary": 630161946757152369395487029780148113741199798854},
                "France_Germany_UK": {"binary": 25634657629830475695080879593172735455814},
                "France_South_Korea": {"binary": 8484412364304969210251414251757639397634630},
                "Georgia": {"binary": 27418965763384647},
                "Germany": {"binary": 34179836909086023},
                "Germany_Israel_Jordan_Saudi_Arabia_Turkey_USA": {"binary": 3599295972025478897151354840582044557016535795860902688018405021916292137618025118208661378066604542240384327},
                "Germany_Mongolia_Myanmar_Pakistan_UN_Vietnam_Individuals": {"binary": 327711598681358806473535046145613536099155348676132340178557461795987392748287290496883585939262089223124598924634327352459624440816967},
                "Germany_Turkey": {"binary": 2462206859723460424033855417247047},
                "Global_Unlisted": {"binary": 521287435408528627617000934358346823},
                "India": {"binary": 418380017225},
                "India_Italy_Saudi_Arabia_Scotland_UAE": {"binary": 34442224644743318243735343714622843513968332852566796037896488177251263385944346459401801},
                "India_Pakistan": {"binary": 2238786227951005213617790040436297},
                "Individuals": {"binary": 139538282629009384004677193},
                "Individuals_Iran": {"binary": 146721050339509918346768000002986110537},
                "Individuals_Latvia": {"binary": 8485778837090825286018691921867596733115977},
                "Individuals_Multiple": {"binary": 579026340795075577836801232462293422175315848777},
                "Individuals_NATO_Ukraine": {"binary": 2487088128465618221363062841210218726675521088406281285193},
                "Individuals_Sri_Lanka": {"binary": 142378982391427591699701078127165432569250395221577},
                "Individuals_USA": {"binary": 339189499736294812625156247350701641},
                "Individuals_Vietnam": {"binary": 2439268704152585959516329496284772107676839497},
                "Indonesia": {"binary": 1796932703671120326217},
                "Indonesia_Mongolia_Myanmar_Taiwan_Tibet_Vietnam_Xinjiang": {"binary": 293663212810770379135919508023638240622048108390492839331378670437676906065559292090827246281641117934618254935537732048405501613207113},
                "International": {"binary": 8586795105461350372667137748553},
                "Iran": {"binary": 1851880009},
                "Iran_Israel_Middle_East": {"binary": 11153761441187306308117234849995952050181433635710792265},
                "Iran_Syria": {"binary": 460014705681956933300809},
                "Iraq_Pakistan_Tajikistan": {"binary": 2706526475567613707123455675952615284393656146857744757321},
                "Ireland": {"binary": 28268862380536393},

                "Central_Asia_Eastern_Europe": {"binary": 41729666698114283016919014524090844581596341132174623587355747651},
                "Central_Asia_Eastern_Europe_Russia": {"binary": 2887559549285678575025028014159333265348920949327583776587248794714267494332130627},
                "Central_Asia_Europe_USA": {"binary": 6256941893813146631859154412586712377514069709544121667},
                "Chile": {"binary": 435610544195},
                "China": {"binary": 418464229443},
                "China_Germany": {"binary": 9620768797959008789195953629251},
                "China_Individuals": {"binary": 39276534853245351046492589691522312136771},
                "China_Pakistan": {"binary": 2238786227951005213617790124648515},
                "CSIS_USA": {"binary": 4707199903439868739},
                "Czech_Republic": {"binary": 2016311051235894369754033219271235},
                 "Czech_Republic_Individuals": {"binary": 185478191754227285249969174530609441383227936193346174183635523},
                 "Denmark": {"binary": 30243585281385796},
                 "East_Asia": {"binary": 1796932664024362082629},
                 "Eastern_Europe": {"binary": 2057431415377846504395799230898501},
                 "Egypt": {"binary": 500103210821},
                 "Estonia": {"binary": 27418995778155333},
                 "Europe": {"binary": 111533580514629},
                 "Europe_Individuals": {"binary": 10054792922430809867902102961034118644790597},
                 "Europe_Individuals_Middle_East": {"binary": 803713213924968946004570530890938146356423406018987839112189083435300165},
                 "Europe_Japan_USA": {"binary": 86832511930930819263603543771519808837},
                 "Europe_Middle_East": {"binary": 10144286935599035412558109646840913932219717},
                 "Europe_Middle_East_North_America": {"binary": 44049991939471719292781853637477999382754235777045428286303327005162211538245},
                 "Europe_NATO": {"binary": 95903023219825537446999365},
                 "Europe_NATO_Ukraine": {"binary": 2261993475681827677693093247589969742749922629},
                 "Europe_North_America": {"binary": 555989064261598943201993414997543446447190603077},
                 "Europe_Russia": {"binary": 7717767261620487822145651635525},
                 "Finland": {"binary": 28268862381123910},
                 "France": {"binary": 111477728047686},
                 "France_Germany_Japan": {"binary": 630161946757152369395487029780148113741199798854}}

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