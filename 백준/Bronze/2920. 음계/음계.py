import sys
IFS = sys.stdin.readline

_Numbers = IFS().rstrip().split()
ascending = list("12345678")
descending = list("87654321")
result = [0] * len(_Numbers)

if _Numbers == ascending:
    print("ascending")
elif _Numbers == descending:
    print("descending")
else:
    print("mixed")