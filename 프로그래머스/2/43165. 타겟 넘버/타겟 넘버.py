def solution(numbers, target):
    method = 0
    
    def addOrSubtract(sumResult, idx):
        nonlocal method
        
        if idx == len(numbers):
            
            if sumResult == target:
                method += 1
            return

        addOrSubtract(sumResult + numbers[idx], idx + 1)
        addOrSubtract(sumResult - numbers[idx], idx + 1)

    addOrSubtract(0, 0)

    return method