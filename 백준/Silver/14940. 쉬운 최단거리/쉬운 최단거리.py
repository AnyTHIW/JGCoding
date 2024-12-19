import sys
from collections import deque

input = sys.stdin.readline
inputs = sys.stdin.readlines

_n_Y, _m_X = map(int, input().split())

_map = [list(map(int, line.split())) for line in inputs()]

def SearchTarget(lst: list) -> tuple:
    for yIdx, row in enumerate(lst):
        for xIdx, item in enumerate(row):
            if item == 2:
                return (xIdx, yIdx)   # 좌표는 (x, y) 형식을 따라 (열 순서, 행 순서)로 표기, 0-based
    return (-1, -1)

target = SearchTarget(_map)

deltaY = [1, -1, 0, 0]
deltaX = [0, 0, -1, 1]

def BFS(map:list, target) -> list:
    distanceMap = [[-1 for _ in range(_m_X)] for _ in range(_n_Y)]
    
    Q = deque([target])
    distanceMap[target[1]][target[0]] = 0
    
    while Q:
        temp = Q.popleft()
        distance = distanceMap[temp[1]][temp[0]]
        for i in range(4):
            newX, newY = temp[0] + deltaX[i], temp[1] + deltaY[i]
            
            if 0 <= newX < _m_X and 0 <= newY < _n_Y and distanceMap[newY][newX] == -1:
                if map[newY][newX] == 0:
                    distanceMap[newY][newX] = 0
                else:    
                    distanceMap[newY][newX] = distance + 1
                    Q.append((newX, newY))
    
    for j in range(_n_Y):
        for i in range(_m_X):
            if map[j][i] == 0:
                distanceMap[j][i] = 0
    
    return distanceMap

for row in BFS(_map,target):
    print(*[F"{item}" for item in row], sep=" ")