#!/usr/bin/env python

import time
import string
import re
import sys
start_time = time.time()

def getSkyAsString(sky):
    skyAsString = ""
    for row in sky:
        skyAsString += ''.join(row)
        skyAsString += '\n'
    return skyAsString
        
with open("input3.txt") as f:
    lines = f.read().splitlines()
    xs = []
    ys = []
    velXs = []
    velYs = []

    for line in lines:
        x, y, velocityX, velocityY = re.compile(r'[-]?[0-9]+').findall(line)
        xs.append(int(x))
        ys.append(int(y))
        velXs.append(int(velocityX))
        velYs.append(int(velocityY))
        
    maxX = max(xs)
    minX = min(xs)
    maxY = max(ys)
    minY = min(ys)
    origMinX = minX
    origMinY = minY
    xRange = abs(maxX) + abs(minX)
    yRange = abs(maxY) + abs(minY)
    lastXRange = xRange
    lastYRange = yRange
    newXRange = 0
    newYRange = 0
    second = 0
    lower = 0
    higher = 0

    while((newXRange <= lastXRange) and (newYRange) <= lastYRange):
        second += 1
        lastXRange = abs(maxX) + abs(minX)
        lastYRange = abs(maxY) + abs(minY)
        newYs = []
        newXs = []
        for i in range(len(xs)):
            newY = ys[i] + velYs[i]*second
            newX = xs[i] + velXs[i]*second
            newYs.append(newY)
            newXs.append(newX)
        maxX = max(newXs)
        minX = min(newXs)
        maxY = max(newYs)
        minY = min(newYs)
        newXRange = abs(maxX) + abs(minX)
        newYRange = abs(maxY) + abs(minY)
        if ((newXRange < lastXRange) and (newYRange) < lastYRange):
            lower = second
        if ((newXRange <= lastXRange) and (newYRange) <= lastYRange):
            higher = second
        
    second = lower + ((higher - lower)/2)
    
    newYs = []
    newXs = []
    for i in range(len(xs)):
        newYs.append(ys[i] + velYs[i]*second)
        newXs.append(xs[i] + velXs[i]*second)
            
    maxX = max(newXs)
    minX = min(newXs)
    maxY = max(newYs)
    minY = min(newYs)
    #xRange = min(61, abs(maxX) + abs(minX))
    #yRange = min(9, abs(maxY) + abs(minY))
    xRange = abs(maxX) + abs(minX)
    yRange = abs(maxY) + abs(minY)
    
    
    for second in range(second-50, second+50):
        sky = [['.' for x in range(xRange+1)] for y in range(yRange+1)]
        for i in range(len(xs)):
            newY = ys[i] - minY + velYs[i]*second
            newX = xs[i] - minX + velXs[i]*second
            
            if ((newX <= xRange) and (newY <= yRange) and (newX >= 0) and (newY >= 0)):
                sky[newY][newX] = "#"
        
        sys.stdout.write("\nTime: %ds\n%s" % (second, getSkyAsString(sky)))
        time.sleep(0.5)
        sys.stdout.flush()

print("--- %s seconds ---" % (time.time() - start_time))