#!/usr/bin/env python

import time
import re
start_time = time.time()
xs = []
ys = []
xRange = []
yRange = []
fabric = []
numberOfX = 0

def pretty_print(fabric):
    for row in fabric:
        print(''.join(row))

def getXAndY(claimId):
    return claimId[claimId.find("@")+1:claimId.find(":")].strip().split(',')
        
def getX(claimId):
    return int(getXAndY(claimId)[0])
    
def getY(claimId):
    return int(getXAndY(claimId)[1])
    
def getXAndYRange(claimId):
    return claimId[claimId.find(":")+1:].strip().split('x')
    
def getXRange(claimId):
    return int(getXAndYRange(claimId)[0])

def getYRange(claimId):
    return int(getXAndYRange(claimId)[1])

with open("input.txt") as f:
    claimIds = f.read().splitlines()
    for claimId in claimIds:
        xRange.append(getXRange(claimId))
        yRange.append(getYRange(claimId))
        xs.append(getX(claimId))
        ys.append(getY(claimId))
    
    fabric = [[0 for x in range(len(xs))] for y in range(len(ys))]
    for i in range(len(claimIds)):
        for xr in range(xs[i], xs[i] + xRange[i]):
            for yr in range(ys[i], ys[i] + yRange[i]):
                if fabric[yr][xr] == 0:
                    fabric[yr][xr] = i+1
                elif fabric[yr][xr] != -1:
                    fabric[yr][xr] = -1
                    numberOfX += 1

    #y, x
    print("Number of Xs: " + str(numberOfX))
    
    for i in range(len(claimIds)):
        claimDoesNotOverlap = True
        for xr in range(xs[i], xs[i] + xRange[i]):
            for yr in range(ys[i], ys[i] + yRange[i]):
                if fabric[yr][xr] == -1:
                    claimDoesNotOverlap = False
        if claimDoesNotOverlap:
            print("Does not overlap: " + str(i+1))
            
print("--- %s seconds ---" % (time.time() - start_time))