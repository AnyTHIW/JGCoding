import sys
import queue

input = sys.stdin.readline
inputs = sys.stdin.readlines

_T = int(input().rstrip())

dY = [1, -1, 0, 0]
dX = [0, 0, -1, 1]

def BFS(mtx: list[list[dict]], start: dict):
    Q = queue.Queue()
    Q.put(start)
    start["visit"] = True
    
    while not Q.empty():
        temp = Q.get()
        for i in range(4):
            ny, nx = dY[i] + temp["position"][1], dX[i] + temp["position"][0]
                
            if 0 <= ny < len(mtx) and 0 <= nx < len(mtx[0]) and not mtx[ny][nx]["visit"] and mtx[ny][nx]["cabbage"]:
                mtx[ny][nx]["visit"] = True
                Q.put(mtx[ny][nx])

def CheckWormNumber(m:int, n:int, k:int):
    fieldMatrix = [[{"position":(idxX,idxY), "visit":False, "cabbage":False} for idxX in range(_M_width)] for idxY in range(_N_height)]

    for _ in range(k):
        width, height = map(int, input().split())
        fieldMatrix[height][width]["cabbage"] = True

    wormSum = 0

    for row in fieldMatrix:
        for item in row:
            if item["visit"] or not item["cabbage"]:
                continue
            
            BFS(fieldMatrix, item)
            wormSum += 1
            
    print(wormSum)

for _ in range(_T):
    _M_width, _N_height, _K_cabbageNumber = map(int, input().split())
    CheckWormNumber(_M_width, _N_height, _K_cabbageNumber)