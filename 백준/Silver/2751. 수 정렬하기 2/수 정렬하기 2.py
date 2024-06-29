import sys
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_ = IFS()
lines = [int(_.strip()) for _ in IFSs()]

print(*sorted(lines), sep='\n')
