#!/usr/bin/env python

import time
start_time = time.time()
current_freq = 0
frequencies = []
doubleFound = False

with open("input.txt") as f:
    content = f.readlines()
    
    while(doubleFound == False):
        for i in range(0,len(content)):
            current_freq += int(content[i].strip())
            if (current_freq in frequencies):
                doubleFound = True
                print("First double: " + str(current_freq))
                break
            frequencies.append(current_freq)
print("--- %s seconds ---" % (time.time() - start_time))
