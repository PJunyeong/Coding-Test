import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]
pq = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(pq, [c, a, b])

for node, cost in enumerate(list(map(int, sys.stdin.readline().rstrip().split())), start=1):
    heapq.heappush(pq, [cost, 0, node])
    # 비상탈출구를 하나의 노드로 생각한다.

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

total = 0
edge_cnt = 0
while pq:
    cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += cost
        edge_cnt += 1
        if edge_cnt == n: break
        # n개의 노드 + 비상탈출구 노드 = n+1-1, 즉 n개의 간선이 추가되면 MST를 구할 수 있다.
print(total)

