#!/usr/bin/env python

import time
import itertools
start_time = time.time()

def match(s1, s2):
    pos = -1

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i

    return pos

with open("input.txt") as f:
    boxIds = f.readlines()
    for a, b in itertools.combinations(boxIds, 2):
        result = match(a, b)
        if(result != -1):
            print("BoxId1: " + a.strip())
            print("BoxId2: " + b.strip())
            print("Result: " + a[:result].strip() + a[result+1:].strip())
            break
        
print("--- %s seconds ---" % (time.time() - start_time))
