import appsList
import random
import time
import os 

#apps menu
print("Getting apps ist...")
for x in appsList.apps:
    print(x)
chosenApp = input("Select app here: ")

#app processing
if chosenApp == "1":
    print("Going to app installer...")
    time.sleep(random.uniform(0,1))
    os.system("python3 appInstaller.py")

elif chosenApp == "111011001":                          #app developer options
    print("Going to app deleloper options...")
    time.sleep(random.uniform(0,1))
    os.system("python3 appdev.py")
    
elif chosenApp == "101011001":                          #main developer options
    print("Going to dev options")
    time.sleep(0.25)
    os.system("python3 devOptions.py")