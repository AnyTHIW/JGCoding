import sys

input = sys.stdin.readline

_N, _M = map(int, input().split())
_TreeList = list(map(int, input().split()))

def BS_rec():
    l = 0
    r = max(_TreeList)
    
    def BS_rec_inner(l, r):
        if l > r:
            return r
        
        m = (l + r) // 2
        
        sumLog = 0
        for item in _TreeList:
            if m > item:
                continue
            
            sumLog += item - m
            if sumLog > _M:
                break
            
        if sumLog >= _M:
            return BS_rec_inner(m + 1, r)

        elif sumLog < _M:
            return BS_rec_inner(l, m - 1)
        
    return BS_rec_inner(l, r)
    
print(BS_rec())
    