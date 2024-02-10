def solution(num_list):
    odd_string = ""
    even_string = ""
    
    for item in num_list:
        if item%2:
            odd_string += str(item)
        else:
            even_string += str(item)
            
    answer = int(odd_string) + int(even_string)
    
    return answer