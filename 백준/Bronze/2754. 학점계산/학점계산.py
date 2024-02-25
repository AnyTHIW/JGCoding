import sys
IFS = sys.stdin.readline

_CLang_score = (IFS().rstrip())
_cLang_avrgVal  = [*_CLang_score]
_cLang_numValue = []

if _cLang_avrgVal[0] == 'A':
    _cLang_numValue += [4]
elif _cLang_avrgVal[0] == 'B':
    _cLang_numValue += [3]
elif _cLang_avrgVal[0] == 'C':
    _cLang_numValue += [2]
elif _cLang_avrgVal[0] == 'D':
   _cLang_numValue += [1]
else:
    _cLang_numValue += [0]

if len(_cLang_avrgVal) != 1:
    if _cLang_avrgVal[1] == '+':
        _cLang_numValue += [.3]
    elif _cLang_avrgVal[1] == '-':
        _cLang_numValue += [-.3]
    elif _cLang_avrgVal[1] == '0':
        _cLang_numValue += [.0]
else:
    _cLang_numValue[0] = 0.0
    
print(sum(_cLang_numValue))