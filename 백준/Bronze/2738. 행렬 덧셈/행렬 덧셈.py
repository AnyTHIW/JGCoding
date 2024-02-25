import sys
IFS = sys.stdin.readline

_N, _M, = map(int, IFS().rstrip().split())

_A_item = [list(map(int, IFS().split())) for _ in range(_N)]
_B_item = [list(map(int, IFS().split())) for _ in range(_N)]
_sum_AB = [[ _A_item[i][j] + _B_item[i][j] for j in range(_M)] for i in range(_N)]

for i in range(_N):
    print(*(_sum_AB[i]))