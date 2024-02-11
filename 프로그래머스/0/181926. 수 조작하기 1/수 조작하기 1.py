def solution(n, control):
    for character in control:
        if character == "w":
            n += 1
        elif character == "s":
            n -= 1
        elif character == "d":
            n += 10
        elif character == "a":
            n -= 10
    
    return n