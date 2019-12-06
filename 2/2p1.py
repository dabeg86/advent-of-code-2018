#!/usr/bin/env python

import time
start_time = time.time()
threesCount = 0
twosCount = 0
threesFound = False
twosFound = False

with open("input.txt") as f:
    boxIds = f.readlines()
    for boxId in boxIds:
        for uniqueChar in "".join(set(boxId.strip())):
            if (boxId.count(uniqueChar) == 2):
                twosFound = True
            elif (boxId.count(uniqueChar) == 3):
                threesFound = True
        if (twosFound == True):
            twosCount += 1
        if (threesFound == True):
            threesCount += 1

        #reset for next boxId
        twosFound = False
        threesFound = False

checksum = twosCount * threesCount
print("Checksum: " + str(twosCount) + "*" + str(threesCount) + "=" + str(checksum))
print("--- %s seconds ---" % (time.time() - start_time))
