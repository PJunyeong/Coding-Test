import sys
import heapq

INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 우, 좌, 상, 하
n, m = map(int, sys.stdin.readline().rstrip().split())
start_row, start_col, end_row, end_col = map(int, sys.stdin.readline().rstrip().split())
start_row -= 1
start_col -= 1
end_row -= 1
end_col -= 1
nodes = []
for _ in range(n): nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))
def Dijkstra():
    distances = [[[INF for _ in range(3)] for _ in range(m)] for _ in range(n)]
    # 3으로 나눈 나머지 0, 1, 2 때 각각 최솟값을 갱신할 distances 배열
    distances[start_row][start_col][1] = 0
    pq = []
    heapq.heappush(pq, [0, 1, start_row, start_col])
    # 첫 번째 움직임이 cnt == 1임을 주의

    while pq:
        cur_cost, cur_cnt, cur_row, cur_col = heapq.heappop(pq)
        if distances[cur_row][cur_col][cur_cnt] < cur_cost: continue

        for x, y in zip(dx, dy):
            if cur_cnt % 3 == 1 and x != 0: continue
            elif cur_cnt % 3 == 2 and y != 0: continue
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m or nodes[next_row][next_col] == -1: continue
            next_cost = nodes[next_row][next_col]
            next_cnt = (cur_cnt+1) % 3
            if distances[next_row][next_col][next_cnt] > next_cost + cur_cost:
                distances[next_row][next_col][next_cnt] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_cnt, next_row, next_col])
    answer = min(distances[end_row][end_col])
    # 각 나머지 카운트에서 도착지로 이동할 때 걸린 최솟값
    if answer == INF: return -1
    else: return answer

answer = Dijkstra()
print(answer)