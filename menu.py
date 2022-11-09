from frontend import *
from booter import *

def menu(userID=0,userName="Carlos"):
    text(Color.CYAN)
    slowPrint("Üdvözlünk ",0.05)
    text(Format.BOLD,Format.ITALIC,Color.BLUE)
    slowPrint(f"{userName}!\n\n",0.04)

    
    text("end")
    slowPrint("Miben segíthetünk?\n\n",0.02) #több megoldás hozzáadása később


    menuColor = lambda x: Color.MAGENTA if x % 2 else Color.RED
    menuTexts = ["Receptek","Kedvencek","Saját publikálása","Meglévő módosítása","Recept bejelentése (törlés)"]
    
    #Egybe:
    #1.recept lista
    #2.kedvencek
    #3.recept publikálása
    #4.recept módosítása
    #5.recept eltávolítása
    for i,row in enumerate(menuTexts):
        text(menuColor(i))
        slowPrint(f"{i+1}. {row}\n",0.02)
        text("end")
    
    #0.kilépés
    print("\n\t")
    text(Format.ITALIC)
    slowPrint(f"0. kilépés\n",0.02)


getBooterText()
boot()
#bejelentkezés()
menu()