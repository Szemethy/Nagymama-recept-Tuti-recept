feljel = []

def splitter(string:str):
    return string.split(";")

def readFile(fileName = 'feljel.csv'):
    f = open(fileName, 'r', encoding="UTF-8-sig")
    for row in f:
        feljel.append(row)
    f.close()

def writeFile(fileName = 'feljel.csv'):
    f = open('feljel.csv', 'w', encoding="UTF-8")
    for recept in feljel:
        f.write(f'{recept}\n')
    f.close()