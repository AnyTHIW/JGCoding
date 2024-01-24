from collections import deque

_N, _M = map(int, input().split())
_INPUT = [list(map(int, input().split())) for _ in range(_M)]

# 인접 리스트와 진입 차수 초기화
graph = [[] for _ in range(_N + 1)]
in_degree = [0] * (_N + 1)

for edge in _INPUT:
    a, b = edge
    graph[a].append(b)
    in_degree[b] += 1


# 위상 정렬 함수
def topological_sort():
    result = []
    queue = deque()

    # 진입 차수가 0인 노드를 큐에 추가
    for i in range(1, _N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)

        # 현재 노드와 연결된 노드들의 진입 차수 감소
        for adjacent_node in graph[node]:
            in_degree[adjacent_node] -= 1

            # 진입 차수가 0이 되면 큐에 추가
            if in_degree[adjacent_node] == 0:
                queue.append(adjacent_node)

    return result


# 위상 정렬 수행
result = topological_sort()

# 결과 출력
print(*result)
