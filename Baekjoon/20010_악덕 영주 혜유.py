import sys
import heapq

INF = sys.maxsize
n, k = map(int, sys.stdin.readline().rstrip().split())
pq = []
for _ in range(k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(pq, [c, a, b])

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1 ,root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

def Dijkstra(nodes, start):
    distances = [INF for _ in range(n)]
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

def Kruskal():
    total = 0
    nodes = [[] for _ in range(n)]
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            nodes[node1].append([node2, cost])
            nodes[node2].append([node1, cost])
            total += cost
    print(total)
    # 크루스칼 알고리즘을 통해 MST 구한다. MST에 사용한 간선을 nodes에 기록한다.
    local_max = 0
    for i in range(n):
        distances = Dijkstra(nodes, i)
        local_max = max(local_max, max(distances))
        # nodes를 통해 각 노드에서 다른 모든 노드에 대한 최단 거리를 다익스트라 알고리즘을 통해 구한다.
        # 최댓값을 local_max에 갱신한다.
    print(local_max)


parents = [i for i in range(n)]
Kruskal()

