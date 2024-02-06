from decimal import Clamped
from classes import *
from os import system
import time
import math
from muncherBrain import debugMode, speed, amountOfTurns

def main():
    map: Map = Map(32, 16)
    muncher: Muncher = Muncher(16, 8, map)
    for i in range(1, amountOfTurns+1):
        muncher.update()
        if not debugMode:
            system("clear")
        print()
        print("Score: " + str(muncher.score))
        print("Turn: " + str(i) + "/" + str(amountOfTurns))
        print(map.getMapAsString())
        time.sleep(speed)
    
    print("TIMES UP, your score is: " + str(muncher.score))
    
    if amountOfTurns != 1000:
        print("Since amountOfTurns has been modified this run does not count.\nIf you wish to restore it to its default set it equal to 1000.")
        return
    
    maxScore: int = getMaxScore("maxScore.txt")
    if maxScore < muncher.score:
        print("NEW MAX SCORE")
        writeNewMaxScore("maxScore.txt", muncher.score)
    else:
        print("Current max score is: " + str(maxScore))

    grade: int = int(((muncher.score/amountOfTurns)/0.55)*100)
    if grade > 100:
        grade = 100
    print("Grade: " + str(grade) + "%") 
    
def getMaxScore(fileName: str) -> int:
    f = open(fileName, "r")
    maxScoreStr: str = f.read()
    maxScoreInt: int = 0
    if maxScoreStr != "" and maxScoreStr.isdecimal():
        maxScoreInt = int(maxScoreStr)

    return maxScoreInt

def writeNewMaxScore(fileName: str, newMaxScore: int) -> None:
    f = open(fileName, "w")
    f.write(str(newMaxScore))

main()