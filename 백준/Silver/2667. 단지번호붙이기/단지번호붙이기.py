import sys
from collections import deque

input = sys.stdin.readline
inputs = sys.stdin.readlines

N_ = int(input().rstrip())
listN_ = [[int(_)  for _ in line.rstrip()] for line in inputs()]

vst = [[False for _ in range(N_)] for _ in range(N_)]

result = []
cntComplex = 0

def BFS(startX, startY):
  # 상하좌우
  dY = [1, -1, 0, 0]
  dX = [0, 0, 1, -1]

  Q = deque([(startX, startY)])
  vst[startX][startY] = True
  cntBuilding = 1

  while Q:
    currX, currY= Q.popleft()

    for i in range(4):
      nextX, nextY = currX + dX[i], currY + dY[i]

      if 0 <= nextX < N_ and 0 <= nextY < N_ and listN_[nextX][nextY] == 1 and not vst[nextX][nextY]:
        nextPos = (nextX, nextY)

        vst[nextX][nextY] = True
        cntBuilding += 1
        Q.append(nextPos)

  result.append(cntBuilding)

for i in range(N_):
  for j in range(N_):
    if listN_[i][j] == 1 and not vst[i][j]:
      cntComplex += 1
      BFS(i, j)

print(cntComplex)
print(*sorted(result), sep='\n')