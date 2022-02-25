from collections import deque

n, m = map(int, input().split())
nodes = [[] for _ in range(n)]
for i in range(n):
    nodes[i] += input()
for i in range(n):
    for j in range(m):
        nodes[i][j] = int(nodes[i][j])
# 그래프 (0, 0) -> (n-1, m-1)까지 이동하는 최단 경로 BFS로 파악하기
# 1이라면 이동 불가능, 하지만 이동 중 한 번은 무시하고 이동 가능.
# 경로 중 벽을 무너뜨린 적이 있는지 여부 확인 위해 visted 3차원 배열로 체크 (0은 무너뜨린 적 없음, 1은 한 번 무너뜨린 적 있음)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS():
    queue = deque()
    queue.append([0, 0, 0])
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    # 시작 위치 (0, 0)와 이 상태에서 벽을 무너뜨린 적 있는지 여부: 없으므로 0.
    # 시작 위치 포함이므로 visted[0][0][0]에는 0이 아니라 1을 준다.

    while queue:
        row, col, wall = queue.popleft()
        if row == n-1 and col == m-1: return visited[row][col][wall]

        for x, y in zip(dx, dy):
            next_row = row + x
            next_col = col + y

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue
            # 그래프 범위에서 다음 좌표가 벗어난다면 스킵한다.

            if nodes[next_row][next_col] == 0 and visited[next_row][next_col][wall] == 0:
                # 다음 좌표 이동 가능하고 탐색한 적이 없다면(visted 값이 0이면 탐색한 적이 없다는 뜻) 큐에 넣는다.
                visited[next_row][next_col][wall] = visited[row][col][wall] + 1
                queue.append([next_row, next_col, wall])
            if nodes[next_row][next_col] == 1 and wall == 0:
                # 벽이 있고 여태까지 벽을 부순 적이 없다면 벽을 부쉈다고 체크하고 큐에 넣는다.
                visited[next_row][next_col][1] = visited[row][col][wall] + 1
                queue.append([next_row, next_col, 1])
    return -1

print(BFS())
