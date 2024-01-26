import sys
INPUT_FROM_SYS = sys.stdin.readline
INPUTS_FROM_SYS = sys.stdin.readlines

_N, _K = map(int, INPUT_FROM_SYS().split())

_A_value = [ int(INPUT_FROM_SYS().strip()) for _ in range(_N)]

count_coins = 0

# for item in reversed(_A_value):
for i in range(len(_A_value)-1, -1, -1):
    count_item = _K // _A_value[i]
    _K = _K % _A_value[i]
    count_coins += count_item
    
print(count_coins)