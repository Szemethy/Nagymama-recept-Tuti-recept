from msvcrt import getwch;import os
from booter import getBooterText, boot
from login import login_menu
from menu import menuStart, menuPrint, menuTexts, getMenuInput
from functions import foods,readFile

if __name__ == "__main__":
    os.system("cls")
    readFile()

    #getBooterText()
    #boot()
    #user = login_menu()

    choice = ''
    while choice != "0":
        menuStart(userName="xd",markiplier=.0)
        menuPrint(markiplier=.0)
        choice = getMenuInput()
        os.system("cls")
        match choice:
            case "1":
                foods()
            case "2":
                pass
            case "3":
                pass 
        os.system("cls")
        

    