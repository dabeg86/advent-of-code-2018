#!/usr/bin/env python

import time
import string
import collections
start_time = time.time()
#generations = 20
generations = 1500#50000000000
state = ""
indexZero = 0
currSum = 0
prevSum = 0
diffs = []

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def getInitialState(line):
    return line[line.find(":")+1:].strip()
    
def getCurrSum(state, indexZero):
    total = 0
    for idx in find(state, "#"):
        total += (idx-indexZero)
    return total
    
def fillSidesWithEmptyPots(state, indexZero):
    if(state[0] == "#"):
        indexZero += 3
        state = "..." + state
    elif(state[1] == "#"):
        indexZero += 2
        state = ".." + state
    elif(state[2] == "#"):
        indexZero += 1
        state = "." + state
    
    if(state[-1] == "#"):
        state = state + "...."
    elif(state[-2] == "#"):
        state = state + "..."
    elif(state[-3] == "#"):
        state = state + ".."
    return state, indexZero
        
with open("input.txt") as f:
    lines = f.read().splitlines()
    state += getInitialState(lines[0])
    state, indexZero = fillSidesWithEmptyPots(state, indexZero)
    rules = {}
    
    for line in lines[2:]:
        lhs, rhs = line.split(" => ")
        rules[lhs] = rhs
        
    #print("0: " + state)
    prevSum = getCurrSum(state, indexZero)
    for generation in range(1, generations+1):
        state, indexZero = fillSidesWithEmptyPots(state, indexZero)
        newState = ['.' for i in range(len(state))]
        for i in range(2, len(state)-2):
            key = state[i-2:i+3]
            if(key in rules.keys()):
                newState[i] = rules[key]
        state = ''.join(newState)
        currSum = getCurrSum(newState, indexZero)
        if(generation == 20):
            print("Part1: " + str(currSum))
        diffs.append(currSum-prevSum)
        if(len(diffs) > 100): diffs.pop(0)
        prevSum = currSum
        #print(str(generation) + ": " + state)
    #print(getCurrSum(state, indexZero))
    last100diff = sum(diffs) // len(diffs)
    #print(last100diff)
    total = (50000000000 - generation) * last100diff + getCurrSum(state, indexZero)
    print("Part2: " + str(total))
    
print("--- %s seconds ---" % (time.time() - start_time))