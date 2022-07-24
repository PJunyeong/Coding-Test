import sys
import heapq

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
INF = sys.maxsize
for _ in range(m):
    a, b, = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, 1])

def Dijkstra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

distances = Dijkstra(x)
cities = [city for city, distance in enumerate(distances) if distance == k]

if not cities: print(-1)
else: print(*cities, sep='\n')

