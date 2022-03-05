import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().rstrip().split())
nodes = [[[] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        nodes[i][j] += list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if nodes[i][j][k] == 1:
                queue.append([[i, j, k], 0])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# z축까지 넣어 위아래 이동 가능

while queue:
    pos, cost = queue.popleft()
    height, row, col = pos

    for x, y, z in zip(dx, dy, dz):
        next_height = height + z
        next_row = row + y
        next_col = col + x

        if next_row < 0 or next_col < 0 or next_height < 0 or next_row >= n or next_col >= m or next_height >= h: continue

        if nodes[next_height][next_row][next_col] == 0:
            queue.append([[next_height, next_row, next_col], cost+1])
            nodes[next_height][next_row][next_col] = cost+1

reachable = True
local_max = 0
for i in range(h):
    for j in range(n):
        if 0 in nodes[i][j]:
            reachable = False
            break
        local_max = max(local_max, max(nodes[i][j]))

if not reachable: print(-1)
# 0이 발견된다면 익지 않은 토마토가 존재
elif local_max == 1: print(0)
# 초깃값 1만 발견된다면 처음부터 모두 익은 상태
else: print(local_max)