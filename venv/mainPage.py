# This page is being built of the template referenced on the TestPage.py.  It will be the main page with
# menu options for the program eventually.

# It is stil in the initial stages of being built.

import random


class MainMenu():

    # Creating menu method with user input for non-contacts pages
    def main(self):

        lottoContacts = Definitions()
        mainM = MainMenu()

        chooseRunQuit = str(input("\n" + "Please choose:" + "\n\n" +
                                  "GO - to return to the " +
                                  "main screen" + "\n" +
                                  "QUIT - to exit the program" + "\n\n" +
                                  "Please enter your choice here / Por favor ingrese su elección aquí: "))

        if chooseRunQuit == "GO":
            Choice()


        if chooseRunQuit == "QUIT":
            exit()

        else:
            print("Incorrect entry. Please try again.")
            mainM.main()

    # Creating menu method with user input for the Contacts pages (gives customer the choice to return to the
    # Contacts page first, rather than the first choice being for the main menu)

MainMenu()

def Choice():

    #Naming variables to pull methods from the Balls() class

    mainM = MainMenu()




# Setting introduction and instructions for Powerball Success Number Generator

    print("\n\n" + "Welcome to the SVM Cyber-Attack Predication Project! " + "\n")

# Setting up the actual input method LotteryChoices for Choice() class; also added spanish translation to the menu

    LotteryChoices = str(input("Please choose: " + "\n\n" +

                               "SVM - to try the SVM and KNN algorithm to " +
                               "make a cybersecurity prediction" + "\n\n" +
                               "Enter your choice here: "))



    if LotteryChoices == "SVM":

        import LocationTarget

    else:
        print("Incorrect entry. Please try again.")
        mainM.main()


Choice()

