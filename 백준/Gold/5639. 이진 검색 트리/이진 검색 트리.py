def post_order(start, end):
    if start > end:
        return
    # start인덱스가 end와 같아질 때까지 start를 비교하고, end보다 커지면 탈출

    # 1.
    root = pre_list[start]

    idx = start + 1

    while idx <= end and pre_list[idx] < root:
        # 다음 루프에서 idx > end == False
        # 순회할 인덱스의 값이 root값 보다는 작을 때
        # idx <= end는당연한거

        idx += 1
        # left트리의 가장작은 노드값을 가지는를 만날때 while 탈출

    # 2.
    post_order(start + 1, idx - 1)
    # 재귀호출이라서 계속 탐색 (left트리)

    # 3.
    # 오른쪽 서브트리 호출
    post_order(idx, end)
    # 재귀호출이라서 계속 탐색 (right트리)

    # 후위 순회 결과 출력
    print(root)


import sys

sys.setrecursionlimit(10**9)

pre_list = list(map(int, sys.stdin.readlines()))

post_order(0, len(pre_list) - 1)
