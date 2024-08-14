import sys
import random

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_Dot_List = [list(map(int, _.split())) for _ in IFSs()]

def RQSort(Arr:list, LIdx:int, RIdx:int ):
    if LIdx < RIdx:
        CIdx = RPartition(Arr, LIdx, RIdx)
        RQSort(Arr, LIdx, CIdx-1)
        RQSort(Arr, CIdx+1, RIdx)
        
def RPartition(Arr:list, LIdx:int, RIdx:int):
    ranIdx = random.randint(LIdx, RIdx)
    Arr[RIdx], Arr[ranIdx] = Arr[ranIdx], Arr[RIdx]
    
    x = Arr[RIdx]
    pivot_1 = LIdx - 1
    
    for pivot_2 in range(LIdx, RIdx):
        if Arr[pivot_2][1] < x[1] or (Arr[pivot_2][1] == x[1] and Arr[pivot_2][0] < x[0]):
            pivot_1 += 1
            Arr[pivot_2], Arr[pivot_1] = Arr[pivot_1], Arr[pivot_2]
    
    Arr[RIdx], Arr[pivot_1 + 1] = Arr[pivot_1 + 1], Arr[RIdx]
    return pivot_1+1

RQSort(_Dot_List, 0, len(_Dot_List)-1)

for dot in _Dot_List:
    print(*dot, sep=" ")