import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N, _M = map(int, IFS().split())
_HaventHeardOf = set()
_HaventSeen = set()

for i in range(_N):
    _HaventHeardOf.add(IFS().rstrip())
    
for i in range(_M):
    _HaventSeen.add(IFS().rstrip())
    
_Both = sorted(_HaventHeardOf & _HaventSeen)

print(len(_Both))
print(*_Both, sep="\n")