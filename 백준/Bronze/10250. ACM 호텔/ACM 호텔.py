from math import remainder
import sys
IFS = sys.stdin.readline

_T_num = int(IFS().rstrip())
_T = []

_T = [[int(x) for x in IFS().rstrip().split()] for _ in range(_T_num)]
# print(_T)

def RoomNumber(testCase: list):
    _H, _W, _N = testCase
    
    remainder = _N%_H
    quote = _N//_H
    
    if remainder == 0:
        remainder = _H
    else:
        quote += 1
    
    level = remainder * 100
    number = quote
    
    roomNumber = level + number
    
    return roomNumber

for idx in range(_T_num) :
    result = RoomNumber(_T[idx])
    print(result)