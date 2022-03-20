import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n+1)]

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

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    union(a, b)
for i in range(1, n+1):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    if i == 1: continue
    # 본사 컴퓨터 1번 노드를 제외한 MST를 만들기 위함
    for j in range(i+1, n+1):
        heapq.heappush(pq, [line[j-1], i, j])

MST = 0
edge_cnt = 0
result = []
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        MST += cur_cost
        edge_cnt += 1
        result.append([node1, node2])
        if edge_cnt == n-1: break
    # 크루스칼 알고리즘

print(MST, len(result))
for node1, node2 in result:
    print(node1, node2)