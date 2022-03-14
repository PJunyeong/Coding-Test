import sys
from collections import deque

w, h = map(int, sys.stdin.readline().rstrip().split())
nodes = []
pos_c = []
for _ in range(h):
    nodes.append(list(sys.stdin.readline().rstrip()))
for i in range(h):
    for j in range(w):
        if nodes[i][j] == 'C':
            pos_c.append([i, j])

queue = deque()
INF = sys.maxsize
visited = [[INF for _ in range(w)] for _ in range(h)]

start_row, start_col = pos_c.pop()
end_row, end_col = pos_c.pop()

visited[start_row][start_col] = 0
queue.append([start_row, start_col, 0, 0])
queue.append([start_row, start_col, 0, 1])
queue.append([start_row, start_col, 0, 2])
queue.append([start_row, start_col, 0, 3])
dir_index = [0, 1, 2, 3]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 동 서 북 남
# 0, 1, 2, 3
local_min = INF
while queue:
    cur_row, cur_col, cur_cnt, cur_dir = queue.popleft()

    if cur_row == end_row and cur_col == end_col:
        local_min = min(local_min, cur_cnt)

    for dir_idx, x, y in zip(dir_index, dx, dy):
        next_col, next_row = x + cur_col, y + cur_row
        next_cnt = cur_cnt

        if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w or nodes[next_row][next_col] == '*': continue

        if cur_dir != dir_idx: next_cnt += 1
        # 현재 방향과 다르게 틀기 위해서는 거울이 하나 더 필요하다.

        if visited[next_row][next_col] >= next_cnt:
            # 거울을 더 많이 썼다면 방문 불가능. 즉 같은 개수의 거울을 사용할 때까지는 같은 노드를 재방문 가능
            visited[next_row][next_col] = next_cnt
            queue.append([next_row, next_col, next_cnt, dir_idx])

print(local_min)

