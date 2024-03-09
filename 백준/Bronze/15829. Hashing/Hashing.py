import sys
IFS = sys.stdin.readline

_N = int(IFS().rstrip())
_String = [*IFS().rstrip()]

count = 0
toTargetNumber = 0

for item in _String:
    base = 31**count
    toIntNumber = ord(item) - ord('a') + 1
    toTargetNumber += toIntNumber * base
    
    count += 1
print(toTargetNumber)