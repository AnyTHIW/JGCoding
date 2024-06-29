import sys
IFS = sys.stdin.readline
IFSs = sys.stdin.readlines

# stable, ascending sort
_N_Member = IFS().rstrip()
_Line_MemberList = [{"age": int(_.rstrip().split()[0]), "name":_.rstrip().split()[1]} for _ in IFSs()]

_Line_MemberList.sort(key=lambda x: x["age"])

for member in _Line_MemberList:
    print(member["age"], member["name"])