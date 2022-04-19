import sys
from collections import deque

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

def Kruskal(mid):
    pq = sorted(edges, key=lambda x:(x[2]+x[3]*mid))
    # 우선순위 큐로 cost + time * x 오름차순 정렬
    total = 0
    for edge in pq:
        node1, node2, cost, time = edge
        if union(node1, node2):
            total += (cost + time * mid)
    if total <= f: return True
    # f보다 작다면 이득이 양수
    else: return False


n, m, f = map(int, sys.stdin.readline().rstrip().split())
edges = deque()
for _ in range(m):
    a, b, c, t = map(int, sys.stdin.readline().rstrip().split())
    edges.append([a, b, c, t])

left, right = 0, sys.maxsize
for _ in range(500):
    parents = [i for i in range(n+1)]
    mid = (left + right) / 2
    # 이득 x = (f-total cost) / total time
    # f = x * total time + total cost
    if Kruskal(mid):
        left = mid
    else:
        right = mid

if mid < 0: print("0.0000")
else: print(f"{mid:.4f}")