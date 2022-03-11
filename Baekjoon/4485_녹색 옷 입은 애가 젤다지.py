import sys
import heapq

INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
problem_cnt = 1

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0: break

    nodes = []
    for _ in range(n):
        nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

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

                next_cost = nodes[next_row][next_col]

                if distances[next_row][next_col] > next_cost + cur_cost:
                    distances[next_row][next_col] = next_cost + cur_cost
                    heapq.heappush(pq, [next_cost+cur_cost, next_row, next_col])

        print(f'Problem {problem_cnt}: {distances[n-1][n-1]+nodes[0][0]}')

    Dijkstra()
    problem_cnt += 1
