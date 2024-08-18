import sys
import math

def thenes(stt:int, ed:int)->list:
    NumberList = [True] * (ed + 1)
    
    NumberList[0] = NumberList[1] = False
    
    for i in range(2, math.isqrt(ed)+1):
        if NumberList[i] == True:
            for j in range(i * i, ed + 1, i):
                NumberList[j] = False
    
    return [number for number in range(stt, ed+1) if NumberList[number]]

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines


_M, _N = map(int, IFS().split())

list = thenes(_M, _N)
print(*list, sep="\n")