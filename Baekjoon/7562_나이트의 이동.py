import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    cur_row, cur_col = map(int, sys.stdin.readline().rstrip().split())
    goal_row, goal_col = map(int, sys.stdin.readline().rstrip().split())

    visited = [[False for _ in range(n)] for _ in range(n)]
    moves_x = [1, 2, 2, 1, -1, -2, -2, -1]
    moves_y = [2, 1, -1, -2, -2, -1, 1, 2]
    queue = deque()
    queue.append([[cur_row, cur_col], 0])
    visited[cur_row][cur_col] = True

    while queue:
        pos, cur_cnt = queue.popleft()
        row, col = pos
        if row == goal_row and col == goal_col: break

        for x, y in zip(moves_x, moves_y):
            next_row, next_col = row + y, col + x

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append([[next_row, next_col], cur_cnt + 1])
    print(cur_cnt)