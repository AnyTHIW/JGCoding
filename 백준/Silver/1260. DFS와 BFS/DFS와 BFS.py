import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

# print(n, m, v)

graph_data = [[int(item) for item in sys.stdin.readline().split()] for _ in range(m)]

# print(graph)

# graph_drawing = [[] * m]  # 인접 리스트 초기화
graph_drawing = [[] for _ in range(n + 1)]

# 기발한 방법
for item in graph_data:
    from_v, to_v = item[0], item[1]
    graph_drawing[from_v].append(to_v)
    graph_drawing[to_v].append(from_v)

for _ in graph_drawing:
    _.sort()


def dfs(g, start, visited):
    print(start, end=" ")
    visited[start] = True
    for neighbor in g[start]:
        if not visited[neighbor]:
            dfs(g, neighbor, visited)


def bfs(g, start):
    visited = [False] * (n + 1)
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            queue.extend(neighbor for neighbor in g[node] if not visited[neighbor])


# DFS 수행
visited_dfs = [False] * (n + 1)
dfs(graph_drawing, v, visited_dfs)
print()

# BFS 수행
visited_bfs = [False] * (n + 1)
bfs(graph_drawing, v)
print()
