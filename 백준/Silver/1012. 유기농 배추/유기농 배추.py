import sys
import queue

input = sys.stdin.readline
inputs = sys.stdin.readlines

_T = int(input().rstrip())

dY = [1, -1, 0, 0]
dX = [0, 0, -1, 1]

def BFS(dct:dict, startKey:tuple, m, n):
    Q = queue.Queue()
    dct[startKey] = True
    Q.put(startKey)
    
    while not Q.empty():
        tempKey = Q.get()
        
        for i in range(4):
            ny, nx = dY[i] + tempKey[1], dX[i] + tempKey[0]
            adjKey = (nx, ny)
            
            if 0 <= ny < n and 0 <= nx < m and (adjKey in dct) and not dct[adjKey]:
                dct[adjKey] = True
                
                Q.put(adjKey)

def CheckWormNumber(m:int, n:int, k:int):
    CabbageVisitDict = {}

    for _ in range(k):
        width, height = map(int, input().split())
        CabbageVisitDict[(width, height)] = False

    wormSum = 0
    for itemKey in CabbageVisitDict:
        if CabbageVisitDict[itemKey]:
            continue

        BFS(CabbageVisitDict, itemKey, m, n)
        wormSum += 1
            
    print(wormSum)

for _ in range(_T):
    _M_width, _N_height, _K_cabbageNumber = map(int, input().split())
    CheckWormNumber(_M_width, _N_height, _K_cabbageNumber)
