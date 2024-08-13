import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines
_T = int(IFS().rstrip())
_TEST_CASE = []

def Collect(floor:int, ho:int)->int:
    sum = 0
    if memo[floor][ho] != -1:
        return memo[floor][ho]
    
    if floor <= 0:
        memo[floor][ho] = ho
    else:
        for i in range(1, ho+1):
            sum += Collect(floor-1, i)
        memo[floor][ho] = sum
        
    return memo[floor][ho]

for i in range(_T):
    _TEST_CASE += [[ int(IFS().rstrip()) for _ in range(2) ]]
    memo = [[-1] * (_TEST_CASE[i][1] + 1) for _ in range(_TEST_CASE[i][0]+1)]
    x = Collect(_TEST_CASE[i][0], _TEST_CASE[i][1])
    print(x)
