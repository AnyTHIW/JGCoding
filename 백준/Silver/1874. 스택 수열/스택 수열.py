import sys

class CustomList(list):
    def __init__(self):
        super().__init__()
        self.plusMinus = ""
    
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
    while numb <= item:
        stack.push(numb)
        numb += 1
    
    if stack and item == stack[-1]:
        stack.pop()
    else:
        print("NO")
        break

else:
    print("\n".join(stack.plusMinus))