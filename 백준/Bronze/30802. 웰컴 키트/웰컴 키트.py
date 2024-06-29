#  사람은 23명
#  티셔츠 신청 사이즈 목록은 [3, 1, 4, 1, 5, 9]
#  티셔츠 묶음단위는 기본 5, 펜 묶음 단위는 기본 7

# 티셔츠 묶음 수
# 펜 묶음 수, 펜 개별 수

import sys
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N_Applicant = int(IFS().rstrip())
_Arr_TShirtCount_BySize = list(map(int, IFS().split()))
_T_TShirtUnit, _P_PenUnit = map(int, IFS().split())

TMinimum, PMaximum, PIndividual = 0,0,0

for TSizeCount in _Arr_TShirtCount_BySize:
    UnitNumber = TSizeCount // _T_TShirtUnit
    
    if TSizeCount % _T_TShirtUnit != 0:
        UnitNumber += 1
    
    TMinimum += UnitNumber

print(TMinimum)

PMaximum = _N_Applicant // _P_PenUnit
PIndividual = _N_Applicant % _P_PenUnit

print(PMaximum, PIndividual)