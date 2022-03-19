import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m, w = map(int, sys.stdin.readline().rstrip().split())
    INF = sys.maxsize
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        edges[s].append([e, t])
        edges[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().rstrip().split())
        edges[s].append([e, -t])

    def Bellman_Ford(start):
        distances = [INF for _ in range(n+1)]
        distances[start] = 0

        for i in range(n):
            for cur_node in range(1, n+1):
                for next_node, next_cost in edges[cur_node]:

                    if distances[next_node] > next_cost + distances[cur_node]:
                        if i == n-1: return True
                        # 음의 사이클 존재 O
                        distances[next_node] = next_cost + distances[cur_node]
        return False
        # 음의 사이클 존재 X
    if Bellman_Ford(1): print("YES")
    else: print("NO")
    # 어떤 시작점에서 출발하든 음의 사이클이 존재한다면 출발지 -> 도착지 -> 출발지 비용이 감소

