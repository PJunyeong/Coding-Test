import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
INF = sys.maxsize
def Dijkstra(start):
    distances = [INF for _ in range(n+1)]
    path = [0 for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost+cur_cost:
                distances[next_node] = next_cost+cur_cost
                path[next_node] = cur_node
                heapq.heappush(pq, [cur_cost+next_cost, next_node])
    return path

path = Dijkstra(1)

result = set()

for i in range(2, n+1):
    cursor = i

    while cursor != 1:
        result.add(tuple((cursor, path[cursor])))
        cursor = path[cursor]

print(len(result))

for edge in result:
    a, b = edge
    print(a, b)