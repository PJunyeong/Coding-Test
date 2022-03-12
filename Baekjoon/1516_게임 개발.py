import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
time = [0]
for i in range(1, n+1):
    build = list(map(int, sys.stdin.readline().rstrip().split()))
    build.pop(-1)
    time.append(build.pop(0))

    for b in build:
        nodes[b].append(i)
        in_degree[i] += 1

queue = deque()
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
        dp[i] = time[i]
        # 사전 건물이 없는 경우는 건물을 짓는 시간 곧 최소 시간

while queue:
    cur_node = queue.popleft()

    for next_node in nodes[cur_node]:
        in_degree[next_node] -= 1
        dp[next_node] = max(dp[next_node], time[next_node] + dp[cur_node])
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(*dp[1:], sep='\n')
