import sys
import math

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
factoNumber = math.factorial(_N)

zeroCounter = 0
for char in str(factoNumber)[::-1]:
    if int(char) != 0:
        break
    zeroCounter += 1
    
print(zeroCounter)