import sys
import heapq
from collections import deque

v, e, p = map(int, sys.stdin.readline().rstrip().split())
nodes= [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
INF = sys.maxsize
def Dijkstra():
    distances = [INF for _ in range(v+1)]
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

def BFS():
    queue = deque()
    queue.append(v)

    while queue:
        cur_node = queue.popleft()
        if cur_node == p: return True

        for post_node, post_cost in nodes[cur_node]:
            if distances[post_node] + post_cost == distances[cur_node]:
                queue.append(post_node)
    return False

distances = Dijkstra()
if BFS(): print("SAVE HIM")
else: print("GOOD BYE")