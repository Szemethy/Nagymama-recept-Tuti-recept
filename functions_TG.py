from result_TG import Result

results = []

def readFile():
    results.clear()
    f = open('etelek.csv', 'r', encoding='UTF-8')
    f.readline() 
    for row in f:
        r = Result(row.strip())
        results.append(r)
    f.close

def searchByName():
    name = input('Név: ')
    for r in results:
        if name.lower() in r.name.lower():
            print(f'{r.name}, {r.time} perc, {r.difficult}')
    input('\n')

def newResult():
    name = input('Név: ')
    time = input('Idő (perc): ')
    difficult = input('Nehézség (könnyű, közepes, bonyolult): ')

    row = f'{name};{time};{difficult}\n'
    f = open('etelek.csv', 'a', encoding='UTF-8')
    f.write(row)
    f.close()

    r = Result(row)
    results.append(r)

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

def foods():
    f = open('etelek.csv', 'r', encoding='UTF-8')
    for r in results:
        print(f'{r.name}, {r.time} perc, {r.difficult}, \nElkészítése:\n{r.preparation}, \nHozzávalók:\n{r.ingredients}\n\n\n\n')
    f.close
    input('\n')

def allData():
    name = input('Név: ')
    for r in results:
        if name.lower() == r.name.lower():
            print(f'{r.name}, {r.time} perc, {r.difficult}, \n{r.preparation}, \n{r.ingredients}')
    input('\n')

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