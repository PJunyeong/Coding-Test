import sys

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])

def B_F(start):
    # 벨만-포드 알고리즘
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    # 시작 노드 자기 자신에 대한 거리는 0으로 초기화

    for i in range(n):
        # 정점 개수만큼 반복
        for cur_node in range(1, n+1):
            for next_node, next_cost in nodes[cur_node]:
                if distances[next_node] > distances[cur_node] + next_cost and distances[cur_node] != INF:
                    # 업데이트 가능
                    if i == n-1: return -1
                    # 업데이트 가능하지만 n번째 반복 시 업데이트는 곧 음수 사이클이 존재함을 의미
                    distances[next_node] = distances[cur_node] + next_cost
    return distances
flag = B_F(1)
if flag == -1: print(-1)
else:
    distances = flag
    for i in range(2, n+1):
        if distances[i] == INF:
            print(-1)
            # 거리 무한은 곧 해당 노드에 대한 경로가 존재하지 않음을 의미
        else: print(distances[i])