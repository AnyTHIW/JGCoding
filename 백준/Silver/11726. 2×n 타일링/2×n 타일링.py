import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
inputs = sys.stdin.readlines

_n = int(input().rstrip())

def tilingDownward(numb: int) -> int:
    dct = {1:1, 2:2}
    
    def tilingDownward_inner(numb: int) -> int:
        if numb in dct:
            return dct[numb]
        
        dct[numb] = tilingDownward_inner(numb-1) + tilingDownward_inner(numb-2)
        return dct[numb]
    
    tilingDownward_inner(numb)
    return dct[numb]

print(tilingDownward(_n)%10007)