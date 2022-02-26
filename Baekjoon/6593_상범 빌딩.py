from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# 3차원 이동시 다음 좌표를 구할 오프셋

while True:
    l, c, r = map(int, input().split())
    if l == 0 and c == 0 and r ==0 : break

    nodes = [[[] for _ in range(c)] for _ in range(l)]
    # 3차원 그래프 구현

    for i in range(l):
        for j in range(c):
            nodes[i][j] += input()
        input()

    queue = deque()
    for i in range(l):
        for j in range(c):
            for k in range(r):
                if nodes[i][j][k] == 'S':
                    start = [i, j, k]
                    nodes[i][j][k] = '#'
                    # 시작 노드 위치를 구한다. 방문한 것으로 간주, #로 마킹
                elif nodes[i][j][k] == 'E':
                    nodes[i][j][k] = '.'
                    end = [i, j, k]
                    # 도착 노드 위치를 구한다. 방문할 것으로 간주, .로 탐색 가능하도록 만들자.
                    break

    queue.append([start, 0])
    reachable = False
    while queue:
        pos, cur_cost = queue.popleft()
        height, row, col = pos


        if pos == end:
            reachable = True
            break
            # 도착 노드에 도착했다면 탐색 가능함을 알려주고 탈출한다.

        for z, x, y in zip(dz, dx, dy):
            next_height = height + z
            next_row = row + x
            next_col = col + y

            if next_row < 0 or next_col < 0 or next_height < 0 or next_row >= c or next_col >= r or next_height >= l: continue
            # 현재 좌표에서 이동 가능한 노드를 구하기 위해 오프셋을 더하자. 배열 범위에서 벗어나는지 체크.

            if nodes[next_height][next_row][next_col] == '.':
                # 다음 좌표가 아직 탐색하지 않은 노드라면 #로 마킹하고 탐색한다.
                nodes[next_height][next_row][next_col] = '#'
                queue.append([[next_height, next_row, next_col], cur_cost + 1])

    if reachable: print(f"Escaped in {cur_cost} minute(s).")
    else: print("Trapped!")
