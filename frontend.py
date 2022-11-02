'''
File tartalma:
    -szöveghez: -színek
                -félkövér
                -dőlt
                -aláhúzott
    -alkalmazás betöltő szövege ("boot") --> random ételes idézet vagy vicc és a logo ascii karakterekből
'''

class Format:
    """Szöveg előtt használja a

            `BOLD` - félkövér

            `ITALIC` - dőlt

            `UNDERLINE` - aláhúzott

    jelzőket, majd ahol abba szeretné hagyni az ÖSSZES formázást, tegye az `END`-et (Akár sorokkal később)."""
    BOLD      = "\033[1m"
    ITALIC    = "\033[3m" 
    UNDERLINE = "\033[4m"
    END       = "\033[0m"


class Color:
    """Szöveg előtt használja, `Format.END`-del törölheti az összes formázást."""
    RED     = "\033[31m"
    GREEN	= "\033[32m"
    YELLOW	= "\033[33m"
    BLUE	= "\033[34m"
    MAGENTA	= "\033[35m"
    CYAN	= "\033[36m"
    WHITE	= "\033[37m"
    DEFAULT	= "\033[39m"

def text(*arg):
    '''Szöveg színének és/vagy formázásának gyors megváltoztatása.
        Két féle módon:

                `Color.NAME` vagy `Format.NAME` megadása. (Pl: `Color.RED` , `Format.BOLD`)

                Névvel megadva idézőjelek között (pl: `"red"` , `"BLUE"` , `"dEfAuLt"` , `"boLD"` , stb.)

    '''
    colorList = Color.__dict__
    formatList = Format.__dict__
    for x in arg:
        xStr = str(x).upper()
        
        if xStr in colorList:
            print(Color.__dict__[xStr],end="")
        elif xStr in formatList:
            print(Format.__dict__[xStr],end="")
        elif x[0] == Format.BOLD[0]:
            print(x,end="")

        #print(f"{ord(x[0])}")


import random

def boot():
    wisedomList = []
    with open("wisdom.txt","r",encoding="UTF-8") as file:
        for row in file:
            wisedomList.append(row)
        randomInListIndex = random.randint(0,len(wisedomList)-1)

    text("end","red",Format.UNDERLINE,"blue")
    print(f"{wisedomList[randomInListIndex]}")

boot()