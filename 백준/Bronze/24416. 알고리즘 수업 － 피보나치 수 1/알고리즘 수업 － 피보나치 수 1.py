import sys
IFS = sys.stdin.readline

_NUMBER = int(IFS().rstrip())

def FiboRecur(n):
    dp = [0, 1, 1]
    CntAsIdx = 3
    while (CntAsIdx <= n):
        dp.append(dp[CntAsIdx-1] + dp[CntAsIdx-2])
        CntAsIdx += 1
        
    return dp[CntAsIdx-1]

def FiboDynP(n):
    if n >= 3 :
        return n-2
    if n <= 2:
        return 0

print(FiboRecur(_NUMBER), FiboDynP(_NUMBER));