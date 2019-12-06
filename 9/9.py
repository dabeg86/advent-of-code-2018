#!/usr/bin/env python

import time
import collections
start_time = time.time()

lastMarble = 71307*100
numberOfPlayers = 439
currentMarble = 1
playerScore = {}
circle = collections.deque()
circle.append(0)

for player in range(1, numberOfPlayers+1):
    playerScore[player] = 0

while(currentMarble < lastMarble):
    for player in range(1, numberOfPlayers+1):
        if ((currentMarble % 23) == 0):
            playerScore[player] += currentMarble
            circle.rotate(7)
            val = circle.popleft()
            playerScore[player] += val
        else:
            if(circle.count > 1):
                circle.rotate(-2)
            circle.appendleft(currentMarble)
        currentMarble += 1
        if (currentMarble > lastMarble):
            break

print(max(playerScore.values()))
