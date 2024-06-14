def solution(my_strings, parts):
    answer = []
    
    for idx, item in enumerate(my_strings):
        s, e = parts[idx]
        answer.append(item[s:e+1])
        
    return ''.join(answer)