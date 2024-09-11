import sys

def Add(Group:set, num:int):
    if not num in Group:
        Group.add(num)
        
def Remove(Group:set, num:int):
    if num in Group:
        Group.remove(num)
        
def Check(Group:set, num:int):
    if num in Group:
        print("1")
    else:
        print("0")
    
def Toggle(Group:set, num:int):
    if num in Group:
        Group.remove(num)
    else:
        Group.add(num)

def All() -> set:
    return set(range(1,21))

def Empty() -> set:
    return set()
    
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_M = int(IFS().rstrip())
# _CommandList = [ _.split() for _ in IFSs() ]
S = set()

for i in range(_M):
    command = IFS().split()
    cmdString = command[0]
    
    if cmdString == "add":
        x = int(command[1])
        Add(S,x)
            
    elif cmdString == "remove":
        x = int(command[1])
        Remove(S,x)
            
    elif cmdString == "check":
        x = int(command[1])
        Check(S,x)
            
    elif cmdString == "toggle":
        x = int(command[1])
        Toggle(S,x)
            
    elif cmdString == "all":
        S = All()
        
    elif cmdString == "empty":
        S = Empty()
        
    else:
        print("Error")