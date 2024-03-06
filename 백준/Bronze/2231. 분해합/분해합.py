import sys
IFS = sys.stdin.readline

_N = int(IFS().rstrip())

constructor = 0

for x in range(1, _N+1):
    digitNumber = sum([int(_) for _ in list(str(x))])
    if  _N == digitNumber + x :
        constructor = x
        break

print(constructor)