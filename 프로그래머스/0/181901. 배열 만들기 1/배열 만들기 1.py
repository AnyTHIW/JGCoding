def solution(n, k):
    answer = []
    
    kMul = k
    
    while (kMul <= n):
        answer.append(kMul)
        kMul += k
    
    return answer