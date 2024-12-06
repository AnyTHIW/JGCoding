import sys
import heapq

input = sys.stdin.readline

_N = int(input().rstrip())

tempHeap = []

for _ in range(_N):
    _X = int(input().rstrip())
    if _X == 0:
        if tempHeap:
            print(heapq.heappop(tempHeap))
        else:
            print(0)
    else:
        heapq.heappush(tempHeap, _X)