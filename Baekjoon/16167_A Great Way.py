import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
inv_nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split())
    if e > 10:
        cost = c + (e-10) * d
    else:
        cost = c
    nodes[a].append([b, cost])
    inv_nodes[b].append([a, cost])

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    distances[1] = 0
    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])

    return distances

def BFS():
    queue = deque()
    queue.append([n, 1])
    visited = [False for _ in range(n+1)]
    visited[n] = True
    answer = INF

    while queue:
        cur_node, cur_cost = queue.popleft()
        if cur_node == 1: answer = min(answer, cur_cost)

        for pre_node, pre_cost in inv_nodes[cur_node]:
            if distances[pre_node] + pre_cost == distances[cur_node] and not visited[pre_node]:
                queue.append([pre_node, cur_cost + 1])
                visited[pre_node] = True
    return answer

distances = Dijkstra()
if distances[n] == INF: print("It is not a great way.")
else: print(distances[n], BFS())



