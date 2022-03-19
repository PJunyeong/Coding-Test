import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
visible = list(map(int, sys.stdin.readline().rstrip().split()))
INF = sys.maxsize
nodes= [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, t])
    nodes[b].append([a, t])

def Dijkstra():
    distances = [INF for _ in range(n)]
    distances[0] = 0
    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if next_node != n-1:
                if visible[next_node] == 0 and distances[next_node] > next_cost + cur_cost:
                    distances[next_node] = next_cost + cur_cost
                    heapq.heappush(pq, [next_cost + cur_cost, next_node])
            else:
                if distances[next_node] > next_cost + cur_cost:
                    distances[next_node] = next_cost + cur_cost
                    heapq.heappush(pq, [next_cost + cur_cost, next_node])

    if distances[n-1] == INF: return -1
    else: return distances[n-1]

print(Dijkstra())


