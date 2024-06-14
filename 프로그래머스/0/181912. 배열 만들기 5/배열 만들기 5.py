def solution(intStrs, k, s, l):
    answer = []
    
    answer = [int(item[s:s+l]) for item in intStrs if int(item[s:s+l]) > k]
    
    print(answer)
    
    return answer