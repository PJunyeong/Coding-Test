import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
s, e = map(int, sys.stdin.readline().rstrip().split())
for i in range(n+1): nodes[i].sort()
# 연결 그래프 세팅 -> DFS 탐색 위한 노드 순서 변경

def Dijkstra(visited, start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0
    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if next_node in visited: continue
            # 이미 산책한 경로 제외
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

distances = Dijkstra(set(), e)
first_cost = 0
cursor = s
visited = set()
while cursor != e:
    for  next_node, next_cost in nodes[cursor]:
        if first_cost + next_cost + distances[next_node] == distances[s]:
            first_cost += next_cost
            visited.add(next_node)
            cursor = next_node
            break
            # 알파벳 순서대로 탐색 -> 한 번 최단 경로 중 입력되면 곧바로 이동, visted에 기록

visited.remove(e)
# s/e는 재방문해야 함
distances = Dijkstra(visited, s)
print(first_cost + distances[e])