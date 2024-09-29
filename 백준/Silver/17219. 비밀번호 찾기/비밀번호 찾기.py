import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

_N, _M = map(int, IFS().split())

_SitePassword = dict()

for i in range(_N):
    site, pwd = IFS().split()
    _SitePassword[site] = pwd
    
for i in range(_M):
    site = IFS().rstrip()
    print(_SitePassword[site])