import sys

IFS = sys.stdin.readline


def solution(word):
    print(*sorted(set(word), key=lambda item: (len(item), item)), sep="\n")


if __name__ == "__main__":
    _N = int(IFS().rstrip())
    _Word = [str(IFS().rstrip()) for _ in range(_N)]
    solution(_Word)
