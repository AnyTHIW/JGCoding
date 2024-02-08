def solution(code):
    ret = []
    mode = False
    
    for index, char in enumerate(code):
        if char == '1':
            mode = not mode
            continue
        
        if mode == False and index % 2 == 0:
            ret.append(char)
        elif mode == True and index % 2 == 1:
            ret.append(char)
        
    if len(ret) == 0:
        return "EMPTY"
            
    return ''.join(map(str, ret))