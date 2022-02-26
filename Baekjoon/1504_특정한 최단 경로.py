import heapq
import math

n, e = map(int, input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(e):
    head, tail, weight = map(int, input().split())
    nodes[head].append([tail, weight])
    nodes[tail].append([head, weight])
    # 무방향 그래프 구현

v1, v2 = map(int, input().split())
# v1, v2를 경유해야 함

INF = math.inf

def Dijkstra(start):
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if cur_cost > distances[cur_node]: continue

        for next_node, next_cost in nodes[cur_node]:
            if cur_cost + next_cost < distances[next_node]:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(queue, [next_cost+cur_cost, next_node])

    return distances


distances_start = Dijkstra(1)
distances_v1 = Dijkstra(v1)
distances_v2 = Dijkstra(v2)
# 노드 1, v1, v2에서 각각 다른 노드에 대한 거리를 다익스트라를 통해 구한다.

route1 = distances_start[v1] + distances_v1[v2] + distances_v2[n]
route2 = distances_start[v2] + distances_v2[v1] + distances_v1[n]
# 1번 노드에서 n번까지 v1, v2를 경유하는 방법은 1 -> v1 -> v2 -> n 또는 1 -> v2 -> v1 -> n이다.

result = min(route1, route2)
if result >= INF: print(-1)
# 경유할 수 없는 경로는 비용 합이 INF보다 클 것이다.
else: print(result)