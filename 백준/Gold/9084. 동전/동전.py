import sys
INPUT_FROM_SYS = sys.stdin.readline  # 불필요한 주석 처리

_T = int(input())
_N = [-1] * (_T+1)
_COIN_TYPE = [[] for _ in range(_T + 1)]
_COIN_TYPE[0] = [-1]
_M = [-1] * (_T+1)

for i in range(1,_T+1):
    _N[i] = int(input())
    _COIN_TYPE[i].append(list(map(int, INPUT_FROM_SYS().split())))
    _M[i] = int(input())

def count_ways(coin_type, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for item in coin_type:
        for j in range(item, amount + 1):
            # item의 값어치를 가지는 amount 부터, 구해야 할 amout+1까지의 amount에 관한 amount값 j를 
            dp[j] += dp[j - item]
    
    return dp[amount]

for i in range(1, _T+1):  # 각 테스트 케이스에 대해
    print(count_ways(_COIN_TYPE[i][0], _M[i]))  # 결과 출력