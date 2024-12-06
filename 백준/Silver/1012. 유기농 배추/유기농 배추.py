import sys
import queue

input = sys.stdin.readline
inputs = sys.stdin.readlines

_T = int(input().rstrip())

dY = [1, -1, 0, 0]
dX = [0, 0, -1, 1]

def BFS(adj:dict, startKey:tuple, m, n):
    Q = queue.Queue()
    adj[startKey]["visit"] = True
    Q.put(startKey)
    
    while not Q.empty():
        tempKey = Q.get()
        
        for i in range(4):
            ny, nx = dY[i] + tempKey[1], dX[i] + tempKey[0]
            adjKey = (nx, ny)
            
            if 0 <= ny < n and 0 <= nx < m and (adjKey in adj) and not adj[adjKey]["visit"]:
                adj[adjKey]["visit"] = True
                
                Q.put(adjKey)

def CheckWormNumber(m:int, n:int, k:int):
    AdjList = {}

    for _ in range(k):
        width, height = map(int, input().split())
        AdjList[(width, height)] = {"visit":False}

    wormSum = 0
    for itemKey in AdjList:
        if AdjList[itemKey]["visit"]:
            continue

        BFS(AdjList, itemKey, m, n)
        wormSum += 1
            
    print(wormSum)

for _ in range(_T):
    _M_width, _N_height, _K_cabbageNumber = map(int, input().split())
    CheckWormNumber(_M_width, _N_height, _K_cabbageNumber)
