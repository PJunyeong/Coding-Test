import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, t])
    nodes[b].append([a, t])

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    distances[1] = 0

    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost+cur_cost, next_node])

    return distances

distances = Dijkstra()
edges = set()

def BFS():
    queue = deque()
    queue.append(n)

    while queue:
        cur_node = queue.popleft()

        if cur_node == 1: continue

        for post_node, post_cost in nodes[cur_node]:
            if distances[post_node] + post_cost == distances[cur_node] and tuple((post_node, cur_node, post_cost)) not in edges:
                edges.add(tuple((post_node, cur_node, post_cost)))
                queue.append(post_node)

BFS()

original = distances[n]
local_diff = 0
for edge in edges:
    a, b, t = edge
    nodes[a].remove([b, t])
    nodes[b].remove([a, t])
    distances = Dijkstra()
    if distances[n] == INF: break
    local_diff = max(local_diff, distances[n]-original)
    nodes[a].append([b, t])
    nodes[b].append([a, t])

if distances[n] == INF: print(-1)
else: print(local_diff)