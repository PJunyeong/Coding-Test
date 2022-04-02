import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
edges = []

for i in range(1, m+1):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    edges.append([i, node1, node2])

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

answers = [0 for _ in range(k)]
for i in range(k):
    total = 0
    edge_cnt = 0
    parents = [i for i in range(n + 1)]
    for edge in edges[i:]:
        cost, node1, node2 = edge
        if union(node1, node2):
            total += cost
            edge_cnt += 1
            if edge_cnt == n-1: break
    if edge_cnt == n-1: answers[i] = total
    else: break

print(*answers)
