from data import *

felhasznalonev = []
jelszo = []
nevek = []


def register():
    nevek.append(input("Név: "))
    felhasznalonev.append(input("Felhasználónév: "))
    jelszo.append(input("Jelszó: "))
    # f = open('feljel.csv', 'a', encoding="UTF-8")
    # f = write(f'{nevek}\n')
    # f.close()


def login():
    username = input("Enter your username:")
    password = input("Enter your Password:")
    if username in felhasznalonev and password in jelszo:
        print("Sikeres bejelentkezés\n")
    else:
        print("Sikertelen bejelentkezés!\n")


while True:
    fiok = input("a)Regisztrálás\nb)Bejelentkezés\nc)Kilépés\n")
    if fiok == "a":
        register()
    if fiok == "b":
        login()
    if fiok == "c":
        break
