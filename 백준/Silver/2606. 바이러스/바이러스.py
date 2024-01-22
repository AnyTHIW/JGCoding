import sys


com_num = int(input())
edge_pair = int(input())

graph_data = [
    [int(item) for item in sys.stdin.readline().split()]
    for _ in range(1, edge_pair + 1)
]
graph_drawing = [[] for _ in range(com_num + 1)]
# 편의를 위해 index 0은 쓰지 않음


for item in graph_data:
    from_v, to_v = item[0], item[1]
    graph_drawing[from_v].append(to_v)
    graph_drawing[to_v].append(from_v)


infected_com = 0


def bfs(graph, start):
    global infected_com
    visited = [False] * (com_num + 1)
    # 편의를 위해 index0은 안씀
    queue = [start]

    while queue:
        node = queue.pop(0)
        # popleft()랑 똑같음

        if not visited[node]:
            visited[node] = True
            infected_com += 1
            queue.extend(
                neighbor for neighbor in graph_drawing[node] if not visited[neighbor]
            )


bfs(graph_drawing, 1)
print(infected_com - 1)
