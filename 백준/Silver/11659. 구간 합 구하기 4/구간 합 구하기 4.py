import sys

input = sys.stdin.readline
inputs = sys.stdin.readlines

_N, _M = map(int, input().split())
_seq = list(map(int, input().split()))

CumulSum = [0]

for numb in _seq:
    CumulSum.append(CumulSum[-1] + numb)

for _ in range(_M):
    i,j = map(int, input().split())
    print(CumulSum[j]-CumulSum[i-1])