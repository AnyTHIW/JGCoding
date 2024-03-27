import sys

IFS = sys.stdin.readline

_N = int(IFS().rstrip())

for i in range(_N):
    str = "*" * (_N - i)
    print(str)