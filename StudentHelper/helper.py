import os

print("Hello there! Welcome to the Amp Lab helper tool! How can I be of assistance?")

def handleQuit():
    print("Thank you for using the Amp Lab helper tool! Have a great day!")
    exit()

def handleAnythingElse():
    print("Can I help you with anything else? y/n: ")
    choice = input()
    if choice == "y":
        os.system('clear')
        pass
    elif choice == "n":
        handleQuit()

def handleOptions(options : dict):
    while True:
        os.system('clear')
        print('-------------------------------------------------')
        allOptions = list(options.keys())
        for i in range(0, len(allOptions)):
            print(f"({i}): {allOptions[i]}")
        print('-------------------------------------------------')
        choice =  int(input("Which number would you like to choose? "))
        if choice < len(allOptions) and choice >= 0:
            options[allOptions[choice]]()
            handleAnythingElse()
        else:
            print("You chose an invalid option! Try again:")
 
def handleProjectSubmission():
    os.system('clear')
    print("Please enter the commit message you would like to use:")
    commitMessage = input()

    os.system("git add .")
    os.system(f"git commit -m '{commitMessage}'")
    os.system(f"git push")

def getInTouchWithMentor():
    print("Please visit the amp lab website to get in touch with a mentor!")

handleOptions({"Submit a project update" : handleProjectSubmission, 
               "Get in touch with a mentor" : getInTouchWithMentor, 
               "Quit" : handleQuit})