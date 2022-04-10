import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
nodes = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    row, col = map(int, sys.stdin.readline().rstrip().split())
    nodes[row-1][col-1] = 1
l = int(sys.stdin.readline().rstrip())
time_rotate = []
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    x = int(x)
    time_rotate.append([x, c])

def next_pos(cur_row, cur_col, cur_dir):
    if cur_dir == 'E':
        return cur_row, cur_col + 1
    elif cur_dir == 'N':
        return cur_row - 1, cur_col
    elif cur_dir == 'W':
        return cur_row, cur_col - 1
    else:
        return cur_row + 1, cur_col
# 현재 방향으로 이동할 때 다음 좌표 리턴

def rotate(cur_dir, c):
    if c == 'L':
        if cur_dir == 'E': return 'N'
        elif cur_dir == 'N': return 'W'
        elif cur_dir == 'W': return 'S'
        else: return 'E'
    else:
        if cur_dir == 'E': return 'S'
        elif cur_dir == 'N': return 'E'
        elif cur_dir == 'W': return 'N'
        else: return 'W'
# 현재 방향 기준 좌우 변경 시 다음 방향 리턴

queue = deque()
queue.append([0, 0, 'E', 0])
visited = deque()
visited.append([0, 0])
# 현재 뱀이 위치한 모든 좌표를 visited로 표시

while queue:
    cur_row, cur_col, cur_dir, cur_time = queue.popleft()
    if cur_row < 0 or cur_col < 0 or cur_row >= n or cur_col >= n or nodes[cur_row][cur_col] == -1: break
    # 벽 또는 자신의 몸에 부딪힐 때까지 반복
    if nodes[cur_row][cur_col] == 0:
        tail_row, tail_col = visited.popleft()
        nodes[tail_row][tail_col] = 0
        # 사과가 아닐 때 꼬리를 비운다.
    nodes[cur_row][cur_col] = -1
    # 현재 위치 뱀의 머리 -1로 마킹
    visited.append([cur_row, cur_col])
    if time_rotate and cur_time == time_rotate[0][0]:
        c = time_rotate[0][1]
        time_rotate.remove([cur_time, c])
        cur_dir = rotate(cur_dir, c)
        # 방향 전환 시점에 방향 바꾸어 cur_dir에 반영
    next_row, next_col = next_pos(cur_row, cur_col, cur_dir)
    queue.append([next_row, next_col, cur_dir, cur_time + 1])

print(cur_time)