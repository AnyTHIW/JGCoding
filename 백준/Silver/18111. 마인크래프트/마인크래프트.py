import sys
from collections import deque

input = sys.stdin.readline

N_, M_, B_ = map(int, input().split())

HeightMap_ = [ list(map(int, input().split())) for _ in range(N_)]
heightList = sorted(set([ _ for __ in HeightMap_ for _ in __]))

def InvestigateHeight():
    for lst in HeightMap_:
        for item in lst:
            heightCount[item] +=1

def test():
    InvestigateHeight()
    
    timeToMakeHeight = {item: -1 for item in heightCount}
    
    for h in timeToMakeHeight:
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
    minTime = min(value for value in timeToMakeHeight.values() if value != -1)
    maxH_atMinTime = max([key for key, value in timeToMakeHeight.items() if value == minTime])
    print(F"{minTime} {maxH_atMinTime}")

if len(heightList) == 1:
    print(F"0 {heightList[0]}")
else:
    heightCount = { item:0 for item in range(heightList[0],heightList[-1]+1)}
    test()