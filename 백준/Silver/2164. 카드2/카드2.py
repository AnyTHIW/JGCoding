import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

def Procedure(queue: list, idx: int):
    idx += 1
    # del queue[0]
    queue.append(queue[idx])
    idx += 1
    return idx

_N = int(IFS().rstrip())
Q = list(range(1, _N+1))
currIdx = 0

for i in range(_N-1):
    currIdx = Procedure(Q, currIdx)
    
print(Q[currIdx])