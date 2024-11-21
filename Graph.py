# 코드 10.3: 너비 우선 탐색(인접 리스트 방식)
from queue import Queue                 # queue 모듈의 Queue 사용
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        # 그래프의 정점 수
    visited = [False]*n                 # 방문 확인을 위한 리스트
    Q = Queue()                         # 공백상태의 큐 생성
    Q.put(s)                            # 맨 처음에는 시작 정점만 있음
    visited[s] = True                   # s는 "방문"했다고 표시
    while not Q.empty() :
        s = Q.get()                     # 큐에서 정점을 꺼냄
        print(vtx[s], end=' ')          # 정점을 출력(처리)함
        for v in aList[s] :               # s의 모든 이웃 v에 대해
            if visited[v]==False :      # 방문하지 않은 이웃 정점이면
                Q.put(v)                # 큐에 삽입
                visited[v] = True       # "방문"했다고 표시


# 깊이 우선 탐색(인접행렬 방식)
def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          # 현재 정점 s를 출력함
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                DFS(vtx, adj, v, visited)



# 너비우선탐색을 이용한 연결성분 검사
from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    group = [s]    # 새로운 연결된 그룹 생성
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

# 연결성분검사 주 함수
def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []		# 부분 그래프별 정점 리스트

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups


# 깊이우선탐색을 이용한 신장트리
def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)

# 인접 정점
aList = [[ 1, 2 ],      # 'A'의 인접정점 인덱스
         [ 0, 3 ],      # 'B'의 인접정점 인덱스
         [ 0, 3, 4 ],   # 'C'
         [ 1, 2, 5 ],   # 'D'
         [ 2, 6, 7 ],   # 'E'
         [ 3 ],         # 'F'
         [ 4, 7 ],      # 'G'
         [ 4, 6 ] ]     # 'H'

# 간선(정점의 연결 관계)
dfs_edge = [ [  0,  1,  1,  0,  0,  0,  0,  0],
         [  1,  0,  0,  1,  0,  0,  0,  0],
         [  1,  0,  0,  1,  1,  0,  0,  0],
         [  0,  1,  1,  0,  0,  1,  0,  0],
         [  0,  0,  1,  0,  0,  0,  1,  1],
         [  0,  0,  0,  1,  0,  0,  0,  0],
         [  0,  0,  0,  0,  1,  0,  0,  1],
         [  0,  0,  0,  0,  1,  0,  1,  0] ]

# 연결 성분을 검사하는 인접 행렬
adjMat =  [ [ 0,  1,  1,  0,  0,  0,  0,  0 ], #A의 연결관계
            [ 1,  0,  0,  0,  0,  0,  0,  0 ], #B
            [ 1,  0,  0,  0,  0,  0,  0,  0 ], #C
            [ 0,  0,  0,  0,  1,  0,  0,  0 ], #D
            [ 0,  0,  0,  1,  0,  0,  0,  0 ], #E
            [ 0,  0,  0,  0,  0,  0,  1,  1 ], #F
            [ 0,  0,  0,  0,  0,  1,  0,  0 ], #G
            [ 0,  0,  0,  0,  0,  1,  0,  0] ] #H

# 신장 트리의 간선 행렬
st_edge = [ [  0,  1,  1,  0,  0,  0,  0,  0],
            [  1,  0,  0,  1,  0,  0,  0,  0],
            [  1,  0,  0,  1,  1,  0,  0,  0],
            [  0,  1,  1,  0,  0,  1,  0,  0],
            [  0,  0,  1,  0,  0,  0,  1,  1],
            [  0,  0,  0,  1,  0,  0,  0,  0],
            [  0,  0,  0,  0,  1,  0,  0,  1],
            [  0,  0,  0,  0,  1,  0,  1,  0] ]

print('-'*80)
vtx = list(input('vertex를 입력하세요 : ').split())
print()
adjList = [list(map(str, input('edge를 입력하세요 : '))) for _ in range(9)]
print('-'*80)

# 인접 리스트 생성
adj_dict = {v: [] for v in vtx}  # 빈 딕셔너리 초기화
for edge in adjList:
    u, v = edge  # 간선의 두 정점
    adj_dict[u].append(v)
    adj_dict[v].append(u)  # 무방향 그래프일 경우

# 결과 출력
print("<Adjacent Vertex List>")
for key, value in adj_dict.items():
    print(f"{key}: {value}")
print('-'*80)

'''
print('vertex : '+', '.join(vtx))
print('edge : '+', '.join(['-'.join(inner) for inner in adjList]))
print('-'*80)
'''

print('BFS : ', end="")
BFS_AL(vtx, aList, 0)
print()

print('DFS : ', end="")
DFS(vtx, dfs_edge, 0, [False]*len(vtx))
print()
print('-'*80)

colorGroup = find_connected_component(vtx, adjMat)
print("Number of Connected component = %d " % len(colorGroup))
print('Connected Component(BFS) : ', colorGroup)
print('-'*80)

print('Spanning Tree(DFS) : ', end="")
ST_DFS(vtx, st_edge, 0, [False]*len(vtx))
print()
print('-'*80)
