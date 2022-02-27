from collections import deque

n, l, r = map(int, input().split())

nodes = [[] for _ in range(n)]
for i in range(n):
    nodes[i] += map(int, input().split())
# 인구 수 그래프 구현

day = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    # 이 날의 연합을 구분할 visited. 연합 번호 1, 2, 3... 순서대로 연합이 가능한 노드를 표시한다.
    fedral_cnt = 1
    fedral_book = {}
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                queue = deque()
                queue.append([i, j])
                while queue:
                    pos = queue.popleft()
                    row, col = pos
                    visited[row][col] = fedral_cnt
                    fedral_pos = fedral_book.get(fedral_cnt, [])
                    fedral_pos.append([row, col])
                    fedral_book[fedral_cnt] = fedral_pos
                    # 연합 번호에 따라 좌표를 딕셔너리에 기록한다.

                    for x, y in zip(dx, dy):
                        next_row = row + x
                        next_col = col + y

                        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

                        if visited[next_row][next_col] == -1 and l <= abs(nodes[next_row][next_col] - nodes[row][col]) <= r:
                            queue.append([next_row, next_col])
                            visited[next_row][next_col] = fedral_cnt
                            # 이동 가능한 다음 노드가 아직 연합에 가입하지 않았다.
                            # 절댓값 차가 주어진 조건에 알맞을 때 탐색 가능. 큐에 넣는다.
                fedral_cnt += 1
                # 해당 fedral_cnt 연합 번호에 따른 노드 구분이 이루어졌다.
    # 모든 노드를 연합 가능한 fedral_cnt로 분류한다. 연합이 불가능하다면 자신만의 번호를 가진다는 뜻이다.

    is_fedral_possible = False
    for fedral_cnt in fedral_book.keys():
        fedral_num = len(fedral_book.get(fedral_cnt))
        if fedral_num == 1: continue
        # 이 연합에 가입한 노드가 2개 이상이어야 의미 있다.

        is_fedral_possible = True
        fedral_people = 0
        for fedral_nation in fedral_book.get(fedral_cnt):
            row, col = fedral_nation
            fedral_people += nodes[row][col]
        fedral_avg_people = fedral_people // fedral_num
        for fedral_nation in fedral_book.get(fedral_cnt):
            row, col = fedral_nation
            nodes[row][col] = fedral_avg_people
        # 연합 내 인구 합을 연합 수로 나눈 몫이 해당 연합의 인구 수로 기록된다.
    if not is_fedral_possible: break
    # 인구 이동이 불가능하다면 더 이상 반복하지 않는다.
    day += 1
    # 인구 이동이 가능할 때 날짜가 추가된다.
print(day)