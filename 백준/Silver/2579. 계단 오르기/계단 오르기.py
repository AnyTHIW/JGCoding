import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_stairNumber = int(IFS().rstrip())
_stairValue = [0] + [ int(_.rstrip()) for _ in IFSs() ]

def DP_upward():
    stairValueSum = list(_stairValue)
    
    if _stairNumber >= 2:
        stairValueSum[2] = _stairValue[1] + _stairValue[2]
    
    for i in range(3, _stairNumber+1):
        stairValueSum[i] = max(stairValueSum[i-3] + _stairValue[i-1], stairValueSum[i-2]) + _stairValue[i]
    
    return print(stairValueSum[-1])
        
def DP_downward():
    stairValueSum = {0:0, 1:_stairValue[1]}
    
    if _stairNumber >= 2:
        stairValueSum[2] = _stairValue[1] + _stairValue[2]
        
    def DP_downward_inner(step) -> int:
        
        if step in stairValueSum:
            return stairValueSum[step]
        
        stairValueSum[step] = max(DP_downward_inner(step-2), DP_downward_inner(step-3) + _stairValue[step-1]) + _stairValue[step]

        return stairValueSum[step]
    
    return print(DP_downward_inner(_stairNumber))

DP_upward()
# DP_downward()