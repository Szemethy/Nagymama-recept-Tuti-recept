from functions_TG import modifyResult, readFile, newResult, searchByName
from menu_TG import menu
from functions_TG import *

readFile()
choice = menu()
while choice != 0:
    if choice == 1:
        newResult()
    if choice == 2:
        modifyResult()
    if choice == 3:
        searchByName()
    if choice == 4:
        foods()
    choice = menu()
