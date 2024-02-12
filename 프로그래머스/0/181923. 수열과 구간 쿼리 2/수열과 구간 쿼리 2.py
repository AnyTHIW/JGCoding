def solution(arr, queries):
    valueList = []
    
    for qItem in queries:
        minValue = 1000001
        
        for subItem in arr[qItem[0]:qItem[1]+1]:
            if qItem[2] < subItem:
                minValue = min(minValue, subItem)
        
        if minValue == 1000001:
            minValue = -1
            
        valueList.append(minValue)
    
    return valueList