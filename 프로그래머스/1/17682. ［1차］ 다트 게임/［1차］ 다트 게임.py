def solution(dartResult):
    answer = 0
    
    scoreList = []
    numb = ""
    
    for char in dartResult:
        if char.isdigit():
            numb += char
            continue

        if numb:
            scoreList += [int(numb)]
            numb = ""
        
        if char.isalpha():
            if char == "D":
                scoreList[-1] **= 2
            elif char == "T":
                scoreList[-1] **= 3
        
        if char == "#":
            scoreList[-1] = - scoreList[-1]
            
        elif char == "*":
            scoreList[-1] = scoreList[-1] * 2
            
            if len(scoreList) != 1:
                scoreList[-2] = scoreList[-2] * 2
    
    return sum(scoreList)