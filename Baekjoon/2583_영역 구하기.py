import sys
from collections import deque

row, col, k = map(int, sys.stdin.readline().rstrip().split())
boxes = []

for _ in range(k):
    boxes.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[False for _ in range(col)] for _ in range(row)]

for box in boxes:
    x1, y1, x2, y2 = box
    for x in range(x1, x2):
        for y in range(y1, y2):
            visited[y][x] = True
# 갈 수 없는 부분을 True로 마킹

queue = deque()
box_size = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(row):
    for j in range(col):
        # 모든 탐색 가능한 시작 노드를 찾는다.
        if not visited[i][j]:
            # 공간이 있다면
            queue.append([i, j])
            visited[i][j] = True
            size = 0
            while queue:
                cur_row, cur_col = queue.popleft()
                size += 1
                for x, y in zip(dx, dy):
                    next_row, next_col = cur_row + x, cur_col + y

                    if next_row < 0 or next_col < 0 or next_row >= row or next_col >= col: continue
                    if not visited[next_row][next_col]:
                        queue.append([next_row, next_col])
                        visited[next_row][next_col] = True
                        # 탐색 부분을 마킹하고 큐에 넣는다. 즉 [i, j]에서 탐색했을 때 이 부분은 갈 수 있다.
            box_size.append(size)

print(len(box_size))
box_size.sort()
print(*box_size, sep=' ')


