import sys
import heapq

n = int(sys.stdin.readline().rstrip())
nodes = []
parents = [i for i in range(n)]
pq = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(i+1, n):
        heapq.heappush(pq, [row[j], i, j])
        # c는 i -> j 연결 비용

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
planet_cnt = 0
while pq:
    c, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += c
        planet_cnt += 1
        if planet_cnt == n-1: break

print(total)



