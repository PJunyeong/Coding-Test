import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
x, y, z = map(int, sys.stdin.readline().rstrip().split())

def Dijkstra(start, y_active= True):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    if y_active:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if distances[next_node] > cur_cost + next_cost:
                    distances[next_node] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_node])
    else:
        while pq:
            cur_cost, cur_node = heapq.heappop(pq)
            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if next_node == y: continue
                if distances[next_node] > cur_cost + next_cost:
                    distances[next_node] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances

distances_1 = Dijkstra(start=x, y_active=True)
distances_2 = Dijkstra(start=y, y_active=True)
distances_3 = Dijkstra(start=x, y_active=False)

answer1 = distances_1[y] + distances_2[z]
answer2 = distances_3[z]

if answer1 >= INF: print(-1, end= ' ')
else: print(answer1, end=' ')

if answer2 == INF: print(-1)
else: print(answer2)