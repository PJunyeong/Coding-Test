import sys
import heapq

INF = sys.maxsize
n, t = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    nodes.append(line)

dx = [0, 0, 1, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1]
dy = [1, -1, 0, 0, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1, 2]
# 1칸 이동 + 3칸 이동 offset

def Dijkstra():
    distances = [[INF for _ in range(n)] for _ in range(n)]
    distances[0][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, 0, 0])
    answer = INF
    while pq:
        cur_cost, cur_row, cur_col, cur_cnt = heapq.heappop(pq)

        if distances[cur_row][cur_col] < cur_cost: continue

        up_to_n = abs(n-1-cur_row) + abs(n-1-cur_col)
        if up_to_n <= 2:
            answer = min(answer, cur_cost + up_to_n*t)
            # 3칸 뛰지 않아도(즉 풀을 먹지 않아도) 될 때 최솟값 갱신

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue
            next_cost = 3*t + nodes[next_row][next_col]
            # 풀을 먹을 때 거리

            if distances[next_row][next_col] > next_cost + cur_cost:
                distances[next_row][next_col] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_row, next_col, cur_cnt + 1])
    return answer

ans = Dijkstra()
print(ans)


