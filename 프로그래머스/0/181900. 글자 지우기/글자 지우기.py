def solution(my_string, indices):
    for val in indices:
        my_string = my_string[:val] +" "+ my_string[val+1:]
        
    return my_string.replace(" ", "")