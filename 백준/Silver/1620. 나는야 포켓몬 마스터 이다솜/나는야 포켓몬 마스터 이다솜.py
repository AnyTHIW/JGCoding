import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N, _M = map(int, IFS().split())
_NameList = list()
_NameDict = dict()

for i in range(_N):
    name = IFS().rstrip()
    _NameList.append(name)
    _NameDict[name] = i + 1
    
for j in range(_M):
    x = IFS().rstrip()
    
    if x.isdigit():
        print(_NameList[int(x)-1])
    else:
        print(_NameDict[x])