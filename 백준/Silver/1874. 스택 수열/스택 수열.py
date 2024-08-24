import sys

class CustomList(list):
    plusMinus = ""
    
    def push(self:"CustomList", num:int):
        super().append(num)
        self.plusMinus += "+"
    
    def pop(self:"CustomList"):
        target = super().pop()
        self.plusMinus += "-"

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N = int(IFS().rstrip())
_Order = [ int(_) for _ in IFSs() ]

stack = CustomList()

numb = 1
for item in _Order:
    while not stack or item > stack[-1]:
        stack.push(numb)
        numb += 1
    
    if item == stack[-1]:
        stack.pop()
    else:
        print("NO")
        break

else:
    for chr in stack.plusMinus:
        print(chr)