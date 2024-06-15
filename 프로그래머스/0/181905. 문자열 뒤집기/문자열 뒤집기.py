def solution(my_string, s, e):
    return F"{my_string[:s]}{my_string[s:e+1][::-1]}{my_string[e+1:]}"