import sys

input = sys.stdin.readline

_n = int(input().rstrip())

memo_arr = [0, 1, 3]
def DP_iter(n):
    if n <= 2:
        return memo_arr[n]
        
    idx = 3
    while (idx <= n):
        memo_arr.append(memo_arr[idx-1] + 2*memo_arr[idx-2])
        idx += 1
    
    return memo_arr[-1]

memo_recur = {1:1, 2:3}
def DP_recur(n):
    if n in memo_recur:
        return memo_recur[n]
    
    memo_recur[n] = DP_recur(n-1) + 2 * DP_recur(n-2)
    return memo_recur[n]

# print(DP_iter(_n)%10007)
print(DP_recur(_n)%10007)