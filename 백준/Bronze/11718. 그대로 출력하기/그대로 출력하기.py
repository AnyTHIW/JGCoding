import sys
IFSs = sys.stdin.readlines

_String_S = [_.rstrip() for _ in IFSs()]

print(*_String_S, sep="\n")