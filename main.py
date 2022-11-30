from msvcrt import getwch;import os
from booter import getBooterText, boot
from login import login_menu
from menu import menuStart, menuPrint, menuTexts, getMenuInput
from functions import foods,readFile,searchByName,newResult,changeResultById,allDataByNameOrIndex,addResultToEnd,results
from frontend import *

def betterChoice(openIndex,charsToGet:int):
    print()
    openIndex = ""
    for i in range(0,charsToGet):
        openIndex += getwch()
        print(openIndex[i],end="")

if __name__ == "__main__":
    os.system("cls")
    readFile() #functions

    #getBooterText()
    #boot()
    #user = login_menu()
    mistakes = 0
    choice = ''
    while choice != "0":
        menuStart(userName="xd",markiplier=markiplier)
        menuPrint(markiplier=markiplier)
        choice = getMenuInput()
        os.system("cls")
        match choice:
            case "1":
                foods()
                #betterChoice(openIndex,2)
                openIndex = input("Index? ")
                while not(openIndex.isnumeric()) or not(0 < int(openIndex) < len(results)+1):
                    openIndex = input("Index? ")
                openIndex = int(openIndex)-1 #gépindex-é emberindex helyett
                allDataByNameOrIndex(nameOrIndex=openIndex,isByIndex=True)
                getwch()
            case "2":
                indexList,isFound = searchByName()
                if isFound == "1":
                    allDataByNameOrIndex(nameOrIndex=indexList[0],isByIndex=True)
                elif isFound == True:
                    openIndex = input("Index ")
                    while not(openIndex.isnumeric()) or not(0 < int(openIndex) < len(indexList)+1):
                        openIndex = input("Index? ")
                    openIndex = int(openIndex)-1
                    searchedIndex = indexList[openIndex]
                    allDataByNameOrIndex(nameOrIndex=searchedIndex,isByIndex=True)
                else: slowPrint("Ilyen nevű receptünk nincs! :c",0.01*markiplier)
                getwch()
            case "3":
                row,rowlist = newResult()
                addResultToEnd(row)
            case "4":
                indexList,isFound = searchByName()
                if isFound == "1":
                    #allDataByNameOrIndex(nameOrIndex=indexList[0],isByIndex=True)
                    row,rowlist = newResult()
                    changeResultById(indexList[0],rowlist)
                elif isFound == True:
                    openIndex = input("Index ")
                    while not(openIndex.isnumeric()) or not(0 < int(openIndex) < len(indexList)+1):
                        openIndex = input("Index? ")
                    openIndex = int(openIndex)-1
                    searchedIndex = indexList[openIndex]
                    #allDataByNameOrIndex(nameOrIndex=searchedIndex,isByIndex=True)
                    row,rowlist = newResult()
                    changeResultById(searchedIndex,rowlist)
                else: slowPrint("Ilyen nevű receptünk nincs! :c",0.01*markiplier)
                getwch()
            case "5":
                pass
        os.system("cls")
        

    