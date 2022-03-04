import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes  = [[] for _ in range(n)]

walls = []
virus = []

for i in range(n):
    nodes[i] += list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(m):
        if nodes[i][j] == 0:
            walls.append([i, j])
            # 벽을 세울 수 있는 공간
        elif nodes[i][j] == 2:
            virus.append([i, j])
# 그래프 구현

total = (n)*(m)
wall_cnt = total - len(walls) - len(virus) + 3
# 벽의 전체 개수는 변하지 않는다. 3개 세울 것이기 때문에 더해준다.
virus_cnt = len(virus)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 오프셋

wall_cases = list(combinations(walls, 3))
result = 0
queue = deque()

for wall_case in wall_cases:
    local_nodes = [node[:] for node in nodes]
    for wall_row, wall_col in wall_case:
        local_nodes[wall_row][wall_col] = 1
    # 만들 수 있는 벽을 3개 세우고 바이러스를 전파시킨다.
    for virus_row, virus_col in virus:
        queue.append([virus_row, virus_col])
    local_virus_cnt = virus_cnt
    # 바이러스는 위치 및 초기 개수는 언제나 같다.

    while queue:
        row, col = queue.popleft()

        for x, y in zip(dx, dy):
            next_row, next_col = row + x, col + y
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            if local_nodes[next_row][next_col] == 0:
                # 전파 가능 노드가 0일 때에만 전파될 수 있다.
                local_nodes[next_row][next_col] = 2
                local_virus_cnt += 1
                # 전파될 때마다 1씩 카운트하면서 이 로컬 그래프에서의 바이러스 개수를 카운트
                queue.append([next_row, next_col])
    local_safety = total - wall_cnt - local_virus_cnt
    # 안전 영역의 넓이는 (전체 넓이 - 벽의 개수 - 바이러스의 개수): BFS 이후 모든 그래프를 탐지하지 않아도 개수는 카운트 가능
    result = max(result, local_safety)

print(result)