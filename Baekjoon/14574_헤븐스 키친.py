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

def get_rate(node1, node2):
    p1, c1 = info[node1]
    p2, c2 = info[node2]
    rate = int((c1+c2)/abs(p1-p2))
    return rate

def DFS(cur_node):
    visited[cur_node] = True
    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            DFS(next_node)
            print(cur_node, next_node)


n = int(sys.stdin.readline().rstrip())
parents = [i for i in range(n+1)]
info = [[0, 0]]
pq = []
nodes = [[] for _ in range(n+1)]
for _ in range(n):
    p, c = map(int, sys.stdin.readline().rstrip().split())
    info.append([p, c])
for i in range(1, n+1):
    for j in range(i+1, n+1):
        heapq.heappush(pq, [-get_rate(i, j), i, j])

total = 0
while pq:
    cost, node1, node2= heapq.heappop(pq)
    if union(node1, node2):
        total += cost
        nodes[node1].append(node2)
        nodes[node2].append(node1)
        # 최대 신장 트리를 구하며 인접 리스트 구성

print(-total)
visited = [False for _ in range(n+1)]
DFS(1)
# 모든 노드가 연결되어 있으므로 각 노드 간 리프 노드 / 루트 노드 구별 가능
# 루트 : 리프 = 패자 : 승자

