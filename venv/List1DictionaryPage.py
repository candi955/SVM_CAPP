# List 1 Dictionary page

import pandas as pd


#------------ListBox Country/Region/binary Dictionary--------------------------------------------------------------------------
# creating a dictionary to associate locations with associated binary
# reference: https://www.w3schools.com/python/python_dictionaries.asp

listOneDictionary = {"China":{"binary": 418464229443},
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629},
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}
                "USA":{"binary" : 4281173},
                "Russia":{"binary" : 107105536406866},
                "Asia":{"binary" : 1634300737},
                "Europe":{"binary" : 111533580514629}}


pdDict = pd.DataFrame(locationDict)
pd.set_option('display.max_rows', 1000) # Attempting to display all rows and columns
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)