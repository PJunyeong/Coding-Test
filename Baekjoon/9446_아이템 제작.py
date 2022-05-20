import sys
import heapq

pq = []
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
costs = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, n+1):
    heapq.heappush(pq, [costs[i], i])
for _ in range(m):
    made, used1, used2 = map(int, sys.stdin.readline().rstrip().split())
    nodes[used1].append([used2, made])
    nodes[used2].append([used1, made])

def Dijkstra():
    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if costs[cur_node] < cur_cost: continue

        for next_used, next_made in nodes[cur_node]:
            if costs[next_made] > cur_cost + costs[next_used]:
                costs[next_made] = cur_cost + costs[next_used]
                heapq.heappush(pq, [cur_cost + costs[next_used], next_made])

Dijkstra()
print(costs[1])