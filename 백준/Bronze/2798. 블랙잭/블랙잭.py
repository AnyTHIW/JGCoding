import sys
from itertools import combinations

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N, _M = map(int, IFS().split())
_CardValue_Array = list(map(int, IFS().split()))
_CardValue_Array.sort(reverse=True)

# print(_N, _M)
# print(_CardValue_Array)

max_sum = 0

for set in combinations(_CardValue_Array, 3):
    setSum = sum(set)
    
    if setSum <= _M and setSum > max_sum:
        max_sum = setSum

print(max_sum)