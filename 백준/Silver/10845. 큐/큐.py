import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_COMMANDS = [ _.rstrip().split() for _ in IFSs() ]
Q = list()

for i in range(_N):
    arg_1 = _COMMANDS[i][0]
    
    if  arg_1 == "push":
        arg_2 = _COMMANDS[i][1]
        Q.append(arg_2)
        continue
    
    elif arg_1 == "pop":
        if len(Q) > 0:
            print(Q[0])
            del Q[0]
        else:
            print(-1)
        continue
    
    elif arg_1 == "size":
        print(len(Q))
        continue
        
    elif arg_1 == "empty":
        if len(Q) > 0:
            print(0)
        else:
            print(1)
        continue
    
    elif arg_1 == "front":
        if len(Q) <= 0:
            print(-1)
        else:
            print(Q[0])
        continue            
        
    elif arg_1 == "back":
        if len(Q) <= 0:
            print(-1)
        else:
            print(Q[len(Q)-1])
        continue

    else:
        print("error")
    