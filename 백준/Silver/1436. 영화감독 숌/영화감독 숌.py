import sys

IFS = sys.stdin.readline

_N = int(IFS().rstrip())
count = 0
targetNumber = 0

while _N > count:
    targetNumber += 1
    
    if "666" in str(targetNumber):
        count += 1    
        
print(targetNumber)