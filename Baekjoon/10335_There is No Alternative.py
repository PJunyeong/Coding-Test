import sys
from collections import deque

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

def Kruskal(MST_check=False):
    if MST_check:
        total = 0
        edge_cnt = 0
        edges = []
        while pq2:
            cost, node1, node2 = pq2.popleft()
            if union(node1, node2):
                total += cost
                edge_cnt += 1
                edges.append([cost, node1, node2])
                if edge_cnt == n-1: break
        if edge_cnt == n-1: return edges, total
        else: return edges, -1
        # MST 형성 간선 집합 및 MST 비용 리턴
    else:
        total = 0
        edge_cnt = 0
        while pq2:
            cost, node1, node2 = pq2.popleft()
            if union(node1, node2):
                total += cost
                edge_cnt += 1
                if edge_cnt == n-1: break
        if edge_cnt == n-1: return total
        else: return -1
        # 특정 간선을 제외했을 때의 MST 비용 리턴

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    pq.append([c, a, b])
pq.sort()
pq = deque(pq)
pq2 = pq.copy()
# 원본 pq를 계속해서 활용해야 하므로 copy
parents = [i for i in range(n+1)]
MST_edges, total = Kruskal(MST_check=True)

no_alternative_cnt = 0
no_alternative_cost = 0
for edge in MST_edges:
    parents = [i for i in range(n+1)]
    pq2 = pq.copy()
    pq2.remove(edge)
    # edge가 alternative하다면 이 edge를 원본 그래프에서 지우고 MST를 구해도 동일한 MST 비용이 나올 것이다.
    total2 = Kruskal(MST_check=False)
    if total != total2:
        no_alternative_cnt += 1
        no_alternative_cost += edge[0]
print(no_alternative_cnt, no_alternative_cost)