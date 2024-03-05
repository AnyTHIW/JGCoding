import sys
IFSs = sys.stdin.readlines

_Strings = [ _.rstrip() for _ in IFSs()]

# print(_Strings)

for item in _Strings:
    if  item == '0':
        break
    elif len(item)==1 or item[:len(item)//2] == item[-(len(item)//2):][::-1]:
        print('yes')
    else:
        print('no')