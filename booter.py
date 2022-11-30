from frontend import *
import random
import time
import os

wisedomList = []

def getBooterText():
    with open("wisdom.txt","r",encoding="UTF-8") as file:
        for row in file:
            wisedomList.append(row.strip())

def boot():
    os.system('cls')

    text("bold")
    print("Betöltés, kérem várjon!",end="")
    text("end")

    minLoad = 4
    maxLoad = 11
    pointList = "." * random.randint(minLoad,maxLoad)

    #[pointList.append(".") for x in range(minLoad,maxLoad)]
    slowPrint(pointList,0.8)
    text("green","bold")
    print("KÉSZ!")
    time.sleep(1)

    os.system('cls')
    text("end")
    print("\t\t ",end="")

    text("italic","red")
    randomInListIndex = random.randint(0,len(wisedomList)-1)
    slowPrint(f'"{wisedomList[randomInListIndex]}"',0.05)
    text(Format.END)

    slowPrint("\n\n",0.8)



