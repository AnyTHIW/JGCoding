import sys
IFS = sys.stdin.readline

_A_NUMBER = IFS().rstrip()
_B_NUMBER = IFS().rstrip()

strLength = len(_A_NUMBER) + len(_B_NUMBER)

dp = list()
for i in range(len(_A_NUMBER)):
    dp.append( int(_A_NUMBER[i]) )
    dp.append( int(_B_NUMBER[i]) )

while len(dp) > 2:
    for i in  range(1, len(dp)):
        dp[i-1] = (dp[i-1] + dp[i])%10   
    dp.pop()
    
print(*dp, sep='')