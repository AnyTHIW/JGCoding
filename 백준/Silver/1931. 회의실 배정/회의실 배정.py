import sys
# import
I_F_S = sys.stdin.readline

_N = int(I_F_S())
maindata_time = [[0]*2 for _ in range(_N)]
# 시작, 끝 시간 가지는 회의리스트

for i in range(_N):
    maindata_time[i][0], maindata_time[i][1] = map(int, I_F_S().split())

maindata_time.sort(key = lambda x: [x[1], x[0]])
# lambda arguments: expression
# 배열을 반환해서 키로 삼음

fin_time = maindata_time[0][1]
# 가장 빠른 회의 끝나는 시간 지정
count = 1
# 첫 회의 미리 카운트

for i in range(1, _N):
    if maindata_time[i][0] >= fin_time:
        # 시작시간이 끝나는 시간보다 더 클때
        # 오름차순 정렬 되어있으므로, 끝나는 시간보다 더 큰 값들 중 가장 작은 값
        count += 1
        fin_time = maindata_time[i][1]

print(count)