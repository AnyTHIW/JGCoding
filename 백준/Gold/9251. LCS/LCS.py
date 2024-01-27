# lc Sub_sequence_ 최장공통부분 수 열(순서?)
def lcs(str1, str2):
    dp = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]
    
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                # 문자열 인덱스는 0부터 시작하므로 -1로 접근
                dp[i][j] = dp[i-1][j-1] + 1
                # dp2차원배열의 인덱스는 1부터 시작
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(str1)][len(str2)], dp

def print_dp(dp):
    for row in dp:
        print(row)

_String1 = input()
_String2 = input()

dpNum, dpT = lcs(_String1, _String2)

print(dpNum)
