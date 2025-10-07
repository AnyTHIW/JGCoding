def solution(my_string):
    stk = list(my_string)
    answer = ''
    
    while stk:
        answer += stk.pop()    

    return answer