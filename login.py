from data import *
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
        print("A jelszó túl rövid (minimum 6 karakter!)")
        newPassword = input("Jelszó: ")
        
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
    username = input("Adjon meg egy felhasználónevet: ")
    while username not in usernameList:
        print("Nincs ilyen felhasználónév!")
        username = input("Adjon meg egy felhasználónevet: ")

    for i in range(len(usernameList)):
        if usernameList[i] == username:
            break
    
    password = input("Adja meg jelszavát: ")
    if passwordList[i] == password:
        print("Sikeres bejelentkezés!")
        return username, True
    print("Sikertelen bejelentkezés!")
    return username, False

def login_menu():
    sikeres = False
    while sikeres == False:
        fiok = input("a)Regisztrálás\nb)Bejelentkezés\nc)Kilépés\n")
        if fiok == "a":
            userToLogin,sikeres = register()
        if fiok == "b":
            userToLogin,sikeres = login()
        if fiok == "c":
            sys.exit()
    #menu(userName=userToLogin)
    return userToLogin
