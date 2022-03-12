import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
time = [0]
for head in range(1, n+1):
    work = list(map(int, sys.stdin.readline().rstrip().split()))
    time.append(work[0])
    if work[1] > 0:
        for w in work[2:]:
            nodes[w].append(head)
            in_degree[head] += 1

queue = deque()
result = []
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
        dp[i] = time[i]
        # 바로 시작 가능

while queue:
    cur_node = queue.popleft()
    result.append(cur_node)

    for next_node in nodes[cur_node]:
        in_degree[next_node] -= 1
        # 일을 마칠 때마다 이 일을 마치고 할 수 있는 다른 작업에 시간이 더해진다.
        dp[next_node] = max(dp[next_node], time[next_node] + dp[cur_node])
        # dp는 선행 작업에 걸리는 시간들 가운데 최댓값 선택
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(max(dp))

