# 위상정렬 문제

from collections import deque
# deque를 import

import sys
input_from_sys = sys.stdin.readline
# 속도를 올리기위한 팁, input을 쓰지말자

_N, _M = map(int, input_from_sys().split())
# 기본데이터 입력받기
_INPUT = [list(map(int, input_from_sys().split())) for _ in range(_M)]
# range(_M)에 대해 _INPUT data 입력받기

graph = [list() for _ in range(_N + 1)]
# 역시나 index 0 값은 안 쓰고, _N+1에 대해, 배열내배열 선언
# 인접 리스트와 진입 차수 초기화

in_degree = [0] * (_N + 1)
# 위상정렬을 쓰는 것이므로, 진입차수에 관한 데이터 사용
# 진입차수 배열 선언 및 초기화 (초기화는 0으로, 역시 index0은 안쓴다)

for edge in _INPUT:
    # 모든 _INPUT의 item인 edge에 대해
    a, b = edge
    # edge부분 의 시작과 끝을 선언하고
    graph[a].append(b)
    # 그래프의 시작값을 인덱스로 하는 그래프 요소에 대해 끝값을 붙임
    in_degree[b] += 1
    # 끝값의 진입차수가 증가하므로, 진입차수 배열에 +1추가


""" 위상 정렬 함수 """


def topological_sort():
    # 함수 지정 :
    # result = []
    # 결과값 배열 선언
    queue = deque()
    # 자료구조 deque 선언

    for i in range(1, _N + 1):
        # 1~N (index0제외) 중 i에 대해 :
        if in_degree[i] == 0:
            # 진입 차수가 0인 노드를 큐에 추가
            queue.append(i)
            # 자료구조 queue에 삽입

    while queue:
        # queue가 비어있지 않으면:
        node = queue.popleft()
        # queue에서 맨 앞을 꺼내어서
        # result.append(node)
        # 결과값 배열에 추가
        print(node, end=" ")
        # or 바로 출력해버리기 (시간이 줄어드나??)

        for adjacent_node in graph[node]:
            # 결과값의 인접 노드들에 대해 :
            in_degree[adjacent_node] -= 1
            # 현재 노드와 연결된 노드들의 진입 차수 감소

            if in_degree[adjacent_node] == 0:
                # -1 했으므로, 진입 차수가 0이 된 몇개가 생겼을 것이므로,
                # 그들을 조사해야되므로

                queue.append(adjacent_node)
                # 진입차수 0인 인접 노드들을 큐에 추가

    # return result
    return


"""위상정렬 끝"""


result = topological_sort()
# # 위상 정렬 수행

# print(*result)
# # 결과 출력
