import sys
import heapq
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
s, e = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n+1)]
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2, k = map(int, sys.stdin.readline().rstrip().split())
    nodes[node1].append([-k, node2])
    nodes[node2].append([-k, node1])

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

for cost, node in nodes[s]:
    heapq.heappush(pq, [cost, s, node])

edges = [[] for _ in range(n+1)]

while pq:
    cost, node1, node2 = heapq.heappop(pq)

    root1, root2 = find(node1), find(node2)

    if root1 == s and root2 != s:
        parents[root2] = root1
        next_node = node2
        edges[node1].append([node2, -cost])
        edges[node2].append([node1, -cost])
        if node1 == e or node2 == e: break
    elif root1 != s and root2 == s:
        parents[root1] = root2
        next_node = node1
        edges[node1].append([node2, -cost])
        edges[node2].append([node1, -cost])
        if node1 == e or node2 == e: break
    else: continue

    for cost, node in nodes[next_node]:
        heapq.heappush(pq, [cost, next_node, node])
    # s 연결 e까지 연결된 MST 생성

visited = [False for _ in range(n+1)]
queue = deque()
queue.append([s, sys.maxsize])
visited[s] = True
result = 0
while queue:
    cur_node, cur_min = queue.popleft()

    if cur_node == e: result = max(result, cur_min)

    for next_node, next_cost in edges[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            next_min = min(cur_min, next_cost)
            queue.append([next_node, next_min])
    # BFS로 s -> e까지 가는 간선을 통해 최소 cur_min 중 최댓값 result 뽑기

print(result)