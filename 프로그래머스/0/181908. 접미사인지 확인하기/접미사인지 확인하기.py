def solution(my_string, is_suffix):
    answer = 0
    thisSuffix = []
    
    for i in range(len(my_string)):
        thisSuffix.append(my_string[i:])
        
    for item in thisSuffix:
        if item == is_suffix:
            answer = 1

    return answer