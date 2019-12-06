#!/usr/bin/env python

import time
import numpy as np
start_time = time.time()

xLen = 300
yLen = 300

#Part1
#minSquareSize = 3
#maxSquareSize = 3

#Part2
minSquareSize = 1
maxSquareSize = 300

def getHundreds(integer):
    res = 0
    if(integer >= 100):
        res = int(str(integer)[-3])
    return res

def setPowerLevels(fuelCellGrid, gridSerialNumber):
    for x in range(xLen):
        for y in range(yLen):
            rackId = x + 10
            pwrLvl = rackId * y
            pwrLvl = pwrLvl + gridSerialNumber
            pwrLvl = pwrLvl * rackId
            pwrLvl = getHundreds(pwrLvl)
            pwrLvl -= 5
            fuelCellGrid[y][x] = pwrLvl
            
    return fuelCellGrid
    
def calculatePwrLvls(fuelCellGrid, squareSize):
    pwrLvlGrid = np.zeros((xLen-squareSize+1, yLen-squareSize+1))
    for x in range(len(pwrLvlGrid[0])):
        for y in range(len(pwrLvlGrid[0])):
            pwrLvlGrid[y][x] = fuelCellGrid[y:y+squareSize, x:x+squareSize].sum()
    return pwrLvlGrid
    
def getLargestTotalPowerXYCoordinate(fuelCellGrid):
    largestSquareSize = 0
    largestX = 0
    largestY = 0
    largestLevel = 0
    for size in range(minSquareSize, maxSquareSize+1):
        pwrLvlGrid = calculatePwrLvls(fuelCellGrid, size)
        for x in range(len(pwrLvlGrid[0])):
            for y in range(len(pwrLvlGrid[0])):
                if (pwrLvlGrid[y][x] > largestLevel):
                    largestLevel = pwrLvlGrid[y][x]
                    largestX = x
                    largestY = y
                    largestSquareSize = size
                
    return largestX, largestY, largestLevel, largestSquareSize

fuelCellGrid = np.zeros((xLen, yLen))
fuelCellGrid = setPowerLevels(fuelCellGrid, 5034)
x, y, lvl, squareSize = getLargestTotalPowerXYCoordinate(fuelCellGrid)
print("Answer ==> X,Y,Size: " + str(x) + "," + str(y) + "," + str(squareSize))

print("--- %s seconds ---" % (time.time() - start_time))