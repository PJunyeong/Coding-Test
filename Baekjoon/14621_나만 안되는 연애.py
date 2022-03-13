import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
uni = ['X'] + list(sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]
pq = []
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().rstrip().split())
    if uni[u] == uni[v]: continue
    heapq.heappush(pq, [d, u, v])

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

total = 0
cnt = 0

while pq:
    c, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += c
        cnt += 1
        if cnt == n-1: break

if cnt == n-1: print(total)
else: print(-1)



