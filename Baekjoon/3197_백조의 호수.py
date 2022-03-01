import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(r)]
water_visited = [[False for _ in range(c)] for _ in range(r)]
swan_visited = [[False for _ in range(c)] for _ in range(r)]

water_queue = deque()
next_water_queue = deque()
swan_queue = deque()
next_swan_queue = deque()

# 이번 차례 백조 이동하는 swan_queue, 이동 불가능하다면 next_swan_queue로 좌표 저장
# 물 또한 이번 차례 들어온 좌표는 '.'으로 녹이고, 동서남북 연결된 얼음 'X' 좌표를 next_water_queue에 저장

for i in range(r):
    nodes[i] += sys.stdin.readline()
    for j in range(c):
        if nodes[i][j] == '.':
            water_queue.append([i, j])
            water_visited[i][j] = True
        elif nodes[i][j] == 'L':
            nodes[i][j] = '.'
            water_queue.append([i, j])
            water_visited[i][j] = True
            swan_queue.append([i, j])
        # 0일차 호수 정보 큐에 담는다.
        # 물이라면 좌표 water_queue에 담고 water_visited로 체크
        # 백조 위치 또한 '.'으로 세팅한 뒤 물과 똑같이 간주

swan1_row, swan1_col = swan_queue.popleft()
swan2_row, swan2_col = swan_queue.popleft()
swan_queue.append([swan1_row, swan1_col])
swan_visited[swan1_row][swan2_col] = True
# 1번 백조가 2번 백조를 만날 때까지 2번 백조는 고정, 1번만 움직일 때

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def swan_bfs():
    while swan_queue:
        row, col = swan_queue.popleft()
        if row == swan2_row and col == swan2_col:
            return True
        # 백조가 만날 때 true 리턴
        for x, y in zip(dx, dy):
            next_row, next_col = row + x, col + y
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c: continue
            if not swan_visited[next_row][next_col] and nodes[next_row][next_col] == '.':
                swan_queue.append([next_row, next_col])
                swan_visited[next_row][next_col] = True
                # 이동 가능하다면 움직인다.
            elif not swan_visited[next_row][next_col] and nodes[next_row][next_col] == 'X':
                next_swan_queue.append([next_row, next_col])
                swan_visited[next_row][next_col] = True
                # 이동 불가능하다면 다음 차례 큐에 담는다. 어차피 이동할 것이므로 swan_visited도 미리 체크할 수 있다.
    return False

def water_bfs():
    while water_queue:
        row, col = water_queue.popleft()
        nodes[row][col] = '.'

        for x, y in zip(dx, dy):
            next_row, next_col = row + x, col + y
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c: continue

            if not water_visited[next_row][next_col] and nodes[next_row][next_col] == 'X':
                next_water_queue.append([next_row, next_col])
                water_visited[next_row][next_col] = True
                # 처음 만나는 얼음이라면 다음에 녹일 next_water_queue에 넣는다.
            elif not water_visited[next_row][next_col] and nodes[next_row][next_col] == '.':
                water_queue.append([next_row, next_col])
                water_visited[next_row][next_col] = True
                # 처음 만나는 물 역시 water_queue에 넣으면서 얼음 만날 때까지 확인

day = 0

while True:
    water_bfs()
    if swan_bfs(): break
    water_queue = next_water_queue
    next_water_queue = deque()
    swan_queue = next_swan_queue
    next_swan_queue = deque()
    # 다음 날 물과 백조 위치를 water_queue, swan_queue로 담고 각각 초기화한다.
    day += 1

print(day)