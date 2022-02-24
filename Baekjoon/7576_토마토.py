from collections import deque

m, n = map(int, input().split())
nodes = [[] for _ in range(n)]
for i in range(n):
    nodes[i] = list(map(int, input().split()))
# 이차원 리스트로 그래프 표현

day = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque([])

for i in range(n):
    for j in range(m):
        if nodes[i][j] == 1:
            queue.append([[i, j], day])
            # 초기 상태에서 '익은', 즉 이동 가능한 노드를 큐에 넣는다.

while queue:
    pos, day = queue.popleft()
    row, col = pos
    for x, y in zip(dx, dy):
        next_row, next_col = row+x, col+y
        if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1: continue
        # 현재 이동 가능 노드에서 상하좌우 이동했을 때 유효한 노드
        if nodes[next_row][next_col] == 0:
            # 방문한 적이 없다면 방문하고 이때 날짜까지 구하자.
            nodes[next_row][next_col] = 1
            queue.append([[next_row, next_col], day+1])

reachable = True
for i in range(n):
    for j in range(m):
        if nodes[i][j] == 0:
            # BFS 이후 0이 남아 있다면 처음 상태 주어진 노드에서 탐색할 수 없다는 뜻이다.
            reachable = False
            break

if not reachable: print(-1)
else: print(day)
