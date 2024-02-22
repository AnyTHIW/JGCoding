def solution(n):
    arr = [n]
    while (n != 1):
        if n%2: n = n*3+1
        else: n //= 2
        arr += [n]
    return arr