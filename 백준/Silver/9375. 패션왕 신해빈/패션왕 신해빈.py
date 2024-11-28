import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines
JR = sys.stdin.read
data = JR().splitlines()

_tc = int(data[0])

def separateType(lst: list) -> dict[str, list]:
    costumeList = dict()
    
    for item in lst:
        name, type = item.split()
        
        if type in costumeList:
            costumeList[type] += [name]
        else:
            costumeList[type] = [name]
        
    return costumeList
        
idx = 1

for _ in range(_tc):
    result = 1
    
    dataLineNumber = int(data[idx])
    idx += 1
    _nList = data[idx:idx+dataLineNumber]
    idx += dataLineNumber
    
    resultList = separateType(_nList)
    
    for typ in resultList:
        result *= len(resultList[typ]) + 1
    
    result -= 1
    print(result)
