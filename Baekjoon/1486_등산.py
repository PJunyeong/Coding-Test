import string
import sys
import heapq

letter_code = {letter:idx for idx, letter in enumerate(string.ascii_uppercase)}
for idx, letter in enumerate(string.ascii_lowercase, start=26): letter_code[letter] = idx

n, m, t, d = map(int, sys.stdin.readline().rstrip().split())
nodes = []
INF = sys.maxsize
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    nodes.append(list(sys.stdin.readline().rstrip()))

def Dijstra(start_row, start_col):
    times = [[INF for _ in range(m)] for _ in range(n)]
    times[start_row][start_col] = 0

    pq = []
    heapq.heappush(pq, [0, start_row, start_col])

    while pq:
        cur_time, cur_row, cur_col = heapq.heappop(pq)

        if times[cur_row][cur_col] < cur_time: continue

        cur_height = letter_code.get(nodes[cur_row][cur_col])
        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            next_height = letter_code.get(nodes[next_row][next_col])

            if abs(cur_height - next_height) > t: continue

            if cur_height >= next_height:
                next_time = cur_time + 1
            else:
                next_time = cur_time + (cur_height-next_height)**2

            if times[next_row][next_col] > next_time:
                times[next_row][next_col] = next_time
                heapq.heappush(pq, [next_time, next_row, next_col])

    return times

my_times = Dijstra(0, 0)
# 시작 노드 호텔인 다익스트라 알고리즘

pos = []

for i in range(n):
    for j in range(m):
        if my_times[i][j] > d: continue
        heapq.heappush(pos, [-1 * letter_code.get(nodes[i][j]), i, j])
        # 해당 노드로 가는 시간이 d 이하라면 높이를 기준 max-heap

while pos:
    local_max, row, col = heapq.heappop(pos)
    local_times = Dijstra(row, col)

    if local_times[0][0] + my_times[row][col] > d: continue
    # 해당 높이를 시작으로 다익스트라 알고리즘, 호텔 도착 시간을 더해 d 시간 이하에 도착 가능하다면 가장 높은 높이.
    print(letter_code.get(nodes[row][col]))
    break


