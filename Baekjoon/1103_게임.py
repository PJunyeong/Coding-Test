import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
# 방문 체크 visited, 해당 노드 방문 가능한 최댓값 dp
for i in range(n):
    nodes[i] += sys.stdin.readline().rstrip()

finish = False

def DFS(pos, cnt):
    row, col = pos
    offset = int(nodes[row][col])
    dx = [offset, -offset, 0, 0]
    dy = [0, 0, offset, -offset]

    for x, y in zip(dx, dy):
        next_row, next_col = row + x, col + y
        if next_row < 0 or next_col < 0 or next_row >= n or next_col >= m or nodes[next_row][next_col] == 'H': continue
        # 배열 범위 밖이거나 구멍일 때는 접근 X
        if cnt + 1 > dp[next_row][next_col]:
            # 접근 가능하고 그 노드에 기록된 로컬 기록보다 현재 그 노드를 방문할 기록이 더 높다면 방문하자.
            if visited[next_row][next_col]:
                # 무한 루프인 경우
                global finish
                finish = True
                return finish
            else:
                visited[next_row][next_col] = True
                dp[next_row][next_col] = cnt + 1
                DFS([next_row, next_col], cnt + 1)
                visited[next_row][next_col] = False
                # 방문한지 체크하고 그 노드를 DFS로 체크한다. 그리고 다시 visited를 False로 바꿔준다. (재귀)
DFS([0, 0], 0)
if finish: print(-1)
else:
    ans = 0
    for i in range(n):
        ans = max(ans, max(dp[i]))
    print(ans+1)
