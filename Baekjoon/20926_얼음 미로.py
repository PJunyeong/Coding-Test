import sys
import heapq

m, n = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = []
start = [0, 0]
end = [0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if row[j] == 'T':
            row[j] = '0'
            start = [i, j]
        elif row[j] == 'E':
            end = [i, j]
    nodes.append(row)

def Dijkstra():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    distances[start[0]][start[1]] = 0
    pq = []
    heapq.heappush(pq, [0, start[0], start[1]])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if distances[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row, cur_col
            next_cost = 0
            while True:
                if next_row + y < 0 or next_col + x < 0 or next_row + y >= n or next_col + x >= m or not nodes[next_row+y][next_col+x].isdigit(): break
                next_row += y
                next_col += x
                next_cost += int(nodes[next_row][next_col])
            #     이동 가능할 때까지 빙판 이동
            if next_row + y < 0 or next_col + x < 0 or next_row + y >= n or next_col + x >= m or nodes[next_row+y][next_col+x] == 'H':continue
            #     다음 이동하는 곳이 구멍이라면 불가능
            elif nodes[next_row+y][next_col+x] == 'E':
                next_row += y
                next_col += x
            #     다음 이동하는 곳이 출구라면 가능
            if distances[next_row][next_col] > cur_cost + next_cost:
                distances[next_row][next_col] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])
    ans = distances[end[0]][end[1]]
    if ans == INF: return -1
    else: return ans

ans = Dijkstra()
print(ans)
