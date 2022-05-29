import sys
import heapq

INF = sys.maxsize
n = int(sys.stdin.readline().rstrip())
dangers = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    dangers.append([x1, y1, x2, y2])

m = int(sys.stdin.readline().rstrip())
deaths = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    deaths.append([x1, y1, x2, y2])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def Dijkstra():
    distances = [[INF for _ in range(501)] for _ in range(501)]
    distances[0][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, 0])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if distances[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row > 500 or next_col > 500: continue

            flag = False
            for x1, y1, x2, y2 in deaths:
                if x1 <= next_col <= x2 and y1 <= next_row <= y2:
                    flag = True
                    break
            if flag: continue
            next_cost = 0
            for x1, y1, x2, y2 in dangers:
                if x1 <= next_col <= x2 and y1 <= next_row <= y2:
                    next_cost += 1
                    break

            if distances[next_row][next_col] > next_cost + cur_cost:
                distances[next_row][next_col] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_row, next_col])
    return distances[500][500]

distance = Dijkstra()
if distance == INF: print(-1)
else: print(distance)
