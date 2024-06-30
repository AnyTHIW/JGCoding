import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N_DotCount = IFS().rstrip()
_Arr_DotInfo = [ {"x_i":int(_.rstrip().split()[0]), "y_i":int(_.rstrip().split()[1])} for _ in IFSs() ]

_Arr_DotInfo.sort(key=lambda x: (x["x_i"], x["y_i"]))

for elem in _Arr_DotInfo:
    print(elem["x_i"], elem["y_i"])