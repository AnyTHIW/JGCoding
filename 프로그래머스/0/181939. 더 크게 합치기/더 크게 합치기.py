def solution(a, b):
    result1 = int(str(a)+str(b))
    result2 = int(str(b)+str(a))
    if result1 > result2: return result1
    else : return result2
