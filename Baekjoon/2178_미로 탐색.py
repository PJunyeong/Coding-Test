n, m = map(int, input().split())
nodes = [[] for _ in range(n)]
for i in range(n):
    nodes[i] += input()
for i in range(n):
    for j in range(m):
        nodes[i][j] = int(nodes[i][j])
# 연결 그래프 리스트로 만들기

queue = [[[0, 0], 1]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 현재 좌표에서 상하좌우 이동한 좌표를 구할 때 더할 offset
while queue:
    pos, cnt = queue.pop(0)
    row, col = pos
    nodes[row][col] = 0
    # 현재 방문 노드 마크
    if row == n-1 and col == m-1: break
    # 도착지라면 탈출
    for x, y in zip(dx, dy):
        next_row = row + x
        next_col = col + y

        if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1: continue
        # 다음 좌표가 이동 가능할 때
        if nodes[next_row][next_col] == 1:
            queue.append([[next_row, next_col], cnt+1])
            nodes[next_row][next_col] = 0
            # 방문한 개수까지 넣어서 다음 방문할 노드 좌표를 큐에 넣는다.
            # 방문한 노드는 0으로 마크
print(cnt)
