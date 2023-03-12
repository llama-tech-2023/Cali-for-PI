#import the good stuff
import settings
import random
import users
import time
import os

#sign in stuff
print("Welcome to Cali OS!")

#print all users
for x in users.users:
    print(x)

#welcome message
settings.userSelect = input("Enter user: ")
time.sleep(random.uniform(0,2))
print("Welcome " + settings.userSelect)
time.sleep(random.uniform(0,2))

#menu
print("Menu option are: ")
print("Go to [settings]")
print("Go to [apps]")
print("[0] power off")

menuOption = input("Enter option here: ")

if menuOption == "0":                           #power off
    print("Powering off...")
    time.sleep(random.uniform(0,2))
    os.system("sudo shutdown")

elif menuOption == "apps":                      #apps menu
    print("Going to apps menu...")
    time.sleep(random.uniform(0,1))
    os.system("python3 apps.py")

elif menuOption == "101011001":                 #dev options
    print("!!! YOU HAVE ENTERED THE DEVELOPER MENU !!!")
    rawContinueConfirm = input("Continue? (Y/n)")
    continueConfirm = rawContinueConfirm.lower()

    if continueConfirm == "n":
        print("!!! EXITING NOW !!!")
        time.sleep(random.uniform(0,2))
        os.system("python3 desktop.py")
    elif continueConfirm == "Y":
        print("Entering Dev options...")
        time.sleep(random.uniform(0,2))
        os.system("python3 devOptions.py")
else:
    print("That is not a valid option!")
    os.system("python3 desktop.py")