import heapq, sys

input = sys.stdin.readline

_N = int(input().rstrip())
_XList = [ int(input().rstrip()) for _ in range(_N) ]

heapQ = []

for item in _XList:
    if item == 0:
        if heapQ:
            print(str(heapq.heappop(heapQ)).lstrip("-"))
        else:
            print(0)
    else:
        heapq.heappush(heapQ, -item)