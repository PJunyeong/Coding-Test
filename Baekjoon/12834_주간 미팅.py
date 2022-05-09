import sys
import heapq

INF = sys.maxsize
n, v, e = map(int, sys.stdin.readline().rstrip().split())
a, b = map(int, sys.stdin.readline().rstrip().split())
position = list(map(int, sys.stdin.readline().rstrip().split()))
nodes = [[] for _ in range(v+1)]
for _ in range(e):
    node1, node2, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[node1].append([node2, cost])
    nodes[node2].append([node1, cost])

def Dijkstra(start):
    distances = [INF for _ in range(v+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])
    return distances

distances_a = Dijkstra(a)
distances_b = Dijkstra(b)
total = 0

for pos in position:
    dist_a = distances_a[pos]
    dist_b = distances_b[pos]
    if dist_a == INF: total -= 1
    else: total += dist_a
    if dist_b == INF: total -= 1
    else: total += dist_b

print(total)
