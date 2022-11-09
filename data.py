
feljel = []

def readFile(fileName = 'feljel.csv'):
    f = open(fileName, 'r', encoding="UTF-8")
    for row in f:
        feljel.append(row.strip())
    f.close()

def writeFile(fileName = 'feljel.csv'):
    f = open('fel.jel.csv', 'w', encoding="UTF-8")
    for recept in feljel:
        f.write(f'{recept}\n')
    f.close()



# feljel = [
#     "Pista;fashsdf",
#     "Béla;gew3",
#     "Józsi;34wf",
#     "Ferenc;34256t4g",
#     "Vlagyi;fassdf45",
#     "János;daw3",
#     "Viktor;35wrf",
#     "Arany;fawe334 "
# ]

# def check(inputData: str, hely: int):
#     splitted = inputData.split(";")
#     return splitted[hely]
