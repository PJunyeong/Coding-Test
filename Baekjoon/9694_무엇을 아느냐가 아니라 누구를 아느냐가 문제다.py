import sys
import heapq
from collections import deque

INF = sys.maxsize
t = int(sys.stdin.readline().rstrip())
for t_num in range(1, t+1):
    m, n = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        nodes[a].append([b, c])
        nodes[b].append([a, c])

    def Dijsktra():
        distances = [INF for _ in range(n)]
        distances[0] = 0
        pq = []
        heapq.heappush(pq, [0, 0])
        note = [-1 for _ in range(n)]
        note[0] = 0

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)

            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if distances[next_node] > next_cost + cur_cost:
                    distances[next_node] = next_cost + cur_cost
                    note[next_node] = cur_node
                    heapq.heappush(pq, [next_cost + cur_cost, next_node])

        return distances, note

    def path_find():
        result = []
        cursor = n-1
        while cursor != 0:
            result.append(cursor)
            cursor = note[cursor]
        result.append(cursor)
        result.reverse()
        return result



    distances, note = Dijsktra()
    if distances[n-1] == INF: result = [-1]
    else: result = path_find()

    print(f"Case #{t_num}:", end=' ')
    print(*result, sep=' ')


