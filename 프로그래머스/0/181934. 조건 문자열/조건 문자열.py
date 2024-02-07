def solution(ineq, eq, n, m):
    if eq == '=' and n == m:
        return 1
    
    if ineq == '>' and n > m:
        return 1
    elif ineq == '<' and n < m:
        return 1
    
    return 0