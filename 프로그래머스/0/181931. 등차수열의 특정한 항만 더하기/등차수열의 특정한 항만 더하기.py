def solution(a, d, included):
    index_true = []
    answer = 0

    for index, item in enumerate(included):
        if item:
            index_true.append(index)
    
    for i in index_true:
        answer += (a + d*i)
    
    return answer