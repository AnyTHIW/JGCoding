_N = int(input())

# memoization을 사용하여 부분 해결책을 저장할 memo 배열 초기화
memo = [0] * max(3, _N + 1)
memo[1], memo[2] = 1, 2  # 초기값 설정

# 동적 계획법을 사용하여 부분 해결책을 계산하고 memo 배열에 저장
for i in range(3, _N + 1):
    memo[i] = (memo[i - 1] + memo[i - 2]) % 15746

# 결과 출력
print(memo[_N])