def solution(nums):
    answer = 0
    
    st = set(nums)
    N = len(nums)
    
    if N//2 <= len(st):
        answer = N//2
    else:
        answer = len(st)
    
    return answer