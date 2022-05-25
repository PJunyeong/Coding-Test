import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]
for i in range(n): nodes[i] = list(map(int, sys.stdin.readline().rstrip().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(row, col):
    queue = deque()
    queue.append([row, col])
    visited[row][col] = True
    # 입력받은 좌표를 시작점으로 카운트

    while queue:
        cur_row, cur_col = queue.popleft()

        num = 0
        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m : continue

            if not visited[next_row][next_col] and nodes[next_row][next_col] == 0: num += 1
            # 방문한 적이 없는 (=빙하만 방문하고 있기 때문에, 현 방문으로 인해 '녹은' 곳은 카운트 X) 물 개수
            if not visited[next_row][next_col] and nodes[next_row][next_col] != 0:
                visited[next_row][next_col] = True
                queue.append([next_row, next_col])

        if nodes[cur_row][cur_col] - num <= 0:
            nodes[cur_row][cur_col] = 0
        else:
            nodes[cur_row][cur_col] -= num
        # 인접 0의 개수만큼 감산

day = 0
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    # 방문 체크. BFS를 통해 확인할 빙하, 연결성 등을 고려하기 위해 매번 갱신
    flag = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and nodes[i][j] != 0:
                flag += 1
                if flag > 1: break
                # 모든 빙하(값이 0이 아닌 위치)가 연결되어 있어야 함
                BFS(i, j)
        if flag > 1: break

    if flag > 1: break
    elif flag == 0:
        # 분리되지 않고 녹았을 때 0으로 기록
        day = 0
        break
    # WHILE 루프를 돌 수 있는 조건은 flag == 1일 경우
    day += 1
print(day)