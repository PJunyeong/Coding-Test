import sys
import heapq

INF = sys.maxsize

n, m, x = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    tail, head, time = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append([head, time])

def Dijsktra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost+next_cost:
                distances[next_node] = cur_cost+next_cost
                heapq.heappush(pq, [cur_cost+next_cost, next_node])

    return distances

distances_x = Dijsktra(x)

for i in range(1, n+1):
    if i == x: continue
    distances_i = Dijsktra(i)
    distances_x[i] += distances_i[x]

print(max(distances_x[1:]))