import sys
from collections import deque

input = sys.stdin.readline

N_, M_, B_ = map(int, input().split())

HeightMap_ = [ list(map(int, input().split())) for _ in range(N_)]
heightList = sorted(set([ _ for __ in HeightMap_ for _ in __]))

def test(minH, maxH):
    heightCount = { item:0 for item in range(heightList[0],heightList[-1]+1)}
    
    for lst in HeightMap_:
        for item in lst:
            heightCount[item] +=1
    
    timeToMakeHeight = {}
    
    for h in range(minH, maxH + 1):
        toFill = 0
        toCarve = 0

        for item in heightList:
            if item > h:
                toCarve += (item - h) * heightCount[item]
            elif item < h:
                toFill += (h - item) * heightCount[item]
        
        if toCarve + B_ < toFill:
            continue

        timeToMakeHeight[h] = toCarve * 2 + toFill * 1
        
    minTime = min(timeToMakeHeight.values())
    maxH_atMinTime = max(key for key, value in timeToMakeHeight.items() if value == minTime)
    print(F"{minTime} {maxH_atMinTime}")

if len(heightList) == 1:
    print(F"0 {heightList[0]}")
else:
    test(heightList[0], heightList[-1])
