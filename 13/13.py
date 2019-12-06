#!/usr/bin/env python

import sys
import time
import string
import collections
import operator
from enum import Enum
start_time = time.time()

def findIndexesOfCharInString(string, char):
    return [i for i, letter in enumerate(string) if letter == char]
    
class Direction(Enum):
    LEFT = 1
    STRAIGHT = 2
    RIGHT = 3

class Cart:
    def __init__(self, x, y, currDir):
        self.X = x
        self.Y = y
        self.NextTurnDir = Direction.LEFT
        self.CurrentDir = currDir
        
    def __str__(self):
        return "Cart(X=%s,Y=%s,NextTurnDir=%s,CurrentDir=%s)"%(self.X, self.Y, self.NextTurnDir, self.CurrentDir) 

    def getX(self):
        return self.X

    def getY(self):
        return self.Y
        
    def getNextTurnDir(self):
        return self.NextTurnDir

    def getCurrDir(self):
        return self.CurrentDir

        
def getReferenceTrack(lines):
    referenceTrack = []
    for line in lines:
        line = ''.join(line)
        line = line.replace('v', '|').replace('^', '|').replace('>', '-').replace('<', '-')
        referenceTrack.append(line)
    return referenceTrack

def findAllCartsOnRow(trackRow):
    cartSymbols = ['v', '^', '<', '>']
    indexes = {}
    for cartSymbol in cartSymbols:
        indexes.extend(findIndexesOfCharInString(trackRow, cartSymbol))
    return indexes

with open("input2.txt") as f:
    trackRows = f.read().splitlines()
    referenceTrack = getReferenceTrack(trackRows)
    cartPositions = {}
    tick = 0
    i = 1
    for yCoord, trackRow in enumerate(trackRows):
        cartXCoords = findAllCartsOnRow(trackRow)
        for cartXCoord in cartXCoords:
            cartPositions[i] = Cart(cartXCoord, yCoord)
            i += 1
    for k, v in cartPositions.items():
        print(str(k) + ": " + str(v))
    collisionDetected = False
    #while(collisionDetected == False):
    #    tick += 1
        
    for cart in (sorted(cartPositions.values(), key=operator.attrgetter('X'))):
        print(str(cart))
        
    for refTrackRow in referenceTrack:
        print(refTrackRow)
    
print("--- %s seconds ---" % (time.time() - start_time))