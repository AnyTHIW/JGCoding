import sys
from collections import deque

input = sys.stdin.readline
inputs = sys.stdin.readlines

_m_row, _n_column = map(int,input().split())

# _tomato = [list(map(int, row.split())) for row in inputs()]
_tomato = [[int(item) for item in row.split()] for row in inputs()]

def BFS(box:list):
    dY, dX = [1, -1, 0, 0], [0, 0, -1, 1]    # 상하좌우
    dateMtx = [[-1 for _ in range(_m_row)] for _ in range(_n_column)]
    
    Q = deque()
    
    for yIdx in range(_n_column):
        for xIdx in range(_m_row):
            if box[yIdx][xIdx] == 1:
                dateMtx[yIdx][xIdx] = 0
                Q.append((xIdx, yIdx))
                
    while Q:
        currX, currY = Q.popleft()
        date = dateMtx[currY][currX]
        
        for i in range(4):
            newX, newY  = currX + dX[i], currY + dY[i]
            
            if 0 <= newX < _m_row and 0 <= newY < _n_column:
                if dateMtx[newY][newX] == -1 and box[newY][newX] == 0:
                    dateMtx[newY][newX] = date + 1
                    box[newY][newX] = 1
                    Q.append((newX, newY))
        
    for yIdx in range(_n_column):
        for xIdx in range(_m_row):
            if box[yIdx][xIdx] == 0:
                return -1
    
    return date

print(BFS(_tomato))