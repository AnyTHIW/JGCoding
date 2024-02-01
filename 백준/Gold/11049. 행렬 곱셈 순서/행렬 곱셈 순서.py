# 행렬 곱셈 순서

import sys
I_F_S = sys.stdin.readline

_N = int(I_F_S())
_Size_matrix = [list(map(int, I_F_S().rstrip().split())) for _ in range(_N)]

# print(_Size_matrix)
Dp_count = [[0]*_N for _ in range(_N)]

# 행렬곱은 두 부분행렬의 곱으로 볼 수 있다. X = XiXjXk....Xz 일 때, X = XaXb (Xa = XiXj....Xa, Xb = Xa+1....Xz)
for step in range(1, _N):
# i는 부분 행렬의 크기를 결정 (1일경우 Xa의 크기가 1, 즉 바깥 for문은 구간행렬앞부분 Xa를 나타낸다)
    for i in range(_N - step):
        end = i + step
        # j는 i로 인한 잘린 나머지 부분 행렬의 크기 (Xb의 크기, 안 for문은 구간행렬뒷부분 Xb를 나타낸다)
        if step == 1:
            Dp_count[i][end] = _Size_matrix[i][0] * _Size_matrix[end][0] * _Size_matrix[end][1]
            continue
        
        Dp_count[i][end] = float('inf')
        
        for k in range(i, end):
            Dp_count[i][end] = min(Dp_count[i][end], Dp_count[i][k] + Dp_count[k + 1][end] + _Size_matrix[i][0] * _Size_matrix[k][1] * _Size_matrix[end][1])

print(Dp_count[0][- 1])