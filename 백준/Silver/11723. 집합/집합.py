import sys

AllSet = (1 << 21) - 1
EmptySet = 0

def Add(Bit, num):
    return Bit | (1 << num)
        
def Remove(Bit, num):
    return Bit & ~(1 << num)
        
def Check(Bit, num):
    print(1 if Bit & (1 << num) else 0)
    
def Toggle(Bit, num):
    return Bit ^ (1 << num)

def All():
    return AllSet

def Empty():
    return EmptySet
    
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_M = int(IFS().rstrip())
BitMaskedSet = 0

for i in range(_M):
    command = IFS().split()
    cmdString = command[0]
    
    if cmdString == "add":
        x = int(command[1])
        BitMaskedSet = Add(BitMaskedSet,x)
            
    elif cmdString == "remove":
        x = int(command[1])
        BitMaskedSet = Remove(BitMaskedSet,x)
            
    elif cmdString == "check":
        x = int(command[1])
        Check(BitMaskedSet,x)
            
    elif cmdString == "toggle":
        x = int(command[1])
        BitMaskedSet =Toggle(BitMaskedSet,x)
            
    elif cmdString == "all":
        BitMaskedSet = All()
        
    elif cmdString == "empty":
        BitMaskedSet = Empty()
        
    else:
        print("Error")