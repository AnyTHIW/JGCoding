import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_K, _N = map(int, IFS().split())
_List_LAN_Wire = [ int(_) for _ in IFSs() ]

def BS(left, right):
    if left > right:
        return right
    
    mid = (left+right) // 2
    targetN = sum(item // mid for item in _List_LAN_Wire)
    
    if targetN >= _N:
        return BS(mid+1, right)
    else:
        return BS(left, mid-1)

start, end = 1, max(_List_LAN_Wire)
print(BS(start, end))