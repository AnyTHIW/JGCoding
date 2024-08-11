import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_T = int(IFS().rstrip())
_PS_STRING = [ _.rstrip() for _ in IFSs() ]

def CheckVPS(string: str):
    stk = []
    
    for char in string:
        if char == "(":
            stk.append(char)
        elif char == ")":
            if stk:
                stk.pop()
            else:
                print("NO")
                return
        else:
            print("error")
            return
        
    if not stk:
        print("YES")
    else:
        print("NO")

for string in _PS_STRING:
    CheckVPS(string)