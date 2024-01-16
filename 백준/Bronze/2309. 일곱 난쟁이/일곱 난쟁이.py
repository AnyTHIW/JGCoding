# 여러 라인을 입력받아야 할 경우
import sys
_inputElements = list(map(int, [sys.stdin.readline().strip() for _ in range(9)]))

_smallMenHeight = sorted(_inputElements)

_9heightSum = 0

# 9 난쟁이 키 합
for i in _smallMenHeight:
    _9heightSum += i
    
_suspiciousHeightSum = _9heightSum - 100

_suspect1Index = 0
_suspect2Index = 0

def aaaa():
    for index1 in range(0, len(_smallMenHeight)):
        for index2 in range(index1 + 1, len(_smallMenHeight)):
            if  _suspiciousHeightSum == _smallMenHeight[index1] + _smallMenHeight[index2]:
                return index1, index2
    return ;
        
# 하나는 앞에서 접근하고, 하나는 본인 제외하고 인덱스로 선택 (조합)
# 다 담아서 9height에서 빼보면 금방 나올텐데 구현이 잘 안되네
_suspect1Index, _suspect2Index = aaaa()

for i in range(len(_smallMenHeight)):
    if i == _suspect1Index or i == _suspect2Index:
        continue
    else:
        print(_smallMenHeight[i])


            
            