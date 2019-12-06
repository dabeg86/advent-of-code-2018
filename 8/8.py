#!/usr/bin/env python

import time
import string
start_time = time.time()

with open("input.txt") as f:
    tree = map(int, f.read().splitlines()[0].split(' '))
    ptr = 0
    headers = []
    metadatas = []
    headers.append(tree[ptr:ptr+2])
    ptr += 2
    currNode = 'A'
    nodeLib = {}

    while (ptr < len(tree)):
        if(headers[-1][0] == 0):
            nc = headers[-1][1]
            metadatas.append(tree[ptr:ptr+nc])
            ptr += nc
            headers.pop()
            if(len(headers) > 0):
                headers[-1][0] -= 1
        else:
            headers.append(tree[ptr:ptr+2])
            #print("Append: " + str(tree[ptr:ptr+2]))
            ptr += 2
        
        #print("Headers: " + str(headers))
        #print("metadata: " + str(metadata))
        #print("Ptr: " + str(ptr))

    res = 0
    for metadata in metadatas:
        res += sum(metadata)
    print(metadatas)
    print "Part 1: " + str(res)
    
print("--- %s seconds ---" % (time.time() - start_time))
