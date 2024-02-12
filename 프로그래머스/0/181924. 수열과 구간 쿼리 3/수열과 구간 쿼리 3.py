def solution(arr, queries):
    
    for queryItem in queries:
        data1 = arr[queryItem[0]]
        data2 = arr[queryItem[1]]
        arr[queryItem[1]] = data1
        arr[queryItem[0]] = data2

    return arr