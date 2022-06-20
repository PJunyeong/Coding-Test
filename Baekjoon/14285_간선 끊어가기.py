import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
edges = []
total = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
    edges.append([a, b])
    total += c
s, t = map(int, sys.stdin.readline().rstrip().split())

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

distances_s = Dijkstra(s)
distances_t = Dijkstra(t)
min_cost = INF
for a, b in edges:
    min_cost = min(min_cost, distances_s[a] + distances_t[b], distances_t[a] + distances_s[b])
    # a-b 간선. s -> a ... b <- t / s -> b ... a <- t 중 최솟값이 리턴
    # 전체 비용에서 이 연결 최솟값을 제거한 값이 곧 제거 가능 최댓값

print(total - min_cost)
# total - (total - min_cost) = min_cost를 제외한 나머지 모든 간선을 제외할 때 "지운 간선 가중치 합이 최대"가 된다.
# 1. s - t 연결 간선 제외 모두 제거 2. 연결 간선 중 비용이 가장 큰 간선 제거



