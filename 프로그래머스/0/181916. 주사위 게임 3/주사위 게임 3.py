def solution(a, b, c, d):
    listABCD = [a, b, c, d,]
    countArr = [0] * (6+1)
    
    for item in listABCD:
        countArr[item] += 1
        
    p, q, r = 0, 0, 0
    
    if 4 in countArr:
        p = countArr.index(4)
        return 1111 * p
        
    if 3 in countArr:
        p = countArr.index(3)
        q = countArr.index(1)
        return (10*p + q)**2
    
    if 2 in countArr and 1 not in countArr:
        p, q = [i for i, value in enumerate(countArr) if value == 2]
        return (p + q) * abs(p - q)
    
    if 2 in countArr and 1 in countArr:
        q, r = [i for i, value in enumerate(countArr) if value == 1]
        return q*r
        
    return min(listABCD)