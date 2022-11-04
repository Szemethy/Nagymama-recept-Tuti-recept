from data import *

bemenet = input('Felhasználónév: ')

# count = 0

# while count < len(feljel) and check(feljel[count],0):
#     count += 1
# if len(feljel) > count:
#     print("Sikeres név")
# else:
#     print('Hibás felhasználónév')


# bemenet2 = input("Jelszó: ")

# count = 0
# while count < len(feljel) and check(feljel[count],1):
#     count += 1
# if len (feljel) > count:
#     print("Sikeres bejelentkezés")
# else:
#     print("Hibás jelszó")

i = 0
while bemenet != check(feljel[i],0):
    print('Nincs ilyen felhasználónév')
else:
    print('Sikeres név')


bemenet2 = input("Jelszó: ")

i = 0
while bemenet != check(feljel[i],1):
    print("Hibás jelszó")
else:
    print("Sikeres bejelentkezés")