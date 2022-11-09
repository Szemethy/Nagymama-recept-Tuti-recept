import os

def menu():
    os.system('cls')
    print('1..Új étel rögzítése')
    print('2..Étel módosítása')
    print('3..Étel keresése (név alapján)')
    print('4..Az összes étel neve, elkészítési ideje, nehézségi szintje')
    print('')
    print('0..Kilépés a programból')

    choice = input('\nVálasztás (0..4): ')
    while len(choice) != 1 or choice < '0' or choice > '4':
        choice = input('\nVálasztás (0..4): ')

    os.system('cls')
    return int(choice)