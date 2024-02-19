import sys

# from AlgoTime import CalculateTime
IFS = sys.stdin.readline


# @CalculateTime
def heap_sort(arr):
    def heapify(arr, left: int, right: int):
        temp = arr[left]

        parent = left
        while parent < (right + 1) // 2:
            curr_left = parent*2 + 1
            curr_right = curr_left + 1

            child = curr_right if curr_right <= right and arr[
                curr_right] > arr[curr_left] else curr_left
            if temp >= arr[child]:
                break
            arr[parent] = arr[child]
            parent = child
        arr[parent] = temp

    n = len(arr)

    for i in range((n-1) // 2, -1, -1):
        heapify(arr, i, n-1)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i-1)


if __name__ == '__main__':
    _N = int(IFS().rstrip())
    _numbers = [int(IFS().rstrip()) for _ in range(_N)]
    heap_sort(_numbers)
    print(* _numbers, sep="\n")
