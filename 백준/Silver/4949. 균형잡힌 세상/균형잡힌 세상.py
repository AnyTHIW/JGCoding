import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_StringList = [ _.rstrip() for _ in IFSs() ]

for string in _StringList:
    stack = list()
    result = "yes"
    
    if string == ".":
        break
    
    for char in string:
        if char == ".":
            if stack:
                result = "no"
            break

        if char == "[" or char =="(":
            stack.append(char)
            
        elif char == "]":
            if not stack or stack.pop() != "[":
                result = "no"
                break
            
        elif  char == ")":
            if not stack or stack.pop() != "(":
                result = "no"
                break
            
    print(result)