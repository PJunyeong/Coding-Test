from collections import deque


def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(maps)
    m = len(maps[0])

    def BFS():
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = True
        queue = deque()
        queue.append([0, 0, 1])

        while queue:
            cur_row, cur_col, cur_cost = queue.popleft()

            if cur_row == n - 1 and cur_col == m - 1:
                return cur_cost

            for x, y in zip(dx, dy):
                next_row, next_col = cur_row + y, cur_col + x
                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m:
                    continue

                if not visited[next_row][next_col] and maps[next_row][next_col] == 1:
                    visited[next_row][next_col] = True
                    queue.append([next_row, next_col, cur_cost + 1])

        return -1

    answer = BFS()
    return answer