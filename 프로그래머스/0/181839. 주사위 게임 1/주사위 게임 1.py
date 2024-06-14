def solution(a, b):
    answer = 0

    if not(a%2 or b%2):
        answer = abs(a - b)
    elif (a%2) and (b%2):
        answer = pow(a, 2) + pow(b, 2)
    else:
        answer = 2*(a+b)
        
    return answer