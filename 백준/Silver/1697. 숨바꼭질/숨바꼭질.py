import sys
from collections import deque

input = sys.stdin.readline

_M, _K = map(int, input().split())

dX = [0, -1, 1]
dMul = 2

Q = deque()
Q.append(_M)
minTimeDct = {_M: 0}
tempTime = 0

while Q:
    tempPos = Q.popleft()
    
    if tempPos in minTimeDct:
        tempTime = minTimeDct[tempPos]
        
    if tempPos == _K:
        break
    
    for dir in dX:
        if dir == 0:
            newPos = tempPos * dMul
        else:
            newPos = tempPos + dir
            
        if 0 <= newPos <= 1000000:
            if newPos not in minTimeDct:
                minTimeDct[newPos] = tempTime + 1
                Q.append(newPos)
            
print(tempTime)