import sys
IFS = sys.stdin.readline

_T = int(IFS().rstrip())
_Strings = [IFS().rstrip() for _ in range(_T)]

print(*( item[0] + item[-1] for item in _Strings ), sep="\n")