import sys
IFS = sys.stdin.readline

_n = int(IFS().rstrip())
_String = list(IFS().rstrip())

flag = False
hiddenNumber = ''
hiddenSum = 0
for i in range(_n):
    # False and 문자일 때 : skip
    # False and 숫자 일 때 : True, 받음
    # True and 문자일 때 : False, 여태 받은거 int로 변환 (6자리를 넘지 않는다)후
    #                               히든넘버들의 합 += 히든 넘버
    # True and 숫자 일 때 : 계속 받음 (6자리를 넘지 않는다)
    if flag == False:
        if ord('0') <= ord(_String[i]) <= ord('9'):
            hiddenNumber += _String[i]
            flag = True
            continue
        else:
            continue
            
    if flag == True:
        if ord('0') <= ord(_String[i]) <= ord('9'):
            hiddenNumber += _String[i]
            continue
        else:
            hiddenSum += int(hiddenNumber)
            hiddenNumber = ''
            flag = False
            continue

if (hiddenNumber != ''):
    hiddenSum += int(hiddenNumber)
                
print(hiddenSum)