import sys

IFS = sys.stdin.readline
IFSs = sys.stdin.readlines
OFS = sys.stdout.write


def can_hunt(fire_position, animal_position, L):
    x, y = animal_position
    # 사대와 동물 사이의 최소 거리 계산
    min_dist = abs(fire_position - x) + y
    return min_dist <= L


# name starting with _ and Upperletter represents In-Question Variables
def solution(_FirePosition, _Animal_position, _L):
    _FirePosition.sort()
    hunted = 0

    for animal in _Animal_position:
        left, right = 0, len(_FirePosition) - 1
        can_be_hunted = False
        while left <= right:
            mid = (left + right) // 2
            if can_hunt(_FirePosition[mid], animal, _L):
                can_be_hunted = True
                break
            if _FirePosition[mid] < animal[0]:
                left = mid + 1
            else:
                right = mid - 1
        if can_be_hunted:
            hunted += 1

    return hunted


if __name__ == "__main__":
    _M, _N, _L = map(int, IFS().split())
    _FirePosition = list(map(int, IFS().split()))
    _Animal_position = [list(map(int, _.split())) for _ in IFSs()]

    print(solution(_FirePosition, _Animal_position, _L))
