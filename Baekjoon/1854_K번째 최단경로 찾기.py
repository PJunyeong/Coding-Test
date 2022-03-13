import sys
import heapq

n, m, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
INF = sys.maxsize
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])

def Dijkstra():
    distances=[[INF for _ in range(k)] for _ in range(n+1)]
    pq = []
    heapq.heappush(pq, [0, 1])
    distances[1][0] = 0
    # 시작 노드의 자기 자신을 향한 0번째 최단 거리는 언제나 0.
    # 업데이트하면서 k번째 최단 경로를 찾는다.

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node][k-1] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node][k-1] > next_cost + cur_cost:
                # 더 짧은 경로로 업데이트 가능하다면 업데이트.
                distances[next_node][k-1] = next_cost + cur_cost
                distances[next_node].sort()
                # idx번에 대한 거리가 짧은 순서대로 기록되어 있다.
                # 업데이트시켜줄 때마다 오름차순으로 정렬해주어야 한다.
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

distances = Dijkstra()

for i in range(1, n+1):
    if distances[i][k-1] == INF: print(-1)
    else: print(distances[i][k-1])

