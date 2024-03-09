import sys
IFS = sys.stdin.readline
_M = 1234567891

_N = int(IFS().rstrip())
_String = [*IFS().rstrip()]


# print(_N, _String, sep="  ")

count = 0
toTargetNumber = 0

for item in _String:
    base = 31**count
    toIntNumber = ord(item) - ord('a') + 1
    toTargetNumber += toIntNumber * base
    
    # print('==========')
    # print(base)
    # print(ord(item))
    # print(ord('a'))
    # print(toIntNumber)
    # print(toTargetNumber)
    
    count += 1
# print(toTargetNumber)

toTargetNumber = toTargetNumber % _M

print(toTargetNumber)