import sys
import heapq
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = []
keys = []
edges = []
for i in range(n):
    line = list(sys.stdin.readline().rstrip())
    nodes.append(line)
    for j in range(n):
        if line[j] == 'S' or line[j] == 'K':
            keys.append([i, j])
            # MST 노드는 'S', 'K' 등 총 m+1개 노드, m개 간선

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(start_row, start_col, goal_row, goal_col):
    queue = deque()
    queue.append([start_row, start_col, 0])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start_row][start_col] = True

    while queue:
        cur_row, cur_col, cur_cost = queue.popleft()
        if cur_row == goal_row and cur_col == goal_col: return cur_cost

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

            if not visited[next_row][next_col] and nodes[next_row][next_col] != '1':
                visited[next_row][next_col] = True
                queue.append([next_row, next_col, cur_cost + 1])
    return -1

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


for i in range(m+1):
    for j in range(i+1, m+1):
        start_row, start_col = keys[i]
        goal_row, goal_col = keys[j]
        cost = BFS(start_row, start_col, goal_row, goal_col)
        # 키 ('S' 또는 'K') 페어 별 최단 거리를 BFS를 통해 구한다. -1은 연결할 수 없는 경우므로 연결 트리 자체 불가능
        if cost == -1:
            print(-1)
            exit(0)
        heapq.heappush(edges, [cost, i, j])


parents = [i for i in range(m+1)]

# 크루스칼 알고리즘
total = 0
edge_num = 0
while edges:
    cur_cost, node1, node2 = heapq.heappop(edges)

    if union(node1, node2):
        total += cur_cost
        edge_num += 1
        if edge_num == m: break

if edge_num == m: print(total)
else: print(-1)