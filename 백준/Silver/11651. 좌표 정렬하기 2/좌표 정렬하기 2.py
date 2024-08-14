import sys
import heapq

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_Dot_List = [list(map(int, _.split())) for _ in IFSs()]

heap = [(item[1], item[0]) for item in _Dot_List]
heapq.heapify(heap)

sortedList = []

while heap:
    y, x = heapq.heappop(heap)
    sortedList.append([x, y])

for dot in sortedList:
    print(*dot, sep=" ")
