#import the good stuff
import appsList
import settings
import random
import users
import time
import os

#random time for delay
def randomTime():
    time1 = random.uniform(0,1)
    time

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

#apps menu
print("Getting apps ist...")
for x in appsList.apps:
    print(x)
chosenApp = input("Select app here: ")