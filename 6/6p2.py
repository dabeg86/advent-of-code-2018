#!/usr/bin/env python

import time
import string
start_time = time.time()

def minimumValues(some_dict):
    positions = [] # output variable
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = [] # output variable
            positions.append(k)

    return positions

def pretty_print(lines):
    for line in lines:
        print(''.join(line))

def getXCoord(xAndY):
    return int(xAndY.split(',')[0].strip())

def getYCoord(xAndY):
    return int(xAndY.split(',')[1].strip())
    
def isCoordNearEnough(dictOfCoord, x, y, maxDistance):
    distances = {}
    for k, coordinate in dictOfCoord.items():
        q1 = getXCoord(coordinate)
        q2 = getYCoord(coordinate)
        distances[k] = getManhattanDistance(q1, q2, x, y)
    
    if(sum(distances.values()) < maxDistance):
        return True
    else:
        return False

def getManhattanDistance(p1, p2, q1, q2):
    return abs(p1-q1) + abs(p2-q2)
    
def getSizeOfNearestRegion(grid, maxX, maxY):
    sizeDict = {}
    
    for x in range(0, maxX):
        for y in range(0, maxY):
            elem = grid[y][x]
            if (elem != '.'):
                if (sizeDict.has_key(elem)):
                    sizeDict[elem] += 1
                else:
                    sizeDict[elem] = 1
    
    return sizeDict['#']

with open("input.txt") as f:
    coordinates = f.read().splitlines()
    maxX = max([getXCoord(coordinate) for coordinate in coordinates])+2
    maxY = max([getYCoord(coordinate) for coordinate in coordinates])+1
    
    grid = [['.' for x in range(maxX)] for y in range(maxY)]
    dictOfCoord = {}
    
    for idx, coordinate in enumerate(coordinates):
        grid[getYCoord(coordinate)][getXCoord(coordinate)] = chr(65 + idx)
        dictOfCoord[chr(65 + idx)] = coordinate
   
    for x in range(0, maxX):
        for y in range(0, maxY):
            if(isCoordNearEnough(dictOfCoord, x, y, 10000)):
                grid[y][x] = "#"
            
    print(getSizeOfNearestRegion(grid, maxX, maxY))
    
print("--- %s seconds ---" % (time.time() - start_time))