import sys
IFS = sys.stdin.readline

_n = set(int(IFS().rstrip()) for _ in range(28))

numberlist = set(range(1,31))
new_set = (numberlist - _n)

print(*sorted(new_set), sep="\n")