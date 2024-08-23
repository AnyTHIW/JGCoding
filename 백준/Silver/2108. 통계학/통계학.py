import sys

def ArithmeticMean(lst:list)->int:
    return round (sum(lst) / len(lst))

def Median(lst:list)->int:
    newLst = sorted(lst)
    return newLst[len(lst)//2]

def Mode(lst:list)->int:
    countList = {}
    
    for num in lst:
        if num not in countList:
            countList[num] = 1
        else:
            countList[num] += 1
            
    mx = max(countList.values())
    mx_list = [key for key, value in countList.items() if value == mx]
    mx_list.sort()
    
    return mx_list[1] if len(mx_list) > 1 else mx_list[0]
    
def Range(lst:list)->int:
    return max(lst) - min(lst)

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_NumberList = [ int(_) for _ in IFSs() ]

amean, med, mod, rng = ArithmeticMean(_NumberList), Median(_NumberList), Mode(_NumberList), Range(_NumberList)

print(amean)
print(med)
print(mod)
print(rng)