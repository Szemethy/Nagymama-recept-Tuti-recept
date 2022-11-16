from msvcrt import getwch;import os
from booter import getBooterText, boot
from login import login_menu
from menu import menuStart, menuPrint, menuTexts, getMenuInput
from functions import foods,readFile,searchByName,newResult,modifyResult

if __name__ == "__main__":
    os.system("cls")
    readFile()

    #getBooterText()
    #boot()
    #user = login_menu()
    mistakes = 0
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
                searchByName()
            case "3":
                newResult()
            case "4":
                modifyResult()
            case "5":
                pass
        os.system("cls")
        

    