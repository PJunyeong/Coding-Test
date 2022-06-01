import sys
import heapq

INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    row, col = map(int, sys.stdin.readline().rstrip().split())
    nodes = []
    prisoners = []
    blank = ["." for _ in range(col+2)]
    nodes.append(blank)
    for i in range(1, row+1):
        line = ["."] + list(sys.stdin.readline().rstrip()) + ["."]
        for j in range(col+2):
            if line[j] == "$": prisoners.append([i, j])
        nodes.append(line)
    nodes.append(blank)
    # 그래프를 상하좌우로 "." (빈 칸)으로 포함하는 새로운 그래프 -> 바깥에서 접근하는 루트를 그리기 위함

    def Dijkstra(start_row, start_col):
        distances = [[INF for _ in range(col+2)] for _ in range(row+2)]
        distances[start_row][start_col] = 0
        pq = []
        heapq.heappush(pq, [0, start_row, start_col])

        while pq:
            cur_cost, cur_row, cur_col = heapq.heappop(pq)
            if distances[cur_row][cur_col] < cur_cost: continue

            for x, y in zip(dx, dy):
                next_row, next_col = cur_row + y, cur_col + x
                if next_row < 0 or next_col < 0 or next_row >= row+2 or next_col >= col+2: continue

                next_cost = 0
                if nodes[next_row][next_col] == "#": next_cost += 1
                elif nodes[next_row][next_col] == "*": continue
                # 벽 통과 불가능, 문을 열었을 때에는 비용 1 추가

                if distances[next_row][next_col] > next_cost + cur_cost:
                    distances[next_row][next_col] = next_cost + cur_cost
                    heapq.heappush(pq, [next_cost + cur_cost, next_row, next_col])
        return distances

    prisoner1_row, prisoner1_col = prisoners[0]
    prisoner2_row, prisoner2_col = prisoners[1]
    prisoner1 = Dijkstra(prisoner1_row, prisoner1_col)
    prisoner2 = Dijkstra(prisoner2_row, prisoner2_col)
    third_party = Dijkstra(0, 0)
    # 죄수 1, 죄수 2, 외부인의 위치에서 각각 다익스트라 알고리즘을 통한 각 노드에 대한 최단 거리 리턴

    answer = INF
    for i in range(row+2):
        for j in range(col+2):
            # 모든 좌푯값의 비용 확인
            if nodes[i][j] == "*": continue
            # 벽이라면 이동 불가능한 곳
            cur_cost = prisoner1[i][j] + prisoner2[i][j] + third_party[i][j]
            if nodes[i][j] == "#": cur_cost -= 2
            # 한 문을 세 명이 열었다고 계산되므로 -2 해주기 (1번만 열면 그대로 문은 유지)
            answer = min(answer, cur_cost)
    print(answer)