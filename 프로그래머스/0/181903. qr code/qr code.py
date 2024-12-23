def solution(q, r, code):
    answer = ''
    
    for idx, char in enumerate(code):
        if (idx % q == r):
            answer += char
    
    return answer