import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n+1)]
total = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    total += c
    heapq.heappush(pq, [c, a, b])

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
MST = 0
edge_cnt = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        MST += cur_cost
        edge_cnt += 1
        if edge_cnt == n-1: break
    # 크루스칼 알고리즘

if edge_cnt == n-1: print(total - MST)
else: print(-1)
