from data import *
from menu import menu
import sys

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
    newUsername = input("Felhasználónév: ")
    while newUsername in usernameList:
        print("Olyan felhasználónevet adjon meg, ami még nem létezik!")
        newUsername = input("Felhasználónév: ")

    newPassword = input("Jelszó: ")
    while len(newPassword) < 6:
        print("A jelszó túl rövid")
        newPassword = input("Jelszó: ")
    usernameList.append(newUsername)
    passwordList.append(newPassword)
    f = open('feljel.csv', 'a', encoding="UTF-8")
    f.write(f'{newUsername};{newPassword}\n')
    f.close()
    global sikeres
    sikeres = True
    return newUsername


def login():
    readFile()
    makeLists()
    username = input("Ajdon meg egy felhasználónevet: ")
    while username not in usernameList:
        print("Nincs ilyen felhasználónév!")
        username = input("Ajdon meg egy felhasználónevet: ")

    for i in range(len(usernameList)):
        if usernameList[i] == username:
            break
    
    password = input("Ajda meg jelszavát: ")
    if passwordList[i] == password:
        print("Sikeres bejelentkezés!")
        global sikeres
        sikeres = True
    else:
        print("Sikertelen bejelentkezés!")
    return username
        
sikeres = False
while sikeres == False:
    fiok = input("a)Regisztrálás\nb)Bejelentkezés\nc)Kilépés\n")
    if fiok == "a":
        userToLogin = register()
    if fiok == "b":
        userToLogin = login()
    if fiok == "c":
        sys.exit()
menu(userName=userToLogin)
