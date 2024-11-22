import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_T = int(IFS().rstrip())
_n = [ int(_.rstrip()) for _ in IFSs() ]

def DP_upward_print():
    result = DP_upward(max(_n))
    
    for item in _n:
        print(result[item])
        
def DP_upward(number: int) -> list[int]:
    sumMethod = [0, 1, 2, 4] + [0] * max(0, number-3)
    
    if number > 3:
        cnt = 4
        while (cnt <= number):
            sumMethod[cnt] = sumMethod[cnt-1] + sumMethod[cnt-2] + sumMethod[cnt-3]
        
            cnt += 1
        
    return sumMethod

def DP_downward_print():
    rsortedN = sorted(_n, reverse=True)
    
    result = DP_downward(rsortedN)
        
    for item in _n:
        print(result[item])
    
def DP_downward(lst: list) -> dict[int, int]:
    sumMethod = {0:0, 1:1, 2:2, 3:4}
    
    def DP_downward_inner(number: int) -> int:
        
        if number in sumMethod:
            return sumMethod[number]
        
        sumMethod[number] = DP_downward_inner(number-3) + DP_downward_inner(number-2) + DP_downward_inner(number-1)
        
        return sumMethod[number]
    
    for item in lst:
        DP_downward_inner(item)
        
    return sumMethod

# DP_upward_print()
DP_downward_print()
