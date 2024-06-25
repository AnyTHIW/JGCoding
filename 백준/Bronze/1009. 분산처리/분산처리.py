import sys 
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_T = int(IFS())
_CASE_SET = [line.rsplit() for line in IFSs()]

_Base_Example = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

for i in range(_T):
    baseA, exponentB = _CASE_SET[i]
    
    exponentRemainder = int(exponentB) % len(_Base_Example[int(baseA[-1])])
    
    print(_Base_Example[int(baseA[-1])][exponentRemainder - 1])