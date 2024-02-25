import sys
IFS = sys.stdin.readline

_A, _B = map(int, IFS().rstrip().split())

def At_Operator(a, b):
    return (a + b)*(a - b)
    

print(At_Operator(_A, _B))