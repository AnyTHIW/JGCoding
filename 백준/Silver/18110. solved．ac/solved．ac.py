import sys
import math

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_n = int(IFS().rstrip())
_LevelList = [ int(_) for _ in IFSs() ]

_LevelList.sort()
excludedNumber = math.floor(_n * 0.15 + 0.5)
if excludedNumber != 0:
    newLevelList = _LevelList[excludedNumber:-excludedNumber]
else:
    newLevelList = _LevelList

sumTrimmedLevel = 0

for lvl in newLevelList:
    sumTrimmedLevel += lvl

if sumTrimmedLevel != 0:
    sumTrimmedLevel = math.floor(sumTrimmedLevel / (_n - excludedNumber*2) + 0.5)

print(sumTrimmedLevel)