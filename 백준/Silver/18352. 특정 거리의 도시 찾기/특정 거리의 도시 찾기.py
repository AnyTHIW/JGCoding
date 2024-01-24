from collections import deque
import sys

n, m, k, x = map(int, input().split())
# 입력
# n, m, k, s = map(int, input().split())
# print(n, m, k, x)
# n : 도시의 개수, m : 도로의 개수, k : 거리 정보, x : 출발 도시의 번호

graph = {}
# 그래프는 빈 딕셔너리로
for i in range(n + 1):
    # range는 헷갈리니까 n+1로 선언하고, 0은 안 쓰는걸로하자
    graph[i] = []
    # i 당 빈 딕셔너리 생성.
for i in range(m):
    # m(도로의 갯수)에 대해 :
    start_city, end_city = list(map(int, sys.stdin.readline().split()))
    # 데이터 쌍 가져와서
    # print(start_city, end_city)

    graph[start_city].append(end_city)
# 데이터 1번을 그래프의 시작도시로 생각하고 접근해서, 연결된 도시번호를 append

# bfs
distance_list = [0 for _ in range(n + 1)]
# 거리 정보를 담은 리스트 n+1개 선언 및 0으로 초기화
visited_list = [0 for _ in range(n + 1)]
# 방문 정보를 담은 리스트 n+1개 선언 및 0으로 초기화
this_is_Q = deque([x])
# queue.append(s)
# deque형태의 큐를 선언해, 거기에 start도시를 바로 넣어서 queue로 선언
visited_list[x] = 1
# s는 시작이니 이미 방문한 형태로, visit에 1로 저장
while this_is_Q:
    # queue가 빈 deque가 아니면:
    spotlight_node = this_is_Q.popleft()
    # deque에서 하나 빼서 현재 위치로 삼기
    for neighbor in graph[spotlight_node]:
        # 그래프에서 현재 위치의 인접도시 값들을 (graph에 저장해 놓긴 함)
        if visited_list[neighbor] == 0:
            # now의 인접 도시를 방문해 방문하지 않은 도시면:
            this_is_Q.append(neighbor)
            # 큐에 j도시를 추가하고
            visited_list[neighbor] = 1
            # j를 방문처리
            distance_list[neighbor] = distance_list[spotlight_node] + 1
# 현재위치에서 거리 정보를 담은 리스트에 1을 추가해, 새로 방문한 도시 j에서 갱신 (now와 j)

count_k_distance_city = 0
#

for i in range(1, n + 1):
    # 1부터 n까지에 대해:
    if distance_list[i] == k:
        # 도시위치 i의 거리가 최단거리k와 같을 경우
        print(i)
        # i를 프린트
        count_k_distance_city += 1
# 도시의 갯수를 증가시킴
if count_k_distance_city == 0:
    print(-1)
