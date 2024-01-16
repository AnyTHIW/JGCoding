_number = int(input())

def loadFactorial(number: int):

    # 결과 반환
    if number >= 1:
        return number*loadFactorial(number-1)
    else :
        return 1
    
# n의 값으로 함수 실 시행, 출력
print(loadFactorial(_number))