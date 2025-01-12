import sys
from collections import deque

input = sys.stdin.readline

N_, M_ = map(int, input().split())
CampusMap_ = [input().rstrip() for _ in range(N_)]
    
def BFS():
    dY, dX = [1, -1, 0, 0], [0, 0, -1, 1]
    Q = deque()
    
    xIdx = 0
    yIdx = 0
    breaker = False
    for string in CampusMap_:
        for char in string:
            if char == "I":
                breaker = True
                break
            xIdx += 1
            
        if (breaker):
            break
        xIdx = 0
        yIdx += 1
    
    vst = {}
    person = 0
    Q.append((xIdx, yIdx))
    vst[(xIdx, yIdx)] = True
    
    while len(Q):
        tempPos = Q.popleft()
    
        for idx in range(4):
            newXPos, newYPos = tempPos[0] + dX[idx], tempPos[1] + dY[idx]
            if 0 <= newXPos < M_ and 0 <= newYPos < N_ and not (newXPos, newYPos) in vst:
                search = CampusMap_[newYPos][newXPos]
                if search == "X":
                    continue

                if search == "P":
                    person += 1
                    
                elif search == "O":
                    pass
                
                vst[(newXPos, newYPos)] = True
                Q.append((newXPos, newYPos))
                    
    return print(person) if person != 0 else print("TT")

BFS()