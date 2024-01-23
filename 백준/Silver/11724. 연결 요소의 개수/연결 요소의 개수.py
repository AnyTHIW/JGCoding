import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]


def dfs(node, visited, graph):
    visited[node] = True
    # 노드 방문 표시
    for neighbor in graph[node]:
        # 그래프 노드의 item인 이웃에 대해
        if not visited[neighbor]:
            # 방문하지 않았으면
            dfs(neighbor, visited, graph)
            # 재귀 진입


def count_connected_components(graph, n):
    # 연결요소 세는 함수
    visited = [False] * (n + 1)
    # 연결요소 1부터 N까지 이용할 거여서, 0을 제외하려면 *n+1
    count = 0
    # count 초기화

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node, visited, graph)
            count += 1

    return count


graph = defaultdict(list)

for item in data:
    u, v = item[0], item[1]
    graph[u].append(v)
    graph[v].append(u)

result = count_connected_components(graph, n)
print(result)
