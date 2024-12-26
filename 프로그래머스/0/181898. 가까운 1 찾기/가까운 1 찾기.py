def solution(arr, idx):
    
    answer = -1
    
    for arrIdx in range(idx, len(arr)):
        if arr[arrIdx] == 1:
            return arrIdx
     
    return answer
