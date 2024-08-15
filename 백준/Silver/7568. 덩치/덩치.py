import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N =int(IFS().rstrip())
_Human_List = [ [idx] + list(map(int, _.split())) + [1] for idx, _ in enumerate(IFSs()) ]

_Human_List.sort(key=lambda x: x[1])

for i in range(_N):
    for j in range(i, _N):
        if i == j:
            continue
        
        if _Human_List[i][1] < _Human_List[j][1] and _Human_List[i][2] < _Human_List[j][2]:
            _Human_List[i][3] += 1

_Human_List.sort(key=lambda x: x[0])

for i in range(_N):
    print(_Human_List[i][3])
            