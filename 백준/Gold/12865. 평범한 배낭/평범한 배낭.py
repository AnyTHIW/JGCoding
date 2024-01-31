# 평범한 배낭
import sys
I_F_S = sys.stdin.readline

_N, _K = map(int, I_F_S().split())

item_info = [[0,0]]
# index가 'weight' 'value'가 되게 자료구조를 짤 수 없을까?

for _ in range(_N):
    item_weight, item_value = map(int, I_F_S().rstrip().split())
    item_info.append([item_weight, item_value])
    # [0]이 무게, [1]이 가치

# dp_value = [0] * (_K + 1)
dp_value = [[0] * (_K + 1) for _ in range(_N+1)]
# 다이나믹 프로그래밍을 위한 2차원 배열 초기화 (index: 무게 제한, value: 가치)

# 제한은 weight, 목표는 value
# for curr_weight, curr_value in item_info:
    # 현재 item의 무게와 가치 추출
for i in range(1, _N+1):
    
    # for i in range(curr_weight, _K+1):
    for j in range(1,_K+1):
        # dp_value[i] = max(dp_value[i], dp_value[i - curr_weight] + curr_value)
        curr_weight, curr_value = item_info[i][0], item_info[i][1]
        
        if j < curr_weight:
            dp_value[i][j] = dp_value[i-1][j]
        else:
            dp_value[i][j] = max(dp_value[i-1][j], dp_value[i-1][j-curr_weight] + curr_value)
    
print(dp_value[_N][_K])