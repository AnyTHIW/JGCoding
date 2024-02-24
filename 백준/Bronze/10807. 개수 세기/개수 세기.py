import sys
IFS = sys.stdin.readline

_ = IFS()
_IntegerS = map(int, IFS().rstrip().split())
_V = int(IFS().rstrip())

count = 0
for item in _IntegerS:
    if _V==item : count += 1

print(count)