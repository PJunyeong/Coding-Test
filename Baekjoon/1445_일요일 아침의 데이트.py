import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
nodes = []
for i in range(n):
    nodes.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if nodes[i][j] == 'S': start = [i, j]
        elif nodes[i][j] == 'F': end = [i, j]

def Dijkstra():
    garages = [[INF for _ in range(m)] for _ in range(n)]
    garages[start[0]][start[1]] = 0
    near_garages = [[INF for _ in range(m)] for _ in range(n)]
    near_garages[start[0]][start[1]] = 0
    pq = []
    heapq.heappush(pq, [0, 0, start[0], start[1]])

    while pq:
        cur_cost, cur_near, cur_row, cur_col = heapq.heappop(pq)

        if garages[cur_row][cur_col] < cur_cost: continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            next_cost = cur_cost
            next_near_set = set()
            if nodes[next_row][next_col] == 'g': next_cost += 1
            # 쓰레기를 밟았다면 비용 카운트
            elif nodes[next_row][next_col] == '.':
                # 다음 노드가 빈 칸이라면 인접 노드에 쓰레기가 있는지 체크한다.
                for x, y in zip(dx, dy):
                    next_next_row, next_next_col = next_row + y, next_col + x

                    if next_next_row < 0 or next_next_col < 0 or next_next_row >= n or next_next_col >= m: continue
                    next_near_set.add(nodes[next_next_row][next_next_col])

            if 'g' in next_near_set: next_near = cur_near + 1
            # 인접 노드 중 쓰레기가 있다면 카운트
            else: next_near = cur_near

            if garages[next_row][next_col] > next_cost:
                garages[next_row][next_col] = next_cost
                near_garages[next_row][next_col] = next_near
                heapq.heappush(pq, [next_cost, next_near, next_row, next_col])
                # 밟은 쓰레기 개수 최소 경로 업데이트
            elif garages[next_row][next_col] == next_cost and near_garages[next_row][next_col] > next_near:
                # 밟은 쓰레기 개수가 같더라도 인접 쓰레기 개수를 업데이트 가능하다면 힙으로 push
                near_garages[next_row][next_col] = next_near
                heapq.heappush(pq, [next_cost, next_near, next_row, next_col])

    print(garages[end[0]][end[1]], near_garages[end[0]][end[1]])

Dijkstra()

