_n = int(input())
  
def DP_topDown_Fib_withMemo(n):
    fib_result = [0]*(n+1)
    
    # for item in fib_result:
    #     item = 0;
    
    # fib_result[0] = 0
    fib_result[1] = 1

    return DP_topDown_Fib_withMemo_AUX(n, fib_result)

def DP_topDown_Fib_withMemo_AUX(n, result):
    if result[n] > 0:
        return result[n]
    else:
        #? 중요코드인가 ->yes 왜?
        # 
        if n < 0:
            return 0
        elif n == 0:
            return 0
    
    result[n] = (
        DP_topDown_Fib_withMemo_AUX(n-1, result)
        + DP_topDown_Fib_withMemo_AUX(n-2, result)
    )
    
    return result[n]

result_dp_TD = DP_topDown_Fib_withMemo(_n)

print(result_dp_TD)