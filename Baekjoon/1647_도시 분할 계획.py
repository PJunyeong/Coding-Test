import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
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

total = []

while pq:
    c, a, b = heapq.heappop(pq)

    if union(a, b):
        total.append(c)

print(sum(total[:-1]))
# 모든 노드를 연결한 최소 신장 트리의 각 간선 total에서 간선 하나를 제외하면 두 개의 분리된 마을이 생긴다.
# 마지막에 들어온 total[-1]을 제외해 마을을 분리하면 간선 비용의 최솟값을 얻을 수 있다.