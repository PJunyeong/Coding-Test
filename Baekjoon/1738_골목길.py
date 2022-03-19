import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
edges = [[] for _ in range(n+1)]
INF = sys.maxsize
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    edges[u].append([v, w])

def Bellman_Ford(start):
    distances = [-INF for _ in range(n+1)]
    # 최장 거리를 업데이트하기 위해 음의 무한대로 거리 값 초기화
    distances[start] = 0
    path = [0 for _ in range(n+1)]

    for i in range(n):
        for cur_node in range(1, n+1):
            for next_node, next_cost in edges[cur_node]:
                if distances[cur_node] != -INF and distances[next_node] < next_cost + distances[cur_node]:
                    # 업데이트 가능할 때 업데이트
                    distances[next_node] = next_cost + distances[cur_node]
                    path[next_node] = cur_node
                    if i == n - 1: distances[next_node] = INF
                    # 사이클 존재한다면 해당 노드에 대한 거리 값 양의 무한대로 표시
    result = []
    cur_node = n
    if distances[n] == INF:
        # distances는 1번 노드에서 해당 노드로 가는 최대 비용. INF라면 사이클 존재한다는 뜻.
        print(-1)
        return
    while cur_node != 1:
        result.append(cur_node)
        cur_node = path[cur_node]
    result.append(cur_node)
    result = result[::-1]
    print(*result, sep=' ')
    # n번 -> 1번 거꾸로 가는 도중 사이클 없음이 distances[n] != INF를 통해 보장
    return

Bellman_Ford(1)