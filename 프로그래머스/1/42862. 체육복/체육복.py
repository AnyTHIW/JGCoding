def solution(n, lost, reserve):
    answer = 0
    
    lostSet = set(lost) - set(reserve)
    reserveSet = set(reserve) - set(lost)
    
    for res in sorted(reserveSet):
        if (res-1) in lostSet:
            lostSet.remove(res-1)
        elif (res+1) in lostSet:
            lostSet.remove(res+1)
            
    answer = n - len(lostSet)
    
    return answer