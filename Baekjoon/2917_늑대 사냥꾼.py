import sys
import heapq
from collections import deque

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = []
start, end = [], []
trees = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    line = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if line[j] == 'V':
            start = [i, j]
            line[j] = '.'
        elif line[j] == 'J':
            end = [i, j]
            line[j] = '.'
        elif line[j] == '+':
            trees.append([i, j])
        # 시작점, 도착점, 나무 위치 파악

def BFS():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    queue = deque()
    for tree in trees:
        row, col = tree
        distances[row][col] = 0
        queue.append([row, col, 0])
    # 나무 기준 다른 모든 좌표와의 최소 거리 distances 구한다.
    while queue:
        cur_row, cur_col, cur_cost = queue.popleft()

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            if distances[next_row][next_col] > cur_cost + 1:
                # 한 좌표에 두 개 이상 나무가 접근 가능할 때 최솟값만 기록
                distances[next_row][next_col] = cur_cost + 1
                queue.append([next_row, next_col, cur_cost + 1])

    return distances

def path():
    pq = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = distances[start[0]][start[1]]
    heapq.heappush(pq, [-distances[start[0]][start[1]], start[0], start[1]])
    # max heap으로 시작점에서 연결된 모든 좌표 파악 가능
    visited[start[0]][start[1]] = True
    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        answer = min(-cur_cost, answer)
        # 경로 중 나무와의 거리가 최솟값을 answer에 기록

        if cur_row == end[0] and cur_col == end[1]: break
        # BFS로 경로 구하는 순간 break.

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row + y, cur_col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m: continue

            if not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                next_cost = distances[next_row][next_col]
                heapq.heappush(pq, [-next_cost, next_row, next_col])
    return answer

distances = BFS()
answer = path()
print(answer)

