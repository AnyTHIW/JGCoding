import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

N_, M_ = map(int, input().split())
relMap = [[0] * (N_ + 1)] + [[0] + [INF] * N_ for _ in range(N_)] # padding

for i in range(1, N_ + 1):
    relMap[i][i] = 0

for _ in range(M_):
    a, b = map(int, input().split())
    
    relMap[a][b] = 1
    relMap[b][a] = 1
    
def BFS(st):  
    vstMap = [False] * (N_+1)
    vstMap[st] = True

    Q = deque([st])
    shortestPath = 0
    while Q:
        curr = Q.popleft()
        for nxt in range(1, N_+1):    
            if not vstMap[nxt] and relMap[curr][nxt] == 1 :
                relMap[st][nxt] = relMap[st][curr] + 1
                vstMap[nxt] = True
                Q.append(nxt)
                
for i in range(1, N_ + 1):
    BFS(i)
    
min_bacon = INF
result = -1
    
for i in range(1, N_ + 1):
    bacon = sum(relMap[i])
    if bacon < min_bacon:
        min_bacon = bacon
        result = i

print(result)