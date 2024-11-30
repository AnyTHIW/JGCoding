import sys

input = sys.stdin.readline
inputs = sys.stdin.readlines

_N, _M = map(int, input().split())
_seq = list(map(int, input().split()))

data = [list(map(int, _.split())) for _ in inputs()]

CumulSum = [0] * (_N + 1)

idx = 1
for numb in _seq:
    CumulSum[idx] += CumulSum[idx-1] + numb
    idx += 1

for i,j in data:
    print(CumulSum[j]-CumulSum[i-1])