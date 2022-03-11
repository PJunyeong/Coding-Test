import sys
import heapq

t = int(sys.stdin.readline().rstrip())
INF = sys.maxsize
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().rstrip().split())
        nodes[b].append([a, s])

    def Dijkstra(start):
        distances = [INF for _ in range(n+1)]
        distances[start] = 0

        pq = []
        heapq.heappush(pq, [0, start])

        while pq:
            cur_cost, cur_node = heapq.heappop(pq)

            if distances[cur_node] < cur_cost: continue

            for next_node, next_cost in nodes[cur_node]:
                if distances[next_node] > next_cost + cur_cost:
                    distances[next_node] = next_cost + cur_cost
                    pq.append([cur_cost+next_cost, next_node])

        unaffected = 0
        local_max = 0

        for distance in distances[1:]:
            if distance == INF: unaffected += 1
            else:
                local_max = max(local_max, distance)

        print(n-unaffected, local_max)

    Dijkstra(c)


