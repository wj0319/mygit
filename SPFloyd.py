# 코드 11.16: Floyd 알고리즘
INF = 9999
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (A[i][j] == INF) :
                print(" INF ", end='')
            else :
                print("%4d "%A[i][j], end='')
        print("");

def find_shortest_path(vertex, adj):
    # Floyd 알고리즘 수행
    dist, path = shortest_path_floyd(vertex, adj)

    while True:
        print('-'*70)
        print('vertex :',vertex)
        print()
        # 사용자 입력 받기
        start = input(f"Enter start vertex : ").strip()
        end = input(f"Enter end vertex : ").strip()
        print('-'*70)

        # 입력 검증
        if start not in vertex or end not in vertex:
            print("Wrong vertices. Please try again.")
            continue

        start_idx = vertex.index(start)
        end_idx = vertex.index(end)

        # 경로 존재 여부 확인
        if dist[start_idx][end_idx] == INF:
            print(f"No path exists between {start} and {end}.")
        else:
            # 경로 추적
            route = []
            while end_idx != -1:
                route.append(vertex[end_idx])
                end_idx = path[start_idx][end_idx]
            route.reverse()

            # 결과 출력
            print(f"Shortest path from {start} to {end}: {' -> '.join(route)}")
            print(f"Distance: {dist[start_idx][vertex.index(end)]}")
            print('-'*70)

            break


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수

    # 최단 거리 배열과 경로 추적 배열 초기화
    dist = [list(row) for row in adj]  # 거리 배열 복사
    path = [[-1 if adj[i][j] == INF or i == j else i for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]  # 경로 배열 갱신
        printA(dist)  # 진행 상황 출력

    return dist, path  # 최단 거리 배열과 경로 추적 배열 반환


if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
    weight = [ [0,	    7,		INF,	INF,	3,      10,		INF],
               [7,		0,	    4,		10,	    2,	    6,	    INF],
               [INF,	4,		0,	    2,		INF,	INF,	INF],
               [INF,	10,     2,		0,      11,		9,	    4   ],
               [3,	    2,	    INF,   11,		0,      13,		5   ],
               [10,		6,	    INF,	9,      13,		0,	    INF],
               [INF,    INF,	INF,   4,		5,		INF,	0   ]]    

    
    find_shortest_path(vertex, weight)
