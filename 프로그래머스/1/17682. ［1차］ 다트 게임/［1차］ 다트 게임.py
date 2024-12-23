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
        
        if char in "SDT":
            power = {"S":1, "D":2, "T":3}[char]
            scoreList[-1] **= power
            continue
        
        if char == "#":
            scoreList[-1] = - scoreList[-1]
        elif char == "*":
            scoreList[-1] *= 2
            if len(scoreList) > 1:
                scoreList[-2] *= 2
    
    return sum(scoreList)