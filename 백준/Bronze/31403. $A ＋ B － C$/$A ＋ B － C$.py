import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_A, _B, _C = map(int, IFSs())

print(_A+_B-_C)
print(int(str(_A)+str(_B))-_C)