import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n)]

h_max = 0
for i in range(n):
    nodes[i] += map(int, sys.stdin.readline().rstrip().split())
    h_max = max(h_max, max(nodes[i]))
    # 비의 범위는 오지 않거나 안전 영역의 최고 높이까지
result = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for h in range(h_max+1):

    local_nodes = [node[:] for node in nodes]
    for i in range(n):
        for j in range(n):
            if local_nodes[i][j] <= h:
                local_nodes[i][j] = -1
                # 이미 잠긴 영역은 -1로 마킹

    cnt = 0
    queue = deque()

    for i in range(n):
        for j in range(n):
            if local_nodes[i][j] != -1:
                # 비에 잠기지 않은 영역을 처음으로 발견했다.
                cnt += 1
                local_nodes[i][j] = -1
                queue.append([i, j])
                # 비에 잠겼다고 치고, 큐에 넣어서 방문 가능한 노드를 탐색한다.
                while queue:
                    row, col = queue.popleft()

                    for x, y in zip(dx, dy):
                        next_row, next_col = row + x, col + y

                        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

                        if local_nodes[next_row][next_col] != -1:
                            queue.append([next_row, next_col])
                            local_nodes[next_row][next_col] = -1
                            # 큐에 넣은 노드에서 탐색 가능한 범위가 모두 -1로 마킹되었다.
                            # 영역이 +1되었다.
    result.append(cnt)

print(max(result))
