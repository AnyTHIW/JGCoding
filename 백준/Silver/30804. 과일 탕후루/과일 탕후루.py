import sys

input = sys.stdin.readline

N_ = int(input().rstrip())
SkewerList_ = list(map(int, input().split()))

lPointer, rPointer = 0, 0
typeFreq = [0] * 10
typeList = set()
maxLength = 0

while (rPointer < N_):
    extendItem = SkewerList_[rPointer]
    typeFreq[extendItem] += 1
    
    if extendItem not in typeList:
        typeList.add(extendItem)
    
    while (len(typeList) > 2):
        shortenItem = SkewerList_[lPointer]
        typeFreq[shortenItem] -= 1
        
        if typeFreq[shortenItem] == 0:
            typeList.remove(shortenItem)
            
        lPointer += 1
    
    if maxLength < (rPointer - lPointer + 1):
        maxLength = rPointer - lPointer + 1
        
    rPointer += 1

print(maxLength)