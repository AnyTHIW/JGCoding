import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_Card_List = list(map(str, IFS().split()))
_Card_Set = dict.fromkeys(_Card_List, 0)
_M = int(IFS().rstrip())
_Test_CardNumber = list(map(str, IFS().split()))

for cardIdx in range(_N):
    _Card_Set[_Card_List[cardIdx]] += 1

result = [0] * _M

for testIdx in range(_M):
    if  _Test_CardNumber[testIdx] in _Card_Set.keys():
        result[testIdx] = _Card_Set[_Test_CardNumber[testIdx]]

print(*result, sep=" ")