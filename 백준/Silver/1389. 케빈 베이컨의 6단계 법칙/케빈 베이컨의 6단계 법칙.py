import sys

input = sys.stdin.readline
INF = float('inf')

N_, M_ = map(int, input().split())
relMap = [[0] * (N_ + 1)] + [[0] + [INF] * N_ for _ in range(N_)] # padding

for i in range(1, N_ + 1):
    relMap[i][i] = 0
    

for _ in range(M_):
    a, b = map(int, input().split())
    
    relMap[a][b] = 1
    relMap[b][a] = 1
    
for btw in range(1, N_+1):
    for stt in range(1, N_+1):
        for ed in range(1, N_+1):
            relMap[stt][ed] = min(relMap[stt][btw] + relMap[btw][ed], relMap[stt][ed])

# 결과 계산
result = []

for i in range(1, N_ + 1):
    total = sum(relMap[i])
    result.append((i, total))
    
print(min(result, key=lambda item: (item[1], item[0]))[0])