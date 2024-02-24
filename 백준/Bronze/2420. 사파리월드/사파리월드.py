import sys
IFS = sys.stdin.readline

_N, _M = map(int, IFS().rstrip().split())
print(abs(_N-_M))