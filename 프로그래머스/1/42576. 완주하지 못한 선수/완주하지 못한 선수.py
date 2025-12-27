def solution(participant, completion):
    answer = ''
    count = {}
    
    for nameP in participant:
        if not nameP in count:
            count[nameP] = 1
        else:
            count[nameP] += 1
    
    for nameC in completion:
        if nameC in count:
            count[nameC] -= 1
    
    for nameP in participant:
        if count[nameP] == 1:
            answer = nameP
            break
    
    return answer