import random
import time
import os

#warning and welcome
print("!!! WARNING: You are now in the developer menu for Cali OS !!!")
print("Some changes can seriously damage your system!!!")
print("At any option you can enter [0] to exit this menu and go back to the boot process")

#options
print("You can change [settings] or you can change [options]")
print("You can also [close] the os")

rawOption = input("What would you like to change: ")
option = rawOption.lower()

if option == "close":
    confirmExit = input("Are you sure you want to exit the os? (Y/n)")

    if confirmExit == "Y":
        print("Exiting os...")
        time.sleep(random.uniform(0,1))
        quit()
    elif confirmExit == "n":
        print("Returning to boot...")
        time.sleep(random.uniform(0,1))
        os.system("python3 boot.py")

elif option == "0":
    print("Quitting....")
    time.sleep(0.25)
    os.system("python3 boot.py")

elif option == "settings":
    print("What would you like to change:")
    print("[1] boot time")
    print("[2] user password -- not a feature yet")
    print("[3] add user")

    #process input
    settingOption = int(input("Enter option here: "))

    if settingOption == "1":                                #boot time
        print("Preparing to change boot time...")
        time.sleep(random.uniform(0,1))
        print("Fetching open apps...")
        rawOpenApps = open("openApps.txt", "r")
        openApps = rawOpenApps.read()
        print(openApps)
        rawOpenApps.close()
        rawCloseConfirm = input("Would you like to close all running apps? (Y/n): ")
        closeConfirm = rawCloseConfirm.lower()

        #close processing
        if closeConfirm == "y":
            closeApps = open("openApps.txt", "w")
            closeApps.write("\n")
        elif closeConfirm == "n":
            print("Exiting to boot...")
            time.sleep(random.uniform(0,1))
            os.system("python3 boot.py")
        else:
            print("That is not a valid option!")
            print("Error : 100000000")
            print("Falling back to the boot page...")
            os.system("python3 boot.py")

    elif settingOption == "2":                              #change password
        print()

    elif settingOption == "3":                              #add user
        print("Preparing to add user...")
        time.sleep(random.uniform(0,1))
        print("Preperation done!")
        print("You can now enter the new users name in the users.py file")
        print("Exiting the system to allow for change...")
        time.sleep(random.uniform(0,1))
        quit()

    elif settingOption == "0":
        print("Quitting....")
        time.sleep(0.25)
        os.system("python3 boot.py")

    else:
        print("That is not a valid option!")
        print("Error : 100000000")
        print("Falling back to the boot page...")
        os.system("python3 boot.py")

else:
    print("That is not a valid option!")
    print("Error : 100000000")
    print("Falling back to the boot page...")
    os.system("python3 boot.py")