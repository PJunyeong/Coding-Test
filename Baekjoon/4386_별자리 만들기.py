import sys
import heapq

n = int(sys.stdin.readline().rstrip())
nodes = []
for _ in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    nodes.append([x, y])
pq = []
parents = [i for i in range(n)]
for i in range(n):
    x1, y1 = nodes[i]
    for j in range(i+1, n):
        x2, y2 = nodes[j]
        cost = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
        heapq.heappush(pq, [cost, i, j])

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
edge_cnt = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += cur_cost
        edge_cnt += 1
        if edge_cnt == n-1: break

print(total)

