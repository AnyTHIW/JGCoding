def solution(arr, queries):
    for qItem in queries:
        for index in range(len(arr)):
            if (qItem[0] <= index <= qItem[1]) and not bool(index % qItem[2]):
                arr[index] += 1

    return arr