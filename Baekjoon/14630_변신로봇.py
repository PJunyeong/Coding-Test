import sys
import heapq

INF = sys.maxsize

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
costs = [0]
for _ in range(n): costs.append(sys.stdin.readline().rstrip())
start, end = map(int, sys.stdin.readline().rstrip().split())


for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = 0
        for c1, c2 in zip(costs[i], costs[j]):
            cost += (int(c1)-int(c2))**2
        nodes[i].append([j, cost])
        nodes[j].append([i, cost])

def Dijkstra():
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
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances[end]

answer = Dijkstra()
print(answer)