import sys
IFS = sys.stdin.readline

_N, _M = map(int, IFS().split())
_LESSON_INFO = [int(x) for x in IFS().split()]

""" set binary points """
cd_size_start = max(_LESSON_INFO)
cd_size_end = sum(_LESSON_INFO)


while cd_size_start <= cd_size_end:
    cd_size_mid = (cd_size_start + cd_size_end) // 2
    
    lssn_time_temp = 0
    cd_number_cnt = 1
    
    for t in _LESSON_INFO:
        if lssn_time_temp + t > cd_size_mid:
            cd_number_cnt += 1
            lssn_time_temp = 0
            
        lssn_time_temp += t
    
    if cd_number_cnt <= _M:
        answer = cd_size_mid
        cd_size_end = cd_size_mid - 1
    else:
        cd_size_start = cd_size_mid + 1

print(answer)