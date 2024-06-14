def solution(my_string, queries):
    
    for q in queries:
        my_string = F"{my_string[:q[0]]}{''.join(reversed(my_string[q[0]:q[1]+1]))}{my_string[q[1]+1:]}"
    
    return my_string