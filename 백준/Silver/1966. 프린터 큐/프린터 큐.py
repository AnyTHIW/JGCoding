import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_TC_N = int(IFS().rstrip())
_N_AllDocNumber = []
_M_TargetDocOrder = []
_TC_Priority = []

for _ in range(_TC_N):
    n, m = list(map(int, IFS().split()))
    _N_AllDocNumber += [ n ]
    _M_TargetDocOrder += [ m ]
    allDocPriority = list(map(int, IFS().split()))
    _TC_Priority += [ [ (idx, item) for idx, item in enumerate(allDocPriority) ] ]
    
for i in range(_TC_N):
    n, mTargetIdx, queue = _N_AllDocNumber[i], _M_TargetDocOrder[i], _TC_Priority[i][:]
    priorityQueue = sorted(queue, key=lambda x:x[1], reverse=True)
    printingCount = 0
    
    while queue:
        readyDoc = queue.pop(0)
        
        if readyDoc[1] == priorityQueue[printingCount][1]:
            printingCount += 1
            
            if mTargetIdx == readyDoc[0]:
                print(printingCount)
                break
            
        else:
            queue.append(readyDoc)