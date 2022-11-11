from time import sleep
from os import system
from datetime import datetime as time
def white ():
    command = '"C:\\Users\\Alexandr\\AppData\\Local\\Microsoft\\Windows\\Themes\\white.theme & timeout /t 0 & taskkill /im "systemsettings.exe" /f"'
    system (command)
    return 0
def dark ():
    command = '"C:\\Users\\Alexandr\\AppData\\Local\\Microsoft\\Windows\\Themes\\dark.theme & timeout /t 0 & taskkill /im "systemsettings.exe" /f"'
    system (command)
    return 0

white()
while True :
    hour = time.now().hour
    print (hour)
    if hour >= 19:
        dark()
        sleep (28800)
    sleep (60)
