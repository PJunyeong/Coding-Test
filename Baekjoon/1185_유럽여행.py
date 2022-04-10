import sys
import heapq

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1,node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True
def Kruskal():
    total = 0
    edge_cnt = 0
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            total += cost
            edge_cnt += 1
            if edge_cnt == n-1: return total

n, m = map(int, sys.stdin.readline().rstrip().split())
costs = [0]
for _ in range(n): costs.append(int(sys.stdin.readline().rstrip()))
pq = []
parents = [i for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    cost = 2*c + costs[a] + costs[b]
    heapq.heappush(pq, [cost, a, b])
    # 출발 노드 -> 간선 이용 -> 도착 노드 -> 간선 이용: 비용 재계산

answer = min(costs[1:]) + Kruskal()
# 출발 노드는 체류 비용이 가장 적은 노드
print(answer)

