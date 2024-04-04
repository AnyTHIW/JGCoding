import sys
IFS = sys.stdin.readline

_N = IFS().rstrip()
_N_String = IFS().rstrip()

result = sum(map(int, list(_N_String)))

print(result)