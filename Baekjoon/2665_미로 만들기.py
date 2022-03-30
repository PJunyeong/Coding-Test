import sys
import heapq

n = int(sys.stdin.readline().rstrip())
nodes = []
for _ in range(n): nodes.append(list(sys.stdin.readline().rstrip()))
INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def Dijkstra():
    distances = [[INF for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, 0])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if distances[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue
            next_cost = cur_cost + abs(int(nodes[next_row][next_col])-1)
            if distances[next_row][next_col] > next_cost:
                distances[next_row][next_col] = next_cost
                heapq.heappush(pq, [next_cost, next_row, next_col])
    print(distances[n-1][n-1])

Dijkstra()


