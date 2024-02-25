import sys
IFS = sys.stdin.readline

_Strings = IFS().rstrip()
_modified_strings = [x.upper() if x.islower() else x.lower() for x in _Strings ]

print(*_modified_strings, sep="")