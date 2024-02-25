import sys
IFS = sys.stdin.readline

_Unq_Number = [*(map(int, IFS().rstrip().split()))]

def Square(number):
    return number**2
    
print(sum( Square(_) for _ in _Unq_Number )%10)
