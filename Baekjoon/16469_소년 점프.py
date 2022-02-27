from collections import deque

n, m = map(int, input().split())

nodes= [[] for _ in range(n)]

for i in range(n):
    nodes[i] += map(int, input())
    for j in range(m):
        if nodes[i][j] == 1: nodes[i][j] = -1
        # 장애물이 양수 1이면 점수 카운트에서 혼동되므로 -1로 변경한다.
# 그래프 구현

global_nodes = []

villains = [[] for _ in range(3)]

for i in range(3):
    row, col = map(int, input().split())
    row -= 1
    col -= 1
    villains[i].append(row)
    villains[i].append(col)
# 제로 인덱스 기반 빌런 시작 위치

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 오프셋

for villain in villains:
    start_row, start_col = villain
    queue = deque()
    local_nodes = [node[:] for node in nodes]
    queue.append([[start_row, start_col], 0])
    # 각 빌런이 BFS를 통해 시작 노드에서 탐색 가능한 모든 노드에 깊이를 기록한다.
    while queue:
        pos, score = queue.popleft()
        row, col = pos

        for x, y in zip(dx, dy):
            next_row = row + x
            next_col = col + y

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            if local_nodes[next_row][next_col] == 0:
                queue.append([[next_row, next_col], score+1])
                local_nodes[next_row][next_col] = score + 1

    for i in range(n):
        for j in range(m):
            if local_nodes[i][j] == 0:
                local_nodes[i][j] = -1
                # BFS이 끝나고 0으로 표시되어 있으면 갈 수 없다는 뜻이므로 -1로 마킹

    local_nodes[start_row][start_col] = 0
    # 시작 노드는 깊이가 0이므로 다시 한 번 재마킹
    global_nodes.append(local_nodes)
    # 이 빌런의 BFS 깊이 정보가 담긴 그래프를 기록한다.

total_scores = []

for i in range(n):
    for j in range(m):
        if global_nodes[0][i][j] >= 0 and global_nodes[1][i][j] >= 0 and global_nodes[2][i][j] >= 0:
            # 빌런 세 명 모두가 기록한 그래프 정보에 음수가 아니라면 탐색 가능한 노드
            total_scores.append(max(global_nodes[0][i][j], global_nodes[1][i][j], global_nodes[2][i][j]))
            # 특정 노드에서 움직이지 않고 있을 수 있기 때문에 그 노드에 도착하는 최댓값만 신경쓴다.

if not total_scores: print(-1)
else:
    total_scores.sort()
    min_score = total_scores[0]
    cnt = 0
    for score in total_scores:
        if score != min_score: break
        cnt += 1

    print(min_score)
    print(cnt)
