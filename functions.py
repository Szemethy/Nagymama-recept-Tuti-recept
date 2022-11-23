from result import Result
from frontend import *
import os

results = []

def readFile():
    results.clear()
    f = open('etelek.csv', 'r', encoding='UTF-8')
    f.readline() 
    for row in f:
        r = Result(row.strip())
        results.append(r)
    f.close()

def writeFile():
    f = open('etelek.csv', 'w', encoding='UTF-8')
    for r in results:
        row = f'{r.name};{r.time};{r.difficult}\n'
        f.write(row)
    f.close()

def modifyResult():
    name = input('Név: ')
    for r in results:
        if r.name.lower() == name.lower():
            # index = results.index(r)     # r elem indexe a results listában
            r.time = input('Idő ( perc): ')
            r.difficult = input('Nehézség (könnyű, közepes, bonyolult): ')       
            writeFile()
            return
    input('Ilyen nevű étel nincs az adatbázisban')

def newResult():
    name = input('Adja meg a nevét: ')
    time = input('Idő (perc): ')
    difficult = input('Nehézség (könnyű, közepes, bonyolult): ')
    prep = input('Lépések: ')
    ing = input('Hozzávalók: ') 

    row = f'{name};{time};{difficult};{prep};{ing}\n'
    with open('etelek.csv', 'a', encoding='UTF-8') as f:
        f.write(row)

    r = Result(row)
    results.append(r)



def smallText(i,r):
    #randomColor()
    slowPrint(f'[{i+1}.] {r.name}, {r.time} perc, {r.difficult}\n',markiplier)

def foods():
    for i,r in enumerate(results):
        smallText(i,r)

def allDataByNameOrIndex(nameOrIndex, isByIndex:bool=True):
    '''Megj.: `nameOrIndex` = vagy a név vagy az index az `isByIndex` alapján.'''
    if isByIndex:
        r = results[nameOrIndex]
    else:
        for r in results:
            if nameOrIndex.lower() == r.name.lower():
                break
    os.system("cls")
    print(f'{r.name}, {r.time} perc, {r.difficult}\n{r.preparation} \n{r.ingredients}')

def searchByName():
    name = input('Név: ')
    count = 0
    indexList = []
    for i,r in enumerate(results):
        if name.lower() in r.name.lower():
            smallText(count,r)
            count += 1
            indexList.append(i)
    if count == 0:
        return False
    elif count == 1:
        allDataByNameOrIndex(nameOrIndex=indexList[0],isByIndex=True)
        return 1
    return indexList

'''
def nameTimeDif():
    name = input('Név: ')
    for r in results:
        if name.lower() == r.name.lower():
            print(f'{r.name}, {r.time} perc, {r.difficult}')
    input('\n')

def ingredients():
    name = input('Név: ')
    for r in results:
        if name.lower() == r.name.lower():
            print(f'{r.ingredients}')
    input('\n')

def preparation():
    name = input('Név: ')
    for r in results:
        if name.lower() == r.name.lower():
            print(f'{r.preparation}')
    input('\n')
'''