def solution(arr):
    stk = []
    i = 0
    while (i < len(arr)):
        if not len(stk) :
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] < arr[i] :
                stk += [arr[i]]
                i += 1
            else :
                stk.pop()
                
    return stk