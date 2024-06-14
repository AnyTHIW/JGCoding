def solution(x):
    def sliceDigit(number):        
        if number == 0:
            return 0
        else:            
            return number % 10 + sliceDigit( number // 10 )
    
    digitSum = sliceDigit(x)
    
    if (x % digitSum == 0):
        answer = True
    else:
        answer = False
    
    return answer


    