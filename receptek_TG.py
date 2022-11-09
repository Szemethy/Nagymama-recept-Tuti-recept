from functions import modifyResult, readFile, newResult, searchByName
from menu import menu

readFile()
choice = menu()
while choice != 0:
    if choice == 1:
        newResult()
    if choice == 2:
        modifyResult()
    if choice == 3:
        searchByName()
    choice = menu()
    