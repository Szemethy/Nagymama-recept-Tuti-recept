from msvcrt import getwch;import os
from booter import getBooterText, boot
from login import login_menu
from menu import menuStart, menuPrint, menuTexts, getMenuInput
from functions import foods,readFile,searchByName,newResult,modifyResult,allDataByNameOrIndex,results

if __name__ == "__main__":
    os.system("cls")
    readFile() #functions

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
                openIndex = input("Index? ")
                while not(openIndex.isnumeric()) or not(0 < int(openIndex) < len(results)+1):
                    openIndex = input("Index? ")
                openIndex = int(openIndex)-1 #gépindex-é emberindex helyett
                allDataByNameOrIndex(nameOrIndex=openIndex,isByIndex=True)
            case "2":
                indexList = searchByName()
                if indexList:
                    openIndex = input("Index? ")
                    while not(openIndex.isnumeric()) or not(0 < int(openIndex) < len(indexList)+1):
                        openIndex = input("Index? ")
                    openIndex = int(openIndex)-1
                    searchedIndex = indexList[openIndex]
                    allDataByNameOrIndex(nameOrIndex=searchedIndex,isByIndex=True)     
            case "3":
                newResult()
            case "4":
                modifyResult()
            case "5":
                pass
        os.system("cls")
        

    