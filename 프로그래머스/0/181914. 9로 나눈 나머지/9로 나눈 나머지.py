def solution(number):
    answer = 0
    digitSum = 0
    
    digitSum = sum(map(int, number))
    answer = digitSum % 9
    
    return answer