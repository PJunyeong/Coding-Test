import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
dp = [[0 for _ in range(n)] for _ in range(m)]
nodes = []

for _ in range(m):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(row, col):
    if dp[row][col] != 0: return dp[row][col]
    # 이미 카운트했다면 넘어간다.
    if row == m-1 and col == n-1:
        # 도착지로 이동 가능한 dp면 +1 돌려준다.
        return 1

    for x, y in zip(dx, dy):
        next_row, next_col = row + y, col + x
        if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n: continue

        if nodes[next_row][next_col] < nodes[row][col]:
            # 내리막길이라면 선택
            dp[row][col] += DFS(next_row, next_col)
    return dp[row][col]



DFS(0, 0)
print(dp[0][0])
