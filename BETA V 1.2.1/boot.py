#import stuff

import time

import os

import random 



#welcome stuff

print("Welcome to the Cali Computer!")

print("Would you like to [boot] or enter [bios]")

bootOption = input("Enter option here: ")



#logic for boot and bios

if bootOption == "boot":

    print("Booting...")

    time.sleep(random.uniform(0,2))

    os.system("python3 desktop.py")



elif bootOption == "bios":

    print("Entering BIOS...")

    time.sleep(random.uniform(0,2))

    os.system("python3 bios.py")



elif bootOption == "101011001":                 #dev options

    print("!!! YOU HAVE ENTERED THE DEVELOPER MENU !!!")

    continueConfirm = input("Continue? (Y/n)")



    if continueConfirm == "n":

        print("!!! EXITING NOW !!!")

        time.sleep(random.uniform(0,2))

        os.system("python3 boot.py")

    elif continueConfirm == "Y":

        print("Entering Dev options...")

        time.sleep(random.uniform(0,2))

        os.system("python3 devOptions.py")



else:

    print("That is not a valid option!")
