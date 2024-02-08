def solution(a, b, c):
    sum = a+b+c
    
    if a==b and b==c:
        return (3**3) * (a**(1+2+3))
    elif a==b or b==c or c==a:
        return sum * (sum**2 - a*(sum-a) - b*(sum-b) - c*(sum-c))
    
    return sum