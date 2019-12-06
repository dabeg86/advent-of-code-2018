#!/usr/bin/env python

import time
import string
start_time = time.time()

def isSameCharWithDifferentCase(c1, c2):
    if(c1 != c2 and (c1.upper() == c2 or c1.lower() == c2)):
        return True
    else:
        return False

def reactPolymer(polymer):
    listPolymer = list(polymer)
    for i in range(0, len(listPolymer)-1):
        firstChar = listPolymer[i]
        secondChar = listPolymer[i+1]
        if (isSameCharWithDifferentCase(firstChar, secondChar)):
            listPolymer[i] = ''
            listPolymer[i+1] = ''
    return ''.join(listPolymer)

with open("input.txt") as f:
    polymers = f.read().splitlines()
    original_polymer = polymers[0]
    lowercaseLetters = list(string.ascii_lowercase)
    for letter in lowercaseLetters:
        polymer = original_polymer.replace(letter, "").replace(letter.upper(), "")
        new_polymer = ""
        reactionWasDetected = True
        while(reactionWasDetected):
            new_polymer = reactPolymer(polymer)
            if (new_polymer == polymer):
                reactionWasDetected = False
            else:
                polymer = new_polymer
                
        print("Units: " + str(len(polymer)) + ", Letter: " + letter)
        
print("--- %s seconds ---" % (time.time() - start_time))