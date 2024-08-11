import sys
from tabnanny import check

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_T = int(IFS().rstrip())
_PS_STRING = [ _.rstrip() for _ in IFSs() ]

checkNumber = 0

def CheckVPS(string: str):
    checkNumber = 0
    
    for char in string:
        if checkNumber < 0:
            break
        if char == "(":
            checkNumber += 1
        elif char == ")":
            checkNumber -= 1
        else:
            print("error")
            
    if checkNumber == 0:
        print("YES")
    else:
        print("NO")

for string in _PS_STRING:
    CheckVPS(string)