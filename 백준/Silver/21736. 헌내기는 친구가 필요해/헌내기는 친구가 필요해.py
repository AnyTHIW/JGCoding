import sys
from collections import deque

input = sys.stdin.readline

N_, M_ = map(int, input().split())
CampusMap_ = [input().rstrip() for _ in range(N_)]
    
def BFS():
    dY, dX = [1, -1, 0, 0], [0, 0, -1, 1]
    Q = deque()
    
    for yIdx, string in enumerate(CampusMap_):
        if "I" in string:
            xIdx = string.index("I")
            Q.append((xIdx, yIdx))
            break
            
    vst = [[False]*M_ for _ in range(N_)]
    vst[yIdx][xIdx] = True
    
    person = 0
    
    while len(Q):
        currX, currY = Q.popleft()
    
        for idx in range(4):
            newXPos, newYPos = currX + dX[idx], currY + dY[idx]
            if 0 <= newXPos < M_ and 0 <= newYPos < N_ and not vst[newYPos][newXPos]:
                vst[newYPos][newXPos] = True
                search = CampusMap_[newYPos][newXPos]
                
                if search == "X":
                    continue

                if search == "P":
                    person += 1
                    
                Q.append((newXPos, newYPos))
                    
    return print(person) if person != 0 else print("TT")

BFS()