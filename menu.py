from frontend import *
import os
from msvcrt import getwch

menuTexts = ["Összes recept","Receptek keresése","Saját publikálása","Meglévő módosítása","Recept bejelentése (törlés)"]

def menuStart(userName="Bugxd",markiplier=1):
    os.system('cls')
    text(Color.CYAN)
    slowPrint("Üdvözlünk ",0.05*markiplier)
    text(Format.BOLD,Format.ITALIC,Color.BLUE)
    slowPrint(f"{userName}!\n\n",0.04*markiplier)
    text("end")

def menuPrint(markiplier=1):
    text("end")
    slowPrint("Miben segíthetünk?\n\n",0.02*markiplier) #több megoldás hozzáadása később

    menuColor = lambda x: Color.MAGENTA if x % 2 else Color.RED
    
    #Egybe:
    #1.recept lista
    #2.kedvencek
    #3.recept publikálása
    #4.recept módosítása
    #5.recept eltávolítása
    for i,row in enumerate(menuTexts):
        text(menuColor(i))
        slowPrint(f"{i+1}. {row}\n",0.02*markiplier)
        text("end")
    
    #0.kilépés
    print("\n\t")
    text(Format.ITALIC)
    slowPrint(f"0. kilépés\n\n",0.02*markiplier)
    text("end")


def getMenuInput():
    choice = getwch()
    menuLenght = len(menuTexts)

    mistaceCount = 0
    while choice.isnumeric() == False or int(choice) < 0 or int(choice) > menuLenght: #Amíg nem szám az input
        mistaceCount+=1
        
        print(f"Ez az opció nem létezik, kérem próbálja újra!")
        
        choice = getwch()
    return choice
