import sys
import heapq

m, n = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n):
    line = list(map(int, input()))
    nodes.append(line)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = sys.maxsize

def Dijkstra():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    distances[0][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, 0])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if distances[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue
            next_cost = nodes[next_row][next_col]
            if distances[next_row][next_col] > cur_cost + next_cost:
                distances[next_row][next_col] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])

    print(distances[n-1][m-1])
    return

Dijkstra()