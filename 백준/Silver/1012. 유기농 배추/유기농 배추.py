import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
inputs = sys.stdin.readlines

_T = int(input().rstrip())

dY = [1, -1, 0, 0]
dX = [0, 0, -1, 1]

def DFS_visit(dct:dict, ky:tuple, m, n):
    dct[ky] = True
    
    for i in range(4):
        ny, nx = dY[i] + ky[1], dX[i] + ky[0]
        adjKey = (nx, ny)
            
        if 0 <= ny < n and 0 <= nx < m and (adjKey in dct) and not dct[adjKey]:
            DFS_visit(dct, adjKey, m, n)

def DFS(dct:dict, m, n) -> int:
    wormSum = 0
    
    for ky in dct:
        if not dct[ky]:
            DFS_visit(dct, ky, m, n)
            wormSum += 1
            
    return wormSum
            
def CheckWormNumber(m:int, n:int, k:int):
    CabbageVisitDict = {}

    for _ in range(k):
        width, height = map(int, input().split())
        CabbageVisitDict[(width, height)] = False

    result = DFS(CabbageVisitDict, m, n)
            
    print(result)

for _ in range(_T):
    _M_width, _N_height, _K_cabbageNumber = map(int, input().split())
    CheckWormNumber(_M_width, _N_height, _K_cabbageNumber)
