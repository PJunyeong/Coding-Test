import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n): nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def Dijkstra():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    distances[0][0] = nodes[0][0]
    pq = []
    if distances[0][0] == -1: return INF
    else: heapq.heappush(pq, [distances[0][0], 0, 0])
    # 시작지가 -1이면 이동 자체가 불가능
    # 시작할 때 사용하는 비용은 0 이나리 nodes[0][0]임을 주의

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)

        if distances[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue
            next_cost = nodes[next_row][next_col]
            if distances[next_row][next_col] > cur_cost + next_cost and next_cost != -1:
                distances[next_row][next_col] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])

    return distances[n-1][m-1]

answer = Dijkstra()
if answer == INF: print(-1)
else: print(answer)
