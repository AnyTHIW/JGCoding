import sys

input = sys.stdin.readline

_N, _M = map(int, input().split())
_TreeList = list(map(int, input().split()))

heightMin = 0
heightMax = max(_TreeList)

l = heightMin
r = heightMax

tempHeight = 0

while l <= r:
    m = (l + r) // 2
    sumLog = sum(item - m for item in _TreeList if item > m)
        
    if sumLog >= _M:
        tempHeight = m
        l = m + 1

    elif sumLog < _M:
        r = m - 1
    
print(tempHeight)