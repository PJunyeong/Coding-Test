import sys
import heapq

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1,node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True
def Kruskal():
    total = 0
    edge_cnt = 0
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            total += cost
            edge_cnt += 1
            if edge_cnt == n*m-1: return total


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    pq = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(m-1):
            heapq.heappush(pq, [line[j], i*m+j, i*m+j+1])
    for i in range(n-1):
        line = list(map(int, sys.stdin.readline().rstrip().split()))
        for j in range(m):
            heapq.heappush(pq, [line[j], i*m+j, (i+1)*m+j])
    parents = [i for i in range(n*m)]
    total = 0
    edge_cnt = 0
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            total += cost
            edge_cnt += 1
            if edge_cnt == n * m - 1: break
    print(total)




