import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m, b, k, q = map(int, sys.stdin.readline().rstrip().split())
# 총 (n+m+b) 개 노드, k 개 간선
nodes = [[] for _ in range(n+m+b+1)]
distances = [[INF for _ in range(n+m+b+1)] for _ in range(b+1)]
# 다리 별로 다익스트라를 만들기 위한 distances
for _ in range(k):
    node1, node2, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[node1].append([node2, cost])
    nodes[node2].append([node1, cost])

def Dijkstra(start):
    pq = []
    heapq.heappush(pq, [0, start])
    distances[start-n-m][start] = 0

    while pq:
        cur_cost, cur_node  = heapq.heappop(pq)

        if distances[start-n-m][cur_node] != cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[start-n-m][next_node] > next_cost + cur_cost:
                distances[start-n-m][next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

for bridge in range(n+m+1, n+m+b+1):
    Dijkstra(bridge)
    # 각 다리에 대해 다익스트라 알고리즘

for _ in range(q):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    answer = INF
    for bridge in range(n+m+1, n+m+b+1):
        answer = min(answer, distances[bridge-n-m][s] + distances[bridge-n-m][e])
        # 특정 다리를 시작점으로 사용했을 때 해당 다리 -> s, 해당 다리 -> e의 합이 s -> e까지 걸리는 거리
    if answer == INF: print(-1)
    else: print(answer)
