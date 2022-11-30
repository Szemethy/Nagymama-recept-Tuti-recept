from data import *
import sys
from frontend import *
from msvcrt import getwch
import os

usernameList = []
passwordList = []

def makeLists():
    for row in feljel:
        splittedData = splitter(row)
        usernameList.append(splittedData[0].strip())
        passwordList.append(splittedData[1].strip())

def register():
    readFile()
    makeLists()

    text("red","bold")
    print("Felhasználónév: ",end="")
    text("end")
    newUsername = input()
    while newUsername in usernameList:
        text("italic")
        print("Olyan felhasználónevet adjon meg, ami még nem létezik!")
        text("end")

        text("red","bold")
        print("Felhasználónév: ",end="")
        text("end")
        newUsername = input()

    text("red","bold")
    print("Jelszó: ",end="")
    text("end")
    newPassword = input()

    while len(newPassword) < 6:
        text("italic")
        print("A jelszó túl rövid (minimum 6 karakter!)")
        text("end")

        text("red","bold")
        print("Jelszó: ",end="")
        text("end")
        newPassword = input()

        
    newUsername = newUsername.replace(";",",")
    newPassword = newPassword.replace(";",",")
    
    usernameList.append(newUsername)
    passwordList.append(newPassword)
    f = open('feljel.csv', 'a', encoding="UTF-8")
    f.write(f'{newUsername};{newPassword}\n')
    f.close()

    return newUsername, True


def login():
    readFile()
    makeLists()

    text("red","bold")
    print("Felhasználónév: ",end="")
    text("end")
    username = input()

    while username not in usernameList:
        text("italic")
        print("Nincs ilyen felhasználónév!")
        text("end")

        text("red","bold")
        print("Felhasználónév: ",end="")
        text("end")
        username = input()

    for i in range(len(usernameList)):
        if usernameList[i] == username:
            break
    
    text("red","bold")
    print("Jelszó: ",end="")
    text("end")

    password = input()

    text("italic")
    if passwordList[i] == password:
        #print("Sikeres bejelentkezés!")
        return username, True
    print("Sikertelen bejelentkezés!")
    text("end")
    print()
    getwch()

    return username, False

def printLogin():
    text("green")
    slowPrint("a) Regisztrálás\n",0.01*markiplier)
    text("yellow")
    slowPrint("b) Bejelentkezés\n\n",0.01*markiplier)
    text(Format.END,Format.ITALIC)
    slowPrint("c) Kilépés\n",0.01*markiplier)
    print()

def login_menu():
    sikeres = False
    printLogin()

    fiok = "alma"
    while fiok not in ["a","b","c"] or sikeres == False:
        text("end")
        if fiok == "a":
            print()
            userToLogin,sikeres = register()
        elif fiok == "b":
            print()
            userToLogin,sikeres = login()
            if sikeres == False:
                os.system("cls")
                printLogin()
                fiok = getwch()

        elif fiok == "c":
            sys.exit()
        elif fiok != "alma":
            print(f"Ez az opció nem létezik, kérem próbálja újra!")
            fiok = getwch()
        else:
            fiok = getwch()
        
    return userToLogin
