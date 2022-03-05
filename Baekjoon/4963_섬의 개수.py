import sys
from collections import deque

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0: break
    nodes = [[] for _ in range(h)]
    for i in range(h):
        nodes[i] += list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = 0

    queue = deque()
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    # 대각선 포함 총 8방향으로 이동 가능
    for i in range(h):
        for j in range(w):
            if nodes[i][j] == 1:
                nodes[i][j] = 0
                queue.append([i, j])
                while queue:
                    row, col = queue.popleft()

                    for x, y in zip(dx, dy):
                        next_col, next_row = col + x, row + y
                        if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w: continue

                        if nodes[next_row][next_col] == 1:
                            queue.append([next_row, next_col])
                            nodes[next_row][next_col] = 0
                cnt += 1

    print(cnt)

