import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n)]

for i in range(n):
    nodes[i] += sys.stdin.readline().rstrip()

nodes2 = [node[:] for node in nodes]
for i in range(n):
    for j in range(n):
        if nodes2[i][j] == 'G':
            nodes2[i][j] = 'R'
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(nodes):
    cnt = 0
    queue = deque()

    for i in range(n):
        for j in range(n):
            if nodes[i][j] != 'V':
                queue.append([i, j])
                base_color = nodes[i][j]
                nodes[i][j] = 'V'
                # visited의 V로 체크하고 이 큐에서 확인할 경계의 색깔을 정한다.
                while queue:
                    row, col = queue.popleft()

                    for x, y in zip(dx, dy):
                        next_row, next_col = row + x, col + y

                        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

                        if nodes[next_row][next_col] == base_color:
                            nodes[next_row][next_col] = 'V'
                            queue.append([next_row, next_col])
                cnt += 1
    return cnt




for local_nodes in (nodes, nodes2):
    print(BFS(local_nodes), end=' ')