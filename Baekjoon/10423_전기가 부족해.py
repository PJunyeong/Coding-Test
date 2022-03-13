import sys
import heapq

n, m, k = map(int, sys.stdin.readline().rstrip().split())
plants = list(map(int, sys.stdin.readline().rstrip().split()))
parents = [i for i in range(n+1)]
pq = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(pq, [w, u, v])

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        if root1 in plants and root2 in plants: return False
        elif root1 not in plants and root2 in plants:
            parents[root1] = root2
            return True
        elif root2 not in plants and root1 in plants:
            parents[root2] = root1
            return True
        else:
            parents[root1] = root2
            return True



total = 0

while pq:
    w, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += w

print(total)



