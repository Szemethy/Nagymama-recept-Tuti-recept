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
    with open('etelek.csv', 'w', encoding='UTF-8') as f:
        for r in results:
            print(r)
            row = f'{r.name};{r.time};{r.difficult};{r.preparation};{r.ingredients}\n'
            f.write(row)

def newResult():
    name = input('Adja meg a nevét: ')
    time = input('Idő (perc): ')
    difficult = input('Nehézség (könnyű, közepes, bonyolult): ')
    prep = input('Lépések: ')
    ing = input('Hozzávalók: ') 

    row = f'{name};{time};{difficult};{prep};{ing}\n'
    return row, [name,time,difficult,prep,ing]

def addResultToEnd(row):
    with open('etelek.csv', 'a', encoding='UTF-8') as f:
        f.write(row)

    r = Result(row)
    results.append(r)

def changeResultById(id:int,rowlist:list):
    results[id] = rowlist
    writeFile()
    

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
            #smallText(count,r)
            count += 1
            indexList.append(i)
    if count == 0:
        return indexList,False
    elif count == 1:
        return indexList,"1"

    for i,r in enumerate(indexList):
        smallText(i,results[r])
    return indexList,True

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