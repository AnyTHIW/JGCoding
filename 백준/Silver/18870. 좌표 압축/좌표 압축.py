import sys

input = sys.stdin.readline

_N = int(input().rstrip())
_Xi_List = list(map(int, input().split()))

sortedList = sorted(_Xi_List)
dct = {}

notDuplicatedIdx = 0
for item in sortedList:
    if item in dct:
        notDuplicatedIdx -= 1
    else:
        dct[item] = notDuplicatedIdx
        
    notDuplicatedIdx += 1
    
for item in _Xi_List:
    print(dct[item])