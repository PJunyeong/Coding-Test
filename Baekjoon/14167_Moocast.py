import sys
import heapq

n = int(sys.stdin.readline().rstrip())
positions = []
for idx in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    positions.append([x, y, idx])
parents = [i for i in range(n)]
pq = []

def get_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)

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

def Kruskal():
    edge_cnt = 0
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            edge_cnt += 1
            if edge_cnt == n-1: return cost
    return -1

for i in range(n):
    x1, y1, node1 = positions[i]
    for j in range(i+1, n):
        x2, y2, node2 = positions[j]
        cost = get_distance(x1, y1, x2, y2)
        heapq.heappush(pq, [cost, node1, node2])

answer = Kruskal()
print(answer)