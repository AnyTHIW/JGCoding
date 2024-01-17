def binarySearch(start_index, end_index, targetNumber):
    # 예외구간
    if start_index > end_index:
        return 0
    
    middle_index = (start_index + end_index) // 2
    
    # 탐색구간
    if targetNumber < _domain[middle_index]:
        return binarySearch(start_index, middle_index-1, targetNumber)
    elif targetNumber == _domain[middle_index]:
        return 1
    else:
        return binarySearch(middle_index + 1, end_index , targetNumber)
    
# 여러 라인을 입력받아야 할 경우
import sys
# _n = int(input())
input()
# _nList = sys.stdin.readline()
# _domain = [_nList.split().strip() for _ in range(_n)]
_domain = list(map(int, sys.stdin.readline().split()))
_domain.sort()

# _m = int(input())
input()
# _mList = sys.stdin.readline()
# _numbersToFind = [ _mList.split().strip() for _ in range(_m)]
_numbersToFind = list(map(int, sys.stdin.readline().split()))

for item in _numbersToFind:
    print(binarySearch(0, len(_domain)-1, item))