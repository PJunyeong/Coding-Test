import sys
import heapq

INF = sys.maxsize
n, m, d, e = map(int, sys.stdin.readline().rstrip().split())
heights = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

def Dijkstra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if heights[cur_node] < heights[next_node] and distances[next_node] > cur_cost + next_cost:
                # 높이에 따라 이동 가능
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])

    return distances

dist_start = Dijkstra(1)
dist_goal = Dijkstra(n)
ans = -INF
for idx in range(2, n):
    d1, d2 = dist_start[idx], dist_goal[idx]
    # 집 -> idx (목표) -> 학교 이동 최소 거리
    if d1 == INF or d2 == INF: continue
    # INF면 이동 불가능한 목표
    ans = max(ans, heights[idx]*e - (d1 + d2) * d)

if ans == -INF: print("Impossible")
else: print(ans)