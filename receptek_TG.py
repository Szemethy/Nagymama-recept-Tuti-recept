from menu_TG import menu
from functions_TG import modifyResult, readFile, newResult, searchByName, allData, ingredients, preparation, nameTimeDif
from menu_TG import menu2
from functions_TG import *
import os

readFile()
choice = menu()
while choice != 0:
    if choice == 1:
        newResult()
    if choice == 2:
        modifyResult()
    if choice == 3:
        menu2()
        if choice == 5:
            searchByName()
        if choice == 6:
            nameTimeDif()
        if choice == 7:
            ingredients()
        if choice == 8:
            preparation()
    if choice == 4:
        foods()
    choice = menu()
