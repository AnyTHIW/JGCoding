def solution(my_string, index_list):
    
    answer = ''
    
    for number in index_list:
        answer += my_string[number]
    
    return answer