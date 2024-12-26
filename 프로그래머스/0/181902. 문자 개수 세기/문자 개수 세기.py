def solution(my_string):
    answer = [0] * 52
    
    for char in my_string:
        charNumb = ord(char)
        if 65 <= charNumb <= 90:
            answer[ord(char)-65] += 1
        elif 97 <= charNumb <= 122:
            answer[ord(char)-(65+7-1)] += 1
    
    return answer