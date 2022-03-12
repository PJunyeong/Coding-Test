import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(n+1)]
    in_degree = [0 for _ in range(n+1)]
    time = [0]
    time += list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        nodes[x].append(y)
        in_degree[y] += 1
    w = int(sys.stdin.readline().rstrip())

    def topological_sort():
        dp = [0 for _ in range(n+1)]
        queue = deque()

        for i in range(1, n+1):
            if in_degree[i] == 0:
                dp[i] = time[i]
                queue.append(i)

        while queue:
            cur_node = queue.popleft()

            for next_node in nodes[cur_node]:
                in_degree[next_node] -= 1
                dp[next_node] = max(dp[next_node], dp[cur_node] + time[next_node])
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        return dp
    dp = topological_sort()
    print(dp[w])