import sys
import heapq

INF = sys.maxsize
n = int(sys.stdin.readline().rstrip())
a, b, c = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[node1].append([node2, cost])
    nodes[node2].append([node1, cost])

def Dijsktra(start):
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
                heapq.heappush(pq, [next_cost + cur_cost, next_node])
    return distances

distances_a = Dijsktra(a)
distances_b = Dijsktra(b)
distances_c = Dijsktra(c)
distances = [INF for _ in range(n+1)]

for i in range(1, n+1):
    distances[i] = min(distances_a[i], distances_b[i], distances_c[i])
print(distances.index(max(distances[1:])))