# for for 2개 돌려서 합이 최소인 간선과 그 노드 둘을 찾는다
# 그 간선의 근접 간선 중 합해서 최소인 간선을 찾고 잇는다 (이은 후 연결된 노드들은 후보 노드에서 지워야한다)
# 반복한다
import sys

v, e = [int(item) for item in input().split()]
edges = [
    list(map(int, sys.stdin.readline().split())) for _ in range(e)
]  # 간선 정보를 리스트로 받음

whos_next = []
# 초기에는 내가 나 자신을 가리키게 해야한다

rank = []


def init_set():
    global whos_next, rank

    whos_next = [i for i in range(v + 1)]
    rank = [0] * (v + 1)


# 각 서로소 노드셋의 대표 노드를 찾는 함수
def find_repre(node):
    global whos_next

    """이게 path compression 기법"""
    if whos_next[node] != node:
        # 현재 노드의 대표정보가 자기자신으로 저장되어 있지 않으면
        # (대표는 대표리스트에 자기자신의 값으로 인덱스접근 시 값이 자기자신으로 저장되어있고, 나머지는 대표가 앞 사람으로 저장되어 있다)
        # 자신의 값과, 자신의 값을 대표정보가 저장되어있는 리스트에 인덱스로 접근했을 시의 정보가 일치하지않으면

        whos_next[node] = find_repre(whos_next[node])
        # 자신을 인덱스로해 자신의 대표 정보(값)과 (여기서는 자신의 앞사람 인덱스이자 값에 해당) 대표리스트를 다시 비교

    return whos_next[node]
    # 현재 노드가 부모의 자식노드가 맞으면, 부모 출력
    """ 끝 """


def unite(node_1, node_2):
    global whos_next, rank

    repre_1 = find_repre(node_1)
    repre_2 = find_repre(node_2)

    """ 거지같은 union-by-rank 기법 """
    if rank[repre_1] > rank[repre_2]:
        # repre_1이 대표하는 나무의 크기가 repre_2가 대표하는 나무의 크기보다 크면,

        whos_next[repre_2] = repre_1
        # repre_2의 whos_next값을 (원래 자기자신) repre_1의 값으로 옮기고   (합쳐야되니까)

    else:
        whos_next[repre_1] = repre_2
        # 반대 케이스면 반대로 합치고

        if rank[repre_1] == rank[repre_2]:
            # 같은크기의 나무면
            rank[repre_2] += 1
            # 한 나무를 위에 쌓는 느낌으로 합치기 때문에 1랭크 올려줘야함
            """ 끝 """


def kruskal(graph):
    global whos_next, rank
    MST = []

    init_set()

    edges.sort(key=lambda x: x[2])  # 간선을 가중치에 따라 정렬
    total_weight = 0

    for edge in edges:
        node1, node2, weight = edge

        if find_repre(node1) != find_repre(node2):
            unite(node1, node2)
            MST.append(edge)
            total_weight += weight

    return total_weight


result = kruskal(edges)
print(result)
