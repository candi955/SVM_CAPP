# Prediction of Attack Origin page
# Support Vector Machine Cyber-Attack Prediction Program (SVM CAPP)__

# A GUI program (through Tkinter) utilizing SKLearn, SVM algorithm, to predict cybersecurity data via a Supervised
# dataset made of source and target data.  At this time the data is not made of completely real data, and the
# project is in the build/test phases.

# About Support Vector Machine (SVM)
# A support vector machine (SVM) is a type of Supervised machine learning classification algorithm.
# SVM differs from the other classification algorithms in the way that it chooses the decision boundary that maximizes
# the distance from the nearest data points of all the classes. An SVM doesn't merely find a decision boundary; it
# finds the most optimal decision boundary.
# (https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/)

# Utilizing SKlearn, pandas, numpy, xlrd APIs and also using a subclass of exception: import warnings (to prevent a
# Future Error warning from popping up; appears is due to possible future updates).

# Resources for original template build:
# https://www.youtube.com/watch?reload=9&v=bwZ3Qiuj3i8
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackabuse.com/implementing-svm-and-kernel-svm-with-pythons-scikit-learn/
# https://github.com/candi955/LottoProject   (my initial SVM project build and template for this project)

# Resources utilized for dataset creation:
# https://datacatalog.worldbank.org/dataset/world-development-indicators
# https://datacatalog.worldbank.org/dataset/global-economic-monitor
# https://csis-prod.s3.amazonaws.com/s3fs-public/190904_Significant_Cyber_Events_List.pdf
# https://www.csis.org/programs/technology-policy-program/significant-cyber-incidents



#---------Imports----------------------------------------------------------------------------------------------------
# Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mbox

# Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import xlrd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#------------ListBox Country/Region/binary Dictionaries--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

# List 1 (Target country/region)
listTargetDictionary = {"Afghanistan":{"binary": 133442057845059666670216769},
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
                "ISIS": {"binary": 1397314377},
                "Israel": {"binary": 119182682387273},
                "Israel_Saudi_Arabia_USA": {"binary": 6256941893723329418780205680006274667958179856383112009},
                "Israel_Sudan_Syria_Middle_East": {"binary": 803713213924968946004570530889369126979850478811228792355694693835764553},
                "Italy": {"binary": 521509368905},
                "Italy_France_Germany_Poland_Spain_Turkey_USA": {"binary": 2340999890724526941997479847528907046777487003526924268424622113184721296010098148746237170904876170966089},
                "Japan": {"binary": 474081157450},
                "Japan_Multiple_Unlisted": {"binary": 9616055909821526137339212106786338705010904763416469834},
                "Japan_Unlisted": {"binary": 2036279044564564951628918490685770},
                "Kazakhstan": {"binary": 521258038456151927578955},
                "Lebanon": {"binary": 31084767309096268},
                "Lebanon_UAE": {"binary": 83724410224598406217753932},
                "Libya": {"binary": 418648320332},
                "Lithuania": {"binary": 1796931291928138639692},
                "Malaysia": {"binary": 7019268459396358477},
                "Mexico": {"binary": 122472761943373},
                "Middle_East": {"binary": 140780261553827770911713613},
                "Middle_East_South_America_UK_USA": {"binary": 29547572681856873838269706859280096340519948949106405771628223098370744674637},
                "Montenegro": {"binary": 526293058905474086104909},
                "Multiple": {"binary": 7308339893542614349},
                "Multiple_Unlisted": {"binary": 34163093366933332139507271942542625371469},
                "Netherlands": {"binary": 139500742065929126696740174},
                "Netherlands_territory": {"binary": 177495008588537150289569034074503311374442523026766},
                "NGOs_UN": {"binary": 22048916628260686},
                "North_America_Pakistan_Russia_Saudi_Arabia_Turkey": {"binary": 4783252672609565942086426335538687073561207333492445561892257896545894802454521445006773297625430995809981742445653838},
                "North_Korea": {"binary": 117744874465821730700160846},
                "Norway": {"binary": 133459522776910},
                "Oman_UAE": {"binary": 4990363730465353039},
                "Pakistan": {"binary": 7953766455951712592},
                "Philippines": {"binary": 139505465009996466775222352},
                "Qatar": {"binary": 491261288785},
                "Qatar_Saudi_Arabia": {"binary": 8485752154221198716887260754064792649752913},
                "Russia": {"binary": 107105536406866},
                "Saudi_Arabia": {"binary": 30147447753212470604776956243},
                "Saudi_Arabia_South_Korea_USA": {"binary": 6879580366467208809293824059458255306814834697835999905549076750675},
                "Saudi_Arabia_USA": {"binary": 86832511926917119432226067621359214931},
                "Scotland": {"binary": 7236828769668784979},
                "Singapore": {"binary": 1871367084451052808531},
                "South_Africa": {"binary": 30140227567590121037825929043},
                "South_Korea": {"binary": 117744874465821730700357459},
                "South_Korea_USA": {"binary": 339189499714501404461968594046381907},
                "Southeast_Asia": {"binary": 1975748358425290468427058206043987},
                "Sweden": {"binary": 121381755123539},
                "Switzerland": {"binary": 121413839423173608325347155},
                "Syria": {"binary": 418380937555},
                "Taiwan": {"binary": 121364894277972},
                "Tehran": {"binary": 121364810327380},
                "Tibet": {"binary": 499917154644},
                "Turkey": {"binary": 133476501321044},
                "UK": {"binary": 19285},
                "UK_USA": {"binary": 71826170399573},
                "Ukraine": {"binary": 28550371533286229},
                "UN": {"binary": 20053},
                "Unlisted": {"binary": 7234316415479344725},
                "USA": {"binary": 4281173},
                "USA_Europe": {"binary": 479033080716116002689877},
                "USA_Western_World": {"binary": 34172387495750340973031615562330792874837},
                "Venezuela": {"binary": 1797144953447118693718},
                "Western_World": {"binary": 7956378975824997986907049911639},
                "Xinjiang": {"binary": 7453001538729830744}}

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
# pdDictOne = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# List 2 (Month of attack in binary numbers)

listMonthDictionary = {"January":{"binary": 34184235089551690}, # list option 0
                "February":{"binary": 8751164182992414022}, # list option 1
                "March":{"binary": 448345039181}, # list option 2
                "April":{"binary": 465625575489}, # list option 3
                "May":{"binary": 7954765}, # list option 4
                "June":{"binary": 1701737802}, # list option 5
                "July":{"binary": 2037151050}, # list option 6
                "August":{"binary": 128039239775553}, # list option 7
                "September":{"binary": 2110234346230949897555}, # list option 8
                "October":{"binary": 32199620796113743}, # list option 9
                "November":{"binary": 8243102914964778830},
                "December":{"binary": 8243102914963531076},
                "Unlisted":{"binary": 7234316415479344725}}

# Creating pandas variable for List 1 dictionary, in case I want to print the dictionary at some point in the program
#pdDictTwo = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

# ----------Opening and creating DataFrame-----------------------------------------------------------------------
# pulling excel file and creating variable
cyberExcel = xlrd.open_workbook('SVMCAPPdataset8Apr2020_OriginOnly_19Apr2020_810pm_fakeDummyNums.xlsx')
# Creating variable to convert excel file to a dataframe (using pandas)
sheets = cyberExcel.sheets()
for sheet in sheets:
   cyberSheetData = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# creating dataframe for tkinter
df = pd.DataFrame(cyberSheetData)

# Removing target row from source dataset, with the -1, and removing source data from target data column, so that the -1
# will only show the last column in the target data
sources = cyberSheetData[:, :-1]
target = cyberSheetData[:, len(cyberSheetData[0]) - 1]

# Deleting header column from dataframe, both source and target data
sourceNoHeader = np.delete(sources, (0), axis=0)
targetNoHeader = np.delete(target, (0), axis=0)

X = sourceNoHeader
y = targetNoHeader

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=50)

model = svm.SVC(kernel='linear')
model.fit(X_train, y_train.ravel())
y_pred = model.predict(X_test)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)


#-----Creating Tkinter Setup (root) for GUI----------------------------------------------------------------------------
root = tk.Tk()
root.title('SVM Prediction: Global attack by location (country)')
#root.geometry("1000x1000")
style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

# Tabs and Frames
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Dataset')
tab_control.add(tab2, text='Prediction Accuracy')
tab_control.add(tab3, text='Dummy Values and Target Prediction')

tab_control.pack(expand=1, fill='both')

# Tkinter listbox with root functions
# reference: http://effbot.org/tkinterbook/listbox.htm
listbox = Listbox(root, selectmode=SINGLE)


#---Creating Tkinter functions----------------------------------------------------------------------------------------

# Creating listbox functions
# https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry
# https://www.youtube.com/watch?v=XJqUu85sMrA
# https://note.nkmk.me/en/python-tuple-list-unpack/
# List 1 function to place list and then transfer answer to textbox, for origin country/region choice
def get_selDummyOneTarget():
    for i in List1.curselection():
        if i == 0:
            Afghanistanlist = listTargetDictionary.get("Afghanistan")
            for k, v in Afghanistanlist.items():
                AfghanistanBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (AfghanistanBinary))
        if i == 1:
            Afghanistan_Application_Users_India_Individuals_Middle_Eastlist = listTargetDictionary.get(
                "Afghanistan_Application_Users_India_Individuals_Middle_East")
            for k, v in Afghanistan_Application_Users_India_Individuals_Middle_Eastlist.items():
                Afghanistan_Application_Users_India_Individuals_Middle_EastBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Afghanistan_Application_Users_India_Individuals_Middle_EastBinary))
        if i == 2:
            Africalist = listTargetDictionary.get("Africa")
            for k, v in Africalist.items():
                AfricaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (AfricaBinary))
        if i == 3:
            Africa_Asialist = listTargetDictionary.get("Africa_Asia")
            for k, v in Africa_Asialist.items():
                Africa_AsiaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Africa_AsiaBinary))
        if i == 4:
            Al_Quaidalist = listTargetDictionary.get("Al_Quaida")
            for k, v in Al_Quaidalist.items():
                Al_QuaidaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Al_QuaidaBinary))
        if i == 5:
            Application_Userslist = listTargetDictionary.get("Application_Users")
            for k, v in Application_Userslist.items():
                Application_UsersBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_UsersBinary))
        if i == 6:
            Application_Users_Individualslist = listTargetDictionary.get("Application_Users_Individuals")
            for k, v in Application_Users_Individualslist.items():
                Application_Users_IndividualsBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_Users_IndividualsBinary))
        if i == 7:
            Application_Users_Japanlist = listTargetDictionary.get("Application_Users_Japan")
            for k, v in Application_Users_Japanlist.items():
                Application_Users_JapanBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (Application_Users_JapanBinary))
        if i == 8:
            Armenialist = listTargetDictionary.get("Armenia")
            for k, v in Armenialist.items():
                ArmeniaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (ArmeniaBinary))
        if i == 9:
            Asialist = listTargetDictionary.get("Asia")
            for k, v in Asialist.items():
                AsiaBinary = "{}".format(v)
                dummyNumberOne.insert(1.0, (AsiaBinary))

# List 2 function to place list and then transfer answer to textbox, for Month choice
def get_selDummyTwoMonth():
    for i in List2.curselection():
        if i == 0:
            Januarylist = listMonthDictionary.get("January")
            for k, v in Januarylist.items():
                JanuaryBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JanuaryBinary))
        if i == 1:
            Februarylist = listMonthDictionary.get("February")
            for k, v in Februarylist.items():
                FebruaryBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (FebruaryBinary))
        if i == 2:
            Marchlist = listMonthDictionary.get("March")
            for k, v in Marchlist.items():
                MarchBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MarchBinary))
        if i == 3:
            Aprillist = listMonthDictionary.get("April")
            for k, v in Aprillist.items():
                AprilBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AprilBinary))
        if i == 4:
            Maylist = listMonthDictionary.get("May")
            for k, v in Maylist.items():
                MayBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (MayBinary))
        if i == 5:
            Junelist = listMonthDictionary.get("June")
            for k, v in Junelist.items():
                JuneBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JuneBinary))
        if i == 6:
            Julylist = listMonthDictionary.get("July")
            for k, v in Julylist.items():
                JulyBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (JulyBinary))
        if i == 7:
            Augustlist = listMonthDictionary.get("August")
            for k, v in Augustlist.items():
                AugustBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (AugustBinary))
        if i == 8:
            Septemberlist = listMonthDictionary.get("September")
            for k, v in Septemberlist.items():
                SeptemberBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (SeptemberBinary))
        if i == 9:
            Octoberlist = listMonthDictionary.get("October")
            for k, v in Octoberlist.items():
                OctoberBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (OctoberBinary))
        if i == 10:
            Novemberlist = listMonthDictionary.get("November")
            for k, v in Novemberlist.items():
                NovemberBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (NovemberBinary))
        if i == 11:
            Decemberlist = listMonthDictionary.get("December")
            for k, v in Decemberlist.items():
                DecemberBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (DecemberBinary))
        if i == 12:
            Unlistedlist = listMonthDictionary.get("Unlisted")
            for k, v in Unlistedlist.items():
                UnlistedBinary = "{}".format(v)
                dummyNumberTwo.insert(1.0, (UnlistedBinary))

# the dataframe method, tab 1
def writeDataset():
    tab1_display.insert(1.0, pd.DataFrame(df))

# the accuracy score method, tab 2
def writeAccuracy():
    tab2_display.insert(4.0, str(accuracy_score(y_test, y_pred)))

# creating a method so that the user can tab from one dummy number textbox to the next, instead of clicking
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

#---- Creating functions to run the main prediction program ----------------------------------------------------------

# the dummy number value method, for tab 3 input entries from the user
def dummyValues():
    while True:
        try:
            # Getting user-input for dummy numbers to be used in the algorithm
            # Dummy User Choice 1 -
            dummyTextOne = dummyNumberOne.get('1.0', tk.END)
            # Dummy User Choice 2 -
            dummyTextTwo = dummyNumberTwo.get('1.0', tk.END)
            # Dummy User Choice 3 -
            dummyTextThree = dummyNumberThree.get('1.0', tk.END)
            # Dummy User Choice 4 -
            dummyTextFour = dummyNumberFour.get('1.0', tk.END)
            # Dummy User Choice 5 -
            dummyTextFive = dummyNumberFive.get('1.0', tk.END)
            # Dummy 6 User Choice 6 -
            dummyTextSix = dummyNumberSix.get('1.0', tk.END)

            # changing dummy numbers to integers for algorithm processing
            dummyValues.dummyTextOne = float(dummyTextOne)
            dummyValues.dummyTextTwo = float(dummyTextTwo)
            dummyValues.dummyTextThree = float(dummyTextThree)
            dummyValues.dummyTextFour = float(dummyTextFour)
            dummyValues.dummyTextFive = float(dummyTextFive)
            dummyValues.dummyTextSix = float(dummyTextSix)

        # exception handling, basically stating 'if the above previous is not true, then do this). Once a statement
        # is made, the program brings the user back to the main menu by calling the Predictions class and menu
        # method
        except ValueError:
            # error message variable
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        # Removed the if statements for exception due to planning to change this option to list-option

        else:
            # breaking the loop to avoid infinite loop
            break

# the prediction method, for tab 3; utilizes dummy value input from dummy value method, which is why that method
# is called at the beginning of the finalPrediction method (for the user-input variables)
def finalPrediction():

    while True:
        try:
            #calling dummy values function to call variables from that function
            dummyValues()
            # turning the dummy values, which were string then integer, back into an array for the prediction
            a = np.array([dummyValues.dummyTextOne, dummyValues.dummyTextTwo, dummyValues.dummyTextThree,
                          dummyValues.dummyTextFour, dummyValues.dummyTextFive])

            # inserting dummy array variable as argument to K-nearest neighbor algorithm to create prediction, which is
            # placed within the prediction variable
            prediction = knn.predict([a])
            tab3_display.insert(4.0, prediction)
        except ValueError:
            mbox.showerror("Error", "Please ensure that your entry is accurate.")
            clear_display_result()

        else:
            break

# Below is the creation of textbox entries; however am planning to make dummy number option a label option
def clear_display_result():
    tab3_display.delete(1.0, END)
    dummyNumberOne.delete(1.0, END)
    dummyNumberTwo.delete(1.0, END)
    dummyNumberThree.delete(1.0, END)
    dummyNumberFour.delete(1.0, END)
    dummyNumberFive.delete(1.0, END)
    dummyNumberSix.delete(1.0, END)
    # when boxes are cleared, bringing the option focus for the user back to the initial textbox
    dummyNumberOne.focus()

def mainMenu():

    while True:
        try:

            # Creating a messagebox for when the user clicks to exit the program, with exception prevention
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                root.protocol("WM_DELETE_WINDOW", mainMenu)
                import mainPage

        except ValueError:
            import mainPage
        else:
            break

def exitProgram():
    exit()

def flush(self):
    pass

#------------Tkinter Labels for Tabs-----------------------------------------------------------------------------------

l1 = Label(tab1, text='Please click the button below to scroll through the original dataset model.', padx=5, pady=5)
l1.grid(row=1, column=0)
l2 = Label(tab2, text='Please click the button below to see the prediction accuracy of the model in decimal ' +
                      'format.', padx=5, pady=5)
l2.grid(row=1, column=0)

# This option will eventually be a dropbox option, rather than fill in the blanks
l3 = Label(tab3, text='Please enter six situational choices in the cells below, and then click the Prediction button'+
                      'to see your prediction results:', padx=5, pady=5)
l3.grid(row=1, column=0)

#--------------------- Dummy 1 Listbox and Textbox Attack Origin-------------------------------------------------------
#Listbox of Dummy Numbers
dummyOneListBox = Listbox(tab3) # height=1, width=50, yscrollcommand=TRUE)
dummyOneListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyOneListBox.grid(row=2, column=0, padx=5, pady=5, ipadx=250, ipady=0)

List1 = Listbox(dummyOneListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listTargetDictionary:
    List1.insert(END, '{}: {}'.format(key, listTargetDictionary[key]))
    List1.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberOne = Text(tab3, height=2, width=50)
dummyNumberOne.bind("<Tab>", focus_next_widget)
dummyNumberOne.grid(row=2, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 2 Listbox and Textbox  (Attack Target) ----------------------------------------------------
#Listbox of Dummy Numbers
dummyTwoListBox = Listbox(tab3, height=2, width=50, yscrollcommand=SCROLL)
dummyTwoListBox.bind("<Tab>", focus_next_widget) # for user to tab between listboxes/textboxes
dummyTwoListBox.grid(row=4, column=0, columnspan=1, padx=5, pady=5, ipadx=250, ipady=0)

List2 = Listbox(dummyTwoListBox)
# Pulling locationDict dictionary data and placing into listbox
# references: https://stackoverflow.com/questions/39315584/tkinter-listbox-and-dictionaries
# https://stackoverflow.com/questions/31046479/resizing-tkinter-listbox-to-width-of-largest-item-using-grid
for key in listMonthDictionary:
    List2.insert(END, '{}: {}'.format(key, listMonthDictionary[key]))
    List2.pack(fill=BOTH, expand=TRUE)

# Textbox of Dummy Numbers, input from Listbox choices
dummyNumberTwo = Text(tab3, height=2, width=50)
dummyNumberTwo.bind("<Tab>", focus_next_widget)
dummyNumberTwo.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 3 Listbox and Textbox Attack Month--------------------------------------------------------

dummyNumberThree = Text(tab3, height=2, width=50)
dummyNumberThree.bind("<Tab>", focus_next_widget)
dummyNumberThree.grid(row=4, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 4 Listbox and Textbox Attack Year----------------------------------------------------------

dummyNumberFour = Text(tab3, height=2, width=50)
dummyNumberFour.bind("<Tab>", focus_next_widget)
dummyNumberFour.grid(row=5, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 5 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberFive = Text(tab3, height=2, width=50)
dummyNumberFive.bind("<Tab>", focus_next_widget)
dummyNumberFive.grid(row=6, column=1, columnspan=1, padx=5, pady=5)

#--------------------- Dummy 6 Listbox and Textbox ---------------------------------------------------------------------

dummyNumberSix = Text(tab3, height=2, width=50)
dummyNumberSix.bind("<Tab>", focus_next_widget)
dummyNumberSix.grid(row=7, column=1, columnspan=1, padx=5, pady=5)

#-------Tkinter Buttons------------------------------------------------------------------------------------------------
#Tab 1
# Dataset Button
datasetButton = Button(tab1, text='Dataset', command=writeDataset, width=12, bg='purple', fg='#fff')
datasetButton.grid(row=3, column=0, padx=15, pady=15)

# Tab 2
# Accuracy Button
AccuracyButton = Button(tab2, text='Prediction Accuracy', command=writeAccuracy, width=20, bg='purple', fg='#fff')
AccuracyButton.grid(row=15, column=0, padx=15, pady=15)

# Tab 3
# DummyOneButton
# http://effbot.org/tkinterbook/listbox.htm
# reference: https://stackoverflow.com/questions/17937039/tkinter-listbox-with-entry

# List 1 Origin country/region choice buttons
# Hashing the 'change answer' buttons for now in case I want to add the option in later
# DummyOneButtonChange = Button(tab3, text="Change", command = change_opt, width=20, bg='purple', fg='#fff')
# DummyOneButtonChange.grid(row=1, column=4, padx=15, pady=15)
DummyOneButtonSubmit = Button(tab3, text="Submit Attack Origin", command=lambda: get_selDummyOneTarget(), width=20, bg='purple', fg='#fff')
DummyOneButtonSubmit.grid(row=3, column=0, padx=15, pady=15)

# List 2 Origin country/region choice button
# Hashing the 'change answer' buttons for now in case I want to add the option in later
# DummyOneButtonChange = Button(tab3, text="Change", command = change_opt, width=20, bg='purple', fg='#fff')
# DummyOneButtonChange.grid(row=1, column=4, padx=15, pady=15)
DummyTwoButtonSubmit = Button(tab3, text="Submit Attack Target", command=lambda: get_selDummyTwoMonth(), width=20, bg='purple', fg='#fff')
DummyTwoButtonSubmit.grid(row=5, column=0, padx=15, pady=15)

# Dummy number Button to start algorithm calculation and display prediction results
PredictionButton = Button(tab3, text='Click to see Prediction Results', command=finalPrediction, width=25,
                          bg='blue', fg='#fff')
PredictionButton.grid(row=6, column=0, padx=5, pady=5)

# Button to clear Tab 3 and start over
ClearTabThreeButton = Button(tab3, text='Clear results and start over', command=clear_display_result, width=25,
                          bg='purple', fg='#fff')
ClearTabThreeButton.grid(row=9, column=2, padx=5, pady=5)

# Menu button on tab 1, to start program over
MenuTabOneButton = Button(tab1, text='Return to Program Main Menu', command=mainMenu, width=25,
                          bg='purple', fg='#fff')
MenuTabOneButton.grid(row=3, column=3, padx=5, pady=5)

# Button on tab 1, to exit the program
ExitTabOneButton = Button(tab1, text='Exit Program', command=exitProgram, width=14,
                          bg='purple', fg='#fff')
ExitTabOneButton.grid(row=4, column=3, padx=5, pady=5)

#------Result Display tabs---------------------------------------------------------------------------------------------

# Display Boxes for Results
tab1_display = ScrolledText(tab1, height=20, width=50)
tab1_display.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

tab2_display = ScrolledText(tab2, height=1, width=20)
tab2_display.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Prediction results window in tab 3
tab3_display = ScrolledText(tab3, height=1)
tab3_display.grid(row=7, column=0, columnspan=1, padx=5, pady=5)

# Keep window alive
mainloop()