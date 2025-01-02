import sys

input = sys.stdin.readline

_n = int(input().rstrip())
squares = [i**2 for i in range(2, int(_n**0.5)+1)]

def DP_iter(n):
    memo_arr = [0,1,2,3] + [4] * max(_n-3, 0)
    
    for sq in squares:
        memo_arr[sq] = 1
    
    if n <= 3:
        return memo_arr[n]
        
    idx = 4
    while (idx <= n):
        if idx in squares:
            idx += 1
            continue
        
        for sq in reversed(squares):
            if sq > idx:
                continue
            
            memo_arr[idx] = min(memo_arr[idx], memo_arr[idx-sq] + 1)
            
            if memo_arr[idx] == 2:
                break
            
        idx += 1
    
    return memo_arr[n]

def DP_recur(n):
    memo_dict = {1:1, 2:2, 3:3}
    
    if n in squares:
        return 1
    
    for sq in squares:
        memo_dict[sq] = 1

    def DP_recur_inner(n):
        if n in memo_dict:
            return memo_dict[n]
        
        minValue = 4        
        for sq in reversed(squares):
            if sq > n:
                continue
            
            minValue = min(minValue, DP_recur_inner(n-sq) + 1)
            
            memo_dict[n] = minValue
            
            if memo_dict[n] == 2:
                return memo_dict[n]
    
        return memo_dict[n]
    
    return DP_recur_inner(n)

# print(DP_iter(_n))
print(DP_recur(_n))