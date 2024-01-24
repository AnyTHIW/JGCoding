import sys
INPUTS_FROM_SYS = sys.stdin.readlines
sys.setrecursionlimit(10**9)
maindata_preT = list(map(int, INPUTS_FROM_SYS()))

def postT(st, ed):
    if st>ed:
        return
    
    root = maindata_preT[st]
    p = st + 1
    while p <= ed and maindata_preT[p] < root:
        p += 1
        
    postT(st+1, p-1)
    postT(p,ed)
    
    print(root)
    
postT(0, len(maindata_preT)-1)