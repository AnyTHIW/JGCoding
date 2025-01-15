import sys

input = sys.stdin.readline

N_ = int(input().rstrip())
SkewerList_ = list(map(int, input().split()))

lPointer, rPointer = 0, 0
typeFreq = [-1] + [0] * 9
typeNumber = 0
maxLength = 0

while (rPointer < N_):
    extendItem = SkewerList_[rPointer]
    typeFreq[extendItem] += 1
    
    if typeFreq[extendItem] == 1:
        typeNumber += 1
    
    while (typeNumber > 2):
        shortenItem = SkewerList_[lPointer]
        typeFreq[shortenItem] -= 1
        
        if typeFreq[shortenItem] == 0:
            typeNumber -= 1
            
        lPointer += 1
    
    maxLength = max(maxLength, rPointer - lPointer + 1)
    rPointer += 1

print(maxLength)