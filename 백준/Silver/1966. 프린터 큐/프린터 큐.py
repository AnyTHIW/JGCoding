import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_TC_N = int(IFS().rstrip())
_N_AllDocNumber = []
_M_TargetDocOrder = []
_AllDocPriority = []

for i in range(_TC_N):
    numbers = list(map(int, IFS().split()))
    _N_AllDocNumber += [ numbers[0] ]
    _M_TargetDocOrder += [ numbers[1] ]
    _AllDocPriority.append(IFS().split())

for i in range(_TC_N):
    n, mTargetIdx, queue = _N_AllDocNumber[i], _M_TargetDocOrder[i], _AllDocPriority[i]
    priorityQueue = sorted(queue)
    printingCount = 0

    while queue:
        readyDoc = queue[0]
        
        if readyDoc == priorityQueue[-1]:
            printingCount += 1
            queue.pop(0)
            priorityQueue.pop()
            
            if mTargetIdx <= 0:
                print(printingCount)
                break

        else:
            queue.append(queue.pop(0))

        if mTargetIdx <= 0:
            mTargetIdx = len(queue) - 1
        else:
            mTargetIdx -= 1