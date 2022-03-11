import sys
import heapq

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
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

total = 0

while pq:
    c, a, b = heapq.heappop(pq)

    if union(a, b):
        total += c

print(total)