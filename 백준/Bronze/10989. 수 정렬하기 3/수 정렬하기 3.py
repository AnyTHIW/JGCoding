import sys

# from AlgoTime import CalculateTime

IFS = sys.stdin.readline
OFS = sys.stdout.write


# @CalculateTime
def solution(_N):
    count = [
        0
    ] * 10001  # 계수 배열 초기화 (문제 조건에 따라 0부터 10000까지의 수를 다룰 수 있어야 함)

    for _ in range(_N):
        num = int(IFS().rstrip())
        count[num] += 1  # 해당하는 idx값 증가

    for i in range(10001):  # idx배열을 돌면서
        if count[i] > 0:  # 0이 아닌 idx를
            for _ in range(count[i]):  # idx값(idx가 카운트된 횟수) 만큼
                OFS(str(i) + "\n")  # 출력


if __name__ == "__main__":
    _N = int(IFS().rstrip())
    solution(_N)
