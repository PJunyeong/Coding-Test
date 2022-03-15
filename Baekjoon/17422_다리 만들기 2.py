import sys
from collections import deque
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))
queue = deque()

island_idx = 2
# 0 -> 바다, 1 -> 섬이므로 섬 인덱스를 2부터 센다.
islands = []

dir_idx = [0, 1, 2, 3]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if nodes[i][j] == 1:
            islands.append([])
            nodes[i][j] = island_idx
            queue.append([i, j])
            while queue:
                cur_row, cur_col = queue.popleft()
                islands[-1].append([cur_row, cur_col])
                for x, y in zip(dx, dy):
                    next_row, next_col = cur_row + y, cur_col + x

                    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

                    if nodes[next_row][next_col] == 1:
                        nodes[next_row][next_col] = island_idx
                        queue.append([next_row, next_col])
            island_idx += 1
            # 2, 3, 4... 로 서로 다른 섬 표시, 각 섬의 좌표를 islands 리스트에 넣는다.

island_cnt = island_idx - 2

pq = []
INF = sys.maxsize
edges = [[INF for _ in range(island_idx+1)] for _ in range(island_idx+1)]

for island in islands:
    island_num1 = nodes[island[0][0]][island[0][1]]
    for island_pos in island:
        queue.append([island_pos, 0, 0])
        queue.append([island_pos, 1, 0])
        queue.append([island_pos, 2, 0])
        queue.append([island_pos, 3, 0])
        # island는 특정 인덱스의 섬 좌표. 출발 노드를 각 방향 인덱스(동서남북)과 함께 큐에 삽입
        while queue:
            cur_pos, cur_dir, cur_cnt = queue.popleft()
            cur_row, cur_col = cur_pos

            next_row, next_col = cur_row + dy[cur_dir], cur_col + dx[cur_dir]

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            if nodes[next_row][next_col] == 0: queue.append([[next_row, next_col], cur_dir, cur_cnt + 1])
            # 직선 코스가 바다라면 계속 간다.
            elif nodes[next_row][next_col] != island_num1 and nodes[next_row][next_col] > 1 and cur_cnt > 1:
                # 직선 코스가 출발한 섬과 다른 종류의 섬이고 다리 길이가 1보다 클 때
                island_num2 = nodes[next_row][next_col]
                edges[island_num1][island_num2] = min(edges[island_num1][island_num2], cur_cnt)
                # 다리는 최솟값 유지
                edges[island_num2][island_num1] = edges[island_num1][island_num2]

pq = []

for i in range(2, island_idx+1):
    for j in range(2, island_idx+1):
        if i == j: continue

        if edges[i][j] != INF:
            heapq.heappush(pq, [edges[i][j], i, j])
            # 놓을 수 있는 다리를 min-heap 기준 다리에 넣는다.


def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

total = 0
parents = [i for i in range(island_idx+1)]
edge_cnt = island_cnt - 1
# 크루스칼 알고리즘의 MST 간선 개수는 언제나 노드 수 - 1
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)

    if union(node1, node2):
        total += cur_cost
        edge_cnt -= 1
        if edge_cnt == 0: break

if edge_cnt == 0: print(total)
else: print(-1)