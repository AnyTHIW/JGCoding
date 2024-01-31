import sys

I_F_S = sys.stdin.readline

_NofA = int(I_F_S().rstrip())
_A_List = list(map(int, I_F_S().rstrip().split()))

# print(_NofA, _A_List)

dpTable = [1]*_NofA

for i in range(1, _NofA):
    for j in range(i):
        if _A_List[j] < _A_List[i]:
            dpTable[i] = max(dpTable[i], dpTable[j]+1)
        
# print(prev_A)
print(max(dpTable))