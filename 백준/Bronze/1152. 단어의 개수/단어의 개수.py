import sys
IFS = sys.stdin.readline

_OneString = [*(map(str, IFS().rstrip().split()))]
    
print(len(_OneString))