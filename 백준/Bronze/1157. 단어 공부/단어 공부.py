import sys
IFS = sys.stdin.readline

_OneWord = IFS().rstrip().upper()
_charSet = list(set(_OneWord))
_charCount = [0] * len(_charSet)

for idx, item in enumerate(_charSet):
    _charCount[idx] = _OneWord.count(item)
    
if _charCount.count(max(_charCount)) > 1:
    print("?")
else :
    max_index = _charCount.index(max(_charCount))
    print(_charSet[max_index])