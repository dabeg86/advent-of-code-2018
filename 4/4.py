#!/usr/bin/env python

import time
from datetime import datetime
import operator
start_time = time.time()
guardMinutes = {}
guardSleepTimes = {}
guardMaxMinutes = {}
guardSumSleep = {}
currentGuardId = 0
minuteFallAsleep = 0
minuteWakeUp = 0

def getTimeFromString(input):
    return input[input.find("[")+1:input.find("]")].strip()
    
def getMinuteFromString(input):
    return int(input[input.find(":")+1:input.find("]")].strip())

def getHourFromString(input):
    return int(input[input.find(":")-2:input.find(":")].strip())
    
def getGuardId(input):
    return int(input[input.find("#")+1:input.find("begins")].strip())

with open("input.txt") as f:
    sortedRecords = sorted(f.read().splitlines(), key=lambda x: datetime.strptime(getTimeFromString(x), '%Y-%m-%d %H:%M'))
    for record in sortedRecords:
        if "Guard" in record:
            currentGuardId = getGuardId(record)
            if currentGuardId not in guardMinutes:
                guardMinutes[currentGuardId] = {}
        elif "falls asleep" in record:
            minuteFallAsleep = getMinuteFromString(record)
        elif "wakes up" in record:
            minuteWakeUp = getMinuteFromString(record)
            for minute in range(minuteFallAsleep, minuteWakeUp):
                if guardMinutes[currentGuardId].has_key(minute):
                    guardMinutes[currentGuardId][minute] += 1
                else:
                    guardMinutes[currentGuardId][minute] = 1
                    
    for guardId in guardMinutes:
        d = guardMinutes[guardId]
        if d:
            maxMinute = max(d, key=d.get)
            guardSumSleep[guardId] = sum(d.values())
            guardSleepTimes[guardId] = maxMinute
            guardMaxMinutes[guardId] = d[maxMinute]
    guardAsleepMost = max(guardSumSleep.items(), key=operator.itemgetter(1))[0]
    print("part1: " + str(guardAsleepMost*guardSleepTimes[guardAsleepMost]))
    guardAsleepSameMinuteMost = max(guardMaxMinutes.items(), key=operator.itemgetter(1))[0]
    minuteAsleepMost = guardSleepTimes[guardAsleepSameMinuteMost]
    print("part2: " + str(guardAsleepSameMinuteMost*minuteAsleepMost))
            
print("--- %s seconds ---" % (time.time() - start_time))