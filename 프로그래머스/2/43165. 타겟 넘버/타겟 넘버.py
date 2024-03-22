def solution(numbers, target):
    perfect_count = 0
    curr = 0
    result = 0
    
    def addOrSubtract(rst, crr):
        nonlocal perfect_count
        
        if crr == len(numbers):
            if rst == target:
                perfect_count += 1
            return

        addOrSubtract(rst + numbers[crr], crr + 1)
        addOrSubtract(rst - numbers[crr], crr + 1)

    addOrSubtract(0, 0)

    return perfect_count