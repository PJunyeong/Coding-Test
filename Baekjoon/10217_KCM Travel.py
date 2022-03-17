import sys
from collections import deque
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(n+1)]
    for _ in range(k):
        u, v, c, d = map(int, sys.stdin.readline().rstrip().split())
        nodes[u].append([v, c, d])

    def Dijkstra():
        INF = sys.maxsize
        distances = [[INF for _ in range(m+1)] for _ in range(n+1)]
        distances[1][0] = 0

        pq = deque()
        pq.append([0, 0, 1])

        while pq:
            cur_time, cur_cost, cur_node = pq.popleft()

            if distances[cur_node][cur_cost] < cur_time: continue
            elif distances[cur_node][cur_cost] == INF: continue

            for next_node, next_cost, next_time in nodes[cur_node]:
                if cur_cost + next_cost > m: continue

                if distances[next_node][cur_cost+next_cost] > next_time + cur_time:
                    distances[next_node][cur_cost+next_cost] = next_time + cur_time
                    pq.append([next_time + cur_time, cur_cost + next_cost, next_node])
        ans = min(distances[n])
        if ans == INF: print("Poor KCM")
        else: print(ans)

    Dijkstra()