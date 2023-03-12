import random
import time
import os

#welcome stuff
print("You are not in the app installer, be sure to continue all of the way through and do not turn")
print("off your system to avoid damageing it.")
startConfirm = input("Would you like ot continue? (Y/n)")

if startConfirm == "n":
    print("Exiting now...")
    time.sleep(random.uniform(0,1))
    os.system("python3 desktop.py")

elif startConfirm == "Y":
    print("Confirmed!")
    print("Please enter the name of the app you would like to install.")
    appToInstall = input("Enter the app name here: ")
    appDirectory = input("Enter the direcotry of the app, if none enter [none]: ")
    
    if appToInstall == "111011001":
        print("Going to app deleloper options...")
        time.sleep(random.uniform(0,1))
        os.system("python3 appdev.py")

    if appDirectory == "111011001":
        print("Going to app deleloper options...")
        time.sleep(random.uniform(0,1))
        os.system("python3 appdev.py")

    elif appDirectory == "none":
        print("[[[ no directory selected ]]]")
        time.sleep(random.uniform(0,1))
        print("Starting install..")
        os.system("python3 " + appToInstall)
    else:
        print("Directory: " + appDirectory + " selected!")
        time.sleep(random.uniform(0,1))
        print("Starting install...")
        time.sleep(random.uniform(0,1))
        os.system("python3 " + appDirectory + appToInstall)