import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
start, end = map(int, sys.stdin.readline().rstrip().split())

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
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances

distances_start = Dijkstra(start)
distances_end = Dijkstra(end)
distances_added = []
for idx, (s, e) in enumerate(zip(distances_start[1:], distances_end[1:]), start=1):
    if s == 0 or e == 0: continue
    distances_added.append((s+e, s, e, idx))
distances_added.sort()
if not distances_added: print(-1)
else:
    total = distances_added[0][0]
    answer_start = INF
    answer_idx = 0
    for case in distances_added:
        local_total, local_start, local_end, local_idx = case
        if total < local_total: break
        elif local_start > local_end: continue
        elif answer_start > local_start:
            answer_start = local_start
            answer_idx = local_idx
        elif answer_start == local_start and answer_idx > local_idx:
            answer_idx = local_idx

    if answer_idx == 0: print(-1)
    else: print(answer_idx)
