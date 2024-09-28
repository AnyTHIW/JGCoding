import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_WithdrawTime = list(map(int, IFS().split()))

_WithdrawTime.sort(reverse=True)

sum = 0

for idx, time in enumerate(_WithdrawTime):
    sum += (idx+1)*time
    
print(sum)