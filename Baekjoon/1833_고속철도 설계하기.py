import sys
import heapq

n = int(sys.stdin.readline().rstrip())
parents = [i for i in range(n)]
pq = []

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

total = 0
edge_set = set()
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(i+1, n):
        if line[j] < 0:
            union(i, j)
            total -= line[j]
            edge_set.add(i)
            edge_set.add(j)
        else:
            heapq.heappush(pq, [line[j], i, j])
edges = []
while pq:
    cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += cost
        edges.append([node1, node2])
        edge_set.add(node1)
        edge_set.add(node2)
        if len(edge_set) == n: break
        # edge_cnt가 아니라 edge_set으로 전체 노드가 MST에 포함되었는지 확인
        # 실제 구성되는 간선 개수는 노드 개수 - 1이 아닐 수 있기 떄문

print(total, len(edges))
for node1, node2 in edges: print(node1+1, node2+1)
