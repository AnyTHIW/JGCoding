import sys
IFS = sys.stdin.readline

_A_UP, _B_DOWN, _V_M_TREE = map(int, IFS().split())

# print(_A_UP, _B_DOWN, _V_M_TREE)

interval = _A_UP-_B_DOWN

days = (_V_M_TREE - _B_DOWN) // interval

# print(days)

lastDays = 0 if (_V_M_TREE - _B_DOWN) % interval == 0 else  1
# _V-_A를 Interval로 올라가는 헛수고Days

print(days + lastDays)