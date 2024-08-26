import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_K, _N = map(int, IFS().split())
_List_LAN_Wire = [ int(_) for _ in IFSs() ]

_List_LAN_Wire.sort()
start, end = 1, max(_List_LAN_Wire)

while start <= end:
    mid = (start + end) // 2
    targetN = 0
    for item in _List_LAN_Wire:
        targetN += item // mid
    
    if targetN >= _N:
        start = mid + 1
    else:
        end = mid - 1

print(end)