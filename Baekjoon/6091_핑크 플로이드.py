import sys
import heapq

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

n = int(sys.stdin.readline().rstrip())
parents = [i for i in range(n+1)]
pq = []
for i in range(1, n+1):
    adj = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, adj_item in zip(range(i+1, n+1), adj):
        heapq.heappush(pq, [adj_item, i, j])
nodes = [[] for _ in range(n+1)]

while pq:
    cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        nodes[node1].append(node2)
        nodes[node2].append(node1)

for adj in nodes[1:]:
    print(len(adj), *(sorted(adj)), sep=' ')
