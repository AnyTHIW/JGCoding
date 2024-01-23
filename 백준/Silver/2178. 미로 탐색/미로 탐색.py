from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (
                0 <= nx < n
                and 0 <= ny < m
                and maze[nx][ny] == 1
                and not visited[nx][ny]
            ):
                queue.append((nx, ny))
                visited[nx][ny] = True
                maze[nx][ny] = maze[x][y] + 1


bfs()
print(maze[n - 1][m - 1])
