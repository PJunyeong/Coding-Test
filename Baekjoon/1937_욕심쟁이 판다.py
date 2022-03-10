import sys

sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline().rstrip())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(row, col):

    if dp[row][col] != 0:
        return dp[row][col]
        # dp 값이 기록되어 있다면 그대로 리턴

    else:
        dp[row][col] += 1
        # 새로 기록한다면 1부터 카운트(지금 노드도 카운트 포함)
        for x, y in zip(dx, dy):
            next_row, next_col = row + y, col + x
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n: continue

            if nodes[next_row][next_col] > nodes[row][col]:
                # 이동 가능하다면 '현재' 위치 dp는 기록된 dp와 다음 위치에서 DFS를 돌린 값에 +1 값 중 최댓값이다.
                dp[row][col] = max(dp[row][col], 1+DFS(next_row, next_col))

        return dp[row][col]
        # 윗 줄에서 DFS를 호출했을 때 전달할 값

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, DFS(i, j))
        # 모든 위치에서 시작, 최댓값 ans 찾는다.

print(ans)