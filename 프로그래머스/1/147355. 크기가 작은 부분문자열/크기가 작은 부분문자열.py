def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        slicedT = int(t[i:i+len(p)])
        if slicedT <= int(p):
            answer += 1
    
    return answer