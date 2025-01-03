import sys
sys.setrecursionlimit(10**6)

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines
INFINITE = float('inf')

_N = int(IFS().rstrip())

def DP_upward(number):
    lst = [-1, 0, 1, 1] + [-1] * max(0, number-3)
    
    testingNumber = 3
    
    while (testingNumber <= number):
        
        temp1, temp2 = INFINITE, INFINITE
        if not(testingNumber%3):
            temp1 = lst[testingNumber//3] + 1
            
        if not(testingNumber%2):
            temp2 = lst[testingNumber//2] + 1
        
        lst[testingNumber] = int(min(lst[(testingNumber-1)] + 1, temp1, temp2))
        
        testingNumber += 1
        
    return print(lst[number])

def DP_downward(number):
    lst = {1:0, 2:1, 3:1}

    def DP_downward_inner(number):
        if number in lst:
            return lst[number]
        
        if not(number%6):
            lst[number] = min(DP_downward_inner(number//3), DP_downward_inner(number//2)) + 1

        elif not(number%3):
            lst[number] = min(DP_downward_inner(number//3), DP_downward_inner(number-1)) + 1

        elif not(number%2):
            lst[number] = min(DP_downward_inner(number//2), DP_downward_inner(number-1)) + 1

        else:
            lst[number] = DP_downward_inner(number-1) + 1
        
        return lst[number]

    return print(DP_downward_inner(number))
    
# DP_upward(_N)
DP_downward(_N)

