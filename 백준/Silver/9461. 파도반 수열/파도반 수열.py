import sys

justRead = sys.stdin.read
data = justRead().splitlines()

_T = int(data[0])

def DP_up(number: int) -> int:
    lst = [-1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * max(0, number - 10)
    
    if number < 11:
        return lst[number]
    
    for iter in range(11, number+1):
        lst[iter] = lst[iter-5] + lst[iter-1]
    
    return lst[number]

def DP_down(number: int) -> int:
    dct = {1:1, 2:1, 3:1, 4:2, 5:2, 6:3, 7:4, 8:5, 9:7, 10:9}
    
    def DP_down_inner(number: int) -> int:
        if number in dct:
            return dct[number]
        
        dct[number] = DP_down_inner(number-5) + DP_down_inner(number-1)
        
        return dct[number]
    
    return DP_down_inner(number)

for idx in range(1, _T+1):
    _N = int(data[idx])
    
    # print(DP_up(_N))
    print(DP_down(_N))
    