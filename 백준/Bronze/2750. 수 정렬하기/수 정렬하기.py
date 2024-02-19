
import array
import sys

IFS = sys.stdin.readline



def bubble_sort(a: list) -> None:
    n = len(a)
    k = 0

    while k < n-1:
        last = n-1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last


if __name__ == '__main__':
    _N = int(IFS().rstrip())
    _numbers = [int(IFS().rstrip()) for _ in range(_N)]
    bubble_sort(_numbers)

    print(* _numbers, sep="\n")
