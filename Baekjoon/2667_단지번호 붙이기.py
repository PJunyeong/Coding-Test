n = int(input())
nodes = [[] for _ in range(n)]
for i in range(n):
    nodes[i] += input()

for i in range(n):
    for j in range(n):
        nodes[i][j] = int(nodes[i][j])
# 탐색할 그래프 준비

total = []
cnt = 0
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1,-1]
# 상하좌우 이동할 때 현재 좌표 col, row에 더할 offset

for i in range(n):
    for j in range(n):
        if nodes[i][j] == 1:
            queue.append([i, j])
            # 현재 집이 있다면 이 좌표에서 시작한다.
            while queue:
                row, col = queue.pop(0)
                nodes[row][col] = 0
                # 방문했으므로 0으로 확인
                cnt += 1
                # 시작 노드와 연결된 모든 노드 카운트
                for x, y in zip(dx, dy):
                    next_row, next_col = row+x, col+y
                    # 이 노드에서 이동 가능한(즉 이전에 이동하지 않은) 노드 탐색
                    if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > n-1: continue

                    if nodes[next_row][next_col] == 1:
                        queue.append([next_row, next_col])
                        nodes[next_row][next_col] = 0
                        # 방문한 적이 없다면 큐에 넣고 탐색 마킹
            total.append(cnt)
            cnt = 0
            # 시작 노드와 연결된 모든 노드 카운트.
total.sort()
print(len(total))
for num in total:
    print(num)