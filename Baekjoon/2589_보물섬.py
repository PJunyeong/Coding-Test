import heapq
from collections import deque
# 루트 노트에서 각 리프 노드까지의 거리를 힙에 넣는다.
# BFS로 확인할 때 리스트가 아니라 디큐를 통해 시간 효율성 높이자.

n, m = map(int, input().split())
nodes = [[] for _ in range(n)]

for i in range(n):
    nodes[i] += input()
shortest = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(m):
        if nodes[i][j] == 'L':
            # 이 육지에서 탐색 가능한 다른 육지까지의 거리를 카운트한다.
            queue = deque()
            maps = [node[:] for node in nodes]
            # 방문할 때마다 마킹해야 하므로 이 좌표점에 필요한 maps를 따로 만들자.
            queue.append([[i, j], 0])
            while queue:
                pos, cur_cost = queue.popleft()
                row, col = pos
                maps[row][col] = 'W'

                is_leaf = True
                for x, y in zip(dx, dy):
                    next_row = row + x
                    next_col = col + y

                    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

                    if maps[next_row][next_col] == 'L':
                        is_leaf = False
                        queue.append([[next_row, next_col], cur_cost + 1])
                        maps[next_row][next_col] = 'W'
                        # 이동한 노드는 'W'로 마킹해 중복 이동하지 않도록 하자.
                    # 만일 이동 가능한 노드가 없다면 리프 노드다.

                if is_leaf: heapq.heappush(shortest, -1 * cur_cost)
                # 현재 노드가 리프 노드라면 이 노드까지 걸린 시간을 힙에 넣자.

print(heapq.heappop(shortest) * -1)
# 힙에 들어 있는 수 중 최댓값을 리턴한다.