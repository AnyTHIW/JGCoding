"""그래프 탐색 기본"""

import sys
# sys 임포트
INPUT_FROM_SYS = sys.stdin.readline

# _V, _E = [int(item) for item in input().split()]
_V, _E = [int(item) for item in input().split()]
# _V, _E = map(int, INPUT_FROM_SYS().split())
# 문제입력
# 첫째줄 : _V, _E
# 둘째줄 : E개의 간선정보 3개 정점번호, 정점번호, 가중치

maindata_edges = [list(map(int, sys.stdin.readline().split())) for _ in range(_E)]
# 간선 갯수만큼 줄 데이터를 리스트로 받아서, edges에 저장

whos_next = []
'''초기에는 내가 나 자신을 가리키게 해야한다'''
# 정점번호를 인덱스 삼아, 자신이 누구와 연결된 건지 확인할수 있어야함

rank = []
'''나무크기'''
# 나무의 크기도 확인하기 위해서, 나무 크기를 저장하는 자료도 필요함

def init_set():
    # set을 초기화 시키는 함수
    global whos_next, rank
    # 바깥에서 whos_next와 rank를 참조
    whos_next = [i for i in range(_V + 1)]
    # 연결정보에 인덱스와 그에 따른 리스트 생성 (index0 안씀)
    rank = [0] * (_V + 1)
    # 나무크기 정보 역시 정점갯수+1만큼 생성 (index0 안씀)


# 각 서로소 노드셋의 대표 노드를 찾는 함수
def find_repre(node):
    global whos_next
    # 연결정보 전역선언

    """이게 path compression 기법"""
    if whos_next[node] != node:
    # '''        # 현재 노드의 대표정보가 자기자신으로 저장되어 있지 않으면
    #         # (대표는 대표리스트에 자기자신의 값으로 인덱스접근 시 값이 자기자신으로 저장되어있고, 나머지는 대표가 앞 사람으로 저장되어 있다)
    #         # 자신의 값과, 자신의 값을 대표정보가 저장되어있는 리스트에 인덱스로 접근했을 시의 정보가 일치하지않으면'''
    # 연결정보에서 현재 노드가 자신의 노드가 아니면 (자신의 노드이면 그 노드가 연결된 나무의 대표노드임)

        whos_next[node] = find_repre(whos_next[node])
        # 대표를 찾아 현재 노드의 연결정보에 저장 & 동시에 재귀진입
        # 자신을 인덱스로해 자신의 대표 정보(값)과 (여기서는 자신의 앞사람 인덱스이자 값에 해당) 대표리스트를 다시 비교

    return whos_next[node]
    # 현재 노드가 부모의 자식노드가 맞으면, 부모 출력
    """ 끝 """

'''유니온 함수'''
def unite(node_1, node_2):
    # 연결 요소들끼리 합치는 함수 (찾을 나무 요소1, 찾을 나무 요소 2):
    global whos_next, rank
    # 연결데이터, 높이데이터 전역선언

    repre_1 = find_repre(node_1)
    # 대표1 찾기
    repre_2 = find_repre(node_2)
    # 대표2 찾기

    """ 거지같은 union-by-rank 기법 """
    if rank[repre_1] > rank[repre_2]:
        # repre_1이 대표하는 나무의 크기가 repre_2가 대표하는 나무의 크기보다 크면,

        whos_next[repre_2] = repre_1
        # repre_2의 whos_next값을 (원래 자기자신) repre_1으로 옮기고 (합쳐야되니까)

    else:
        whos_next[repre_1] = repre_2
        # 반대 케이스면 반대로 합치고

        if rank[repre_1] == rank[repre_2]:
            # 같은크기의 나무면
            rank[repre_2] += 1
            # 나무 위에 다른 나무를 쌓는 느낌으로 합치기 때문에 1랭크 올려줘야함 (합쳐야되니까)
    """ union-by-rank 끝 """
'''유니온 함수 끝'''

'''크루스칼 함수'''
def kruskal(graph):
    # 크루스칼 (쓸 그래프):
    global whos_next, rank
    # 연결정보, 랭크정보 전역선언
    MST = []
    # 최소신장트리 정보 저장배열

    init_set()
    # init하기

    maindata_edges.sort(key=lambda x: x[2])
    # 간선을 가중치에 따라 정렬
    # 간선 정렬 (익명함수, 내장함수의 정렬법 씀)
    total_weight = 0
    # 전체 가중치 (최소 스패닝 트리의 가중치를 출력하는게 문제)

    for edge in maindata_edges:
        # 간선들 중 간선에 대해:
        node1, node2, weight = edge
        # 간선의 정보를 언패킹해서 사용할 준비

        if find_repre(node1) != find_repre(node2):
            # 대표찾는 함수를 써서 둘의 대표가 다르면:
            unite(node1, node2)
            # 합치기
            MST.append(edge)
            # 최소신장트리에 간선추가
            total_weight += weight
            # 가중치 추가

    return total_weight
    # 가중치 반환

result = kruskal(maindata_edges)
# 결과를
print(result)
# 출력
