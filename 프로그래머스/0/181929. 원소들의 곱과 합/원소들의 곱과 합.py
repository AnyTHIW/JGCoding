def solution(num_list):
    answer1 = 1
    answer2 = 0
    
    for item in num_list:
        answer1 *= item
        answer2 += item
    
    return 1 if answer1 < answer2*answer2 else 0