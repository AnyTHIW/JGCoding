def solution(arr):
    answer = []
    idxS, idxE = -1,-1
    
    for idx, val in enumerate(arr):
        if val == 2:
            if idxS == -1:
                idxS, idxE = idx, idx
            else:
                idxE = idx
    
    if idxS == -1:
        answer = [-1]
    else:
        answer = arr[idxS:idxE+1]
    
    return answer