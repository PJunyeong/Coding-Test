t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    # row N col M
    nodes = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        col, row = map(int, input().split())
        nodes[row][col] = 1
    queue = []
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 상화좌우 이동할 때 현재 좌표 row, col에 각각 더할 offset
    for i in range(n):
        for j in range(m):
            if nodes[i][j] == 1:
                queue.append([i, j])
                # 순서대로 이동하며 이동 가능 노드를 시작 노드로 선택
                while queue:
                    row, col = queue.pop(0)
                    nodes[row][col] = 0
                    # 방문 노드를 0으로 마크
                    for x, y in zip(dx, dy):
                        next_row, next_col = row+x, col+y
                        # 상하좌우 이동 시 이동 가능한지 확인
                        if next_row < 0 or next_col < 0 or next_row > n-1 or next_col > m-1: continue

                        # 이동 시 연결 노드가 있다면 큐에 넣고 0으로 마킹
                        if nodes[next_row][next_col] == 1:
                            queue.append([next_row, next_col])
                            nodes[next_row][next_col] = 0
                cnt += 1
                # 클러스터의 개수만 파악한다.
    print(cnt)
