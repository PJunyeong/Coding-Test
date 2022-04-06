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

def Dijkstra(node1, node2):
    distances = [INF for _ in range(n+1)]
    distances[1] = 0
    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if cur_node == node1 and next_node == node2: continue
            elif cur_node == node2 and next_node == node1: continue

            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

def path_construct():
    path = []
    visited = [False for _ in range(n+1)]
    visited[n] = True
    queue = deque()
    queue.append(n)

    while queue:
        cur_node = queue.popleft()
        path.append(cur_node)
        if cur_node == 1: break

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] + next_cost == distances[cur_node] and not visited[next_node]:
                # 양방향 그래프 -> 인접 노드까지 최단 거리 + 간선 비용 == 현재 노드까지 최단 거리라면 최단 거리 경로에 사용한 간선
                visited[next_node] = True
                queue.append(next_node)
    return path

distances = Dijkstra(-1, -1)
path = path_construct()

answer = 0
for i in range(len(path)-1):
    # 특정 간선 하나를 비활성화한 채로 다익스트라 알고리즘 사용. 최단 거리 중 최댓값 answer
    distances = Dijkstra(path[i], path[i+1])
    answer = max(answer, distances[n])
print(answer)