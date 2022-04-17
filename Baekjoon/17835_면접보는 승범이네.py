import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[b].append([a, c])
interviews = list(map(int, sys.stdin.readline().rstrip().split()))

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    pq = []
    for interview in interviews:
        heapq.heappush(pq, [0, interview])
        distances[interview] = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances

distances = Dijkstra()
dist = max(distances[1:])
print(distances.index(dist))
print(dist)

