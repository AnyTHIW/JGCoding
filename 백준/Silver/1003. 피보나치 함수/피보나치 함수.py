import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_T = IFS().rstrip()
_N = [int(_.rstrip()) for _ in IFSs()]

def DP_up(idx):
    lst = [(1, 0) , (0, 1)]
    
    cnt = 2
    while cnt <= idx:
        lst.append( tuple(a+b for a, b in zip(lst[cnt-1], lst[cnt-2])) )
        cnt += 1
    
    return lst[idx]
    
def DP_down(idx):
    lst = [(1, 0) , (0, 1)] + [(-1, -1)] * max(0, idx - 1)
    
    def DP_down_inner(idx):
        if lst[idx] != (-1, -1):
            return lst[idx]
        
        lst[idx] = tuple(a+b for a, b in zip(DP_down_inner(idx-1), DP_down_inner(idx-2)))
        return lst[idx]
            
    return DP_down_inner(idx)

for tc in _N:
    # print(* DP_up(tc),sep=" ")
    print(* DP_down(tc),sep=" ")