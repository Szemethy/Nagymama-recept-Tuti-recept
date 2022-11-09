felhasznalonev = []
jelszo = []
nevek = []


def register():
    nevek.append(input("Név: "))
    felhasznalonev.append(input("Felhasználónév: "))
    jelszo.append(input("Jelszó: "))


def login():
    username = input("Enter your username:")
    password = input("Enter your Password:")
    if username in felhasznalonev and password in jelszo:
        print("Sikeres bejelentkezés\n")
    else:
        print("Sikertelen bejelentkezés!\n")



