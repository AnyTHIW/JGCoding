def push(integer_X):
    _this_is_stack.append(integer_X)

def pop():
    # 가장 위에있는 정수를 뺀다
    # 그 정수를 출력한다.
    # 없으면 -1
    
    if len(_this_is_stack) >= 1:
        print( _this_is_stack.pop() )
    else:
        print(-1) 
    
def size():
    # 스택의 정수갯수를 출력한다.
    print(len(_this_is_stack))

def empty():
    if len(_this_is_stack) == 0:
        print(1)
    else:
        print(0)
        
def top():
    if len(_this_is_stack) == 0:
        print(-1)
    else:
        print(_this_is_stack[len(_this_is_stack)-1])

import sys
_n = int(input())
_input_CMD = [sys.stdin.readline().strip() for _ in range(_n)]

_this_is_stack = []

for cmd_line in _input_CMD:
    cmd = cmd_line.split()
    
    function_name = str(cmd[0])

    if function_name == 'push':
        push(cmd[1])
    elif function_name == 'pop':
        pop()
    elif function_name == 'size':
        size()
    elif function_name == 'empty':
        empty()
    elif function_name == 'top':
        top()