import heapq
import sys

t_case = int(sys.stdin.readline().rstrip())
INF = int(1e9)
for _ in range(t_case):
    n, m, t = map(int, sys.stdin.readline().rstrip().split())
    s, g, h = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(n+1)]
    goals = []
    for _ in range(m):
        tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
        nodes[tail].append([head, cost])
        nodes[head].append([tail, cost])
        # 양방향 그래프 구현
    for _ in range(t):
        goals.append(int(sys.stdin.readline().rstrip()))

    def dijkstra(start):
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
                    heapq.heappush(pq, [cur_cost+next_cost, next_node])
        return distances

    distances_s = dijkstra(s)
    distances_g = dijkstra(g)
    distances_h = dijkstra(h)

    s_to_g = distances_s[g]
    s_to_h = distances_s[h]
    g_to_h = distances_g[h]
    h_to_g = distances_h[g]

    result = []
    for goal in goals:
        # s -> g, g -> h, h -> goal
        # s -> h, h -> g, g -> goal
        # g-h 간선을 사용해 해당 goal에 도착한 거리가 s->goal까지의 최단 거리와 같다면 goal까지 가는 데 g-h를 사용하였음
        if distances_s[goal] == s_to_g + g_to_h + distances_h[goal]:
            result.append(goal)
        elif distances_s[goal] == s_to_h + h_to_g + distances_g[goal]:
            result.append(goal)

    result.sort()
    print(*result, sep=' ')


