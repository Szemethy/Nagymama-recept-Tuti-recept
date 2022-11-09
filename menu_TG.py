import os

def menu():
    os.system('cls')
    print('1. Új étel rögzítése')
    print('2. Étel módosítása')
    print('3. Étel keresése (név alapján)')
    print('')
    print('0..Kilépés a programból')

    choice = input('\nVálasztás (0..3): ')
    while len(choice) != 1 or choice < '0' or choice > '3':
        choice = input('\nVálasztás (0..3): ')

    os.system('cls')
    return int(choice)