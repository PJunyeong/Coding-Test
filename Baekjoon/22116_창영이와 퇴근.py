import sys
import heapq
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = []
for _ in range(n): nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))
INF = sys.maxsize
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def Dijkstra():
    distances = [[INF for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0

    pq = []
    heapq.heappush(pq, [0, 0, 0])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if distances[cur_row][cur_col] < cur_cost: continue

        # if cur_row == n-1 and cur_col == n-1: break

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

            next_cost = max(cur_cost, abs(nodes[cur_row][cur_col]-nodes[next_row][next_col]))
            if distances[next_row][next_col] > next_cost:
                distances[next_row][next_col] = next_cost
                heapq.heappush(pq, [next_cost, next_row, next_col])
    return distances

distances = Dijkstra()
print(distances[n-1][n-1])


