import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_K = int(IFS().rstrip())
_NumberList = [ int(_.rstrip()) for _ in IFSs() ]
stack = list()

for i in range(_K):
    if _NumberList[i] == 0:
        stack.pop()
    else:
        stack.append(_NumberList[i])
    
if not stack:
    print(0)
else:
    print(sum(stack))