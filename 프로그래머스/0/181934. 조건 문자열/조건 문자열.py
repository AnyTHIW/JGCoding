def solution(ineq, eq, n, m):
    return int((eq == '=' and n == m) or (ineq == '>' and n > m) or (ineq == '<' and n < m))