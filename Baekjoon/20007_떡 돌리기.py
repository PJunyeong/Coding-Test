import sys
import heapq

INF = sys.maxsize

n, m, x, y = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

def Dijkstra():
    distances = [INF for _ in range(n)]
    distances[y] = 0
    pq = []
    heapq.heappush(pq, [0, y])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances

distances = Dijkstra()
distances_idx = [[distance, idx] for idx, distance in enumerate(distances)]
distances_idx.sort()

if distances_idx[-1][0] * 2 > x: print(-1)
else:
    day = 1
    cur = 0
    for distance, idx in distances_idx:
        if cur + 2 * distance <= x:
            cur += 2 * distance
        else:
            day += 1
            cur = 2 * distance
    print(day)