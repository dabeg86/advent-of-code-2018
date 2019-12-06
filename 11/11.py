#!/usr/bin/env python

import time
start_time = time.time()

xLen = 300
yLen = 300
#minSquareSize = 1
#maxSquareSize = 300
minSquareSize = 3
maxSquareSize = 3

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
    pwrLvlGrid = [[0 for x in range(xLen-squareSize+1)] for y in range(yLen-squareSize+1)]
    for x in range(len(pwrLvlGrid[0])):
        for y in range(len(pwrLvlGrid[0])):
            #print(squareSize)
            #print(x)
            #print(y)
            pwrLvlGrid[y][x] = sum(fuelCellGrid[y][x:x+squareSize])+sum(fuelCellGrid[y+1][x:x+squareSize])+sum(fuelCellGrid[y+2][x:x+squareSize])
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

fuelCellGrid = [[0 for x in range(xLen)] for y in range(yLen)]

#Example inputs
#fuelCellGrid = setPowerLevels(fuelCellGrid, 8)
#print(fuelCellGrid[5][3])
#fuelCellGrid = setPowerLevels(fuelCellGrid, 57)
#print(fuelCellGrid[79][122])
#fuelCellGrid = setPowerLevels(fuelCellGrid, 39)
#print(fuelCellGrid[196][217])
#fuelCellGrid = setPowerLevels(fuelCellGrid, 71)
#print(fuelCellGrid[153][101])

fuelCellGrid = setPowerLevels(fuelCellGrid, 18)
x, y, lvl, squareSize = getLargestTotalPowerXYCoordinate(fuelCellGrid)
print("X,Y: " + str(x) + "," + str(y))
print("Lvl: " + str(lvl))
print("Size: " + str(squareSize))

fuelCellGrid = setPowerLevels(fuelCellGrid, 42)
x, y, lvl, squareSize = getLargestTotalPowerXYCoordinate(fuelCellGrid)
print("X,Y: " + str(x) + "," + str(y))
print("Lvl: " + str(lvl))
print("Size: " + str(squareSize))

fuelCellGrid = setPowerLevels(fuelCellGrid, 5034)
x, y, lvl, squareSize = getLargestTotalPowerXYCoordinate(fuelCellGrid)
print("Part1 ==> X,Y: " + str(x) + "," + str(y))
print("Lvl: " + str(lvl))
print("Size: " + str(squareSize))

print("--- %s seconds ---" % (time.time() - start_time))