import sys
import heapq
from collections import deque

INF = sys.maxsize
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
nodes_inv = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes_inv[b].append([a, c])

start, end = map(int, sys.stdin.readline().rstrip().split())

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost+cur_cost, next_node])

    return distances

distances = Dijkstra()
edges = [[] for _ in range(n+1)]

def edge_find():
    queue = deque()
    queue.append(end)

    while queue:
        cur_node = queue.popleft()

        if cur_node == start: continue

        for post_node, post_cost in nodes_inv[cur_node]:
            if distances[post_node] + post_cost == distances[cur_node] and [cur_node, post_cost] not in edges[post_node]:
                edges[post_node].append([cur_node, post_cost])
                queue.append(post_node)

def path_find():
    queue = deque()
    queue.append(start)
    note = [0 for _ in range(n+1)]
    note[start] = start

    while queue:
        cur_node = queue.popleft()

        if cur_node == end: break

        for next_node, next_cost in edges[cur_node]:
            note[next_node] = cur_node
            queue.append(next_node)

    while cur_node != start:
        visited.append(cur_node)
        cur_node = note[cur_node]
    visited.append(cur_node)

visited = []
edge_find()
path_find()
visited.reverse()

print(distances[end])
print(len(visited))
print(*visited, sep=' ')

