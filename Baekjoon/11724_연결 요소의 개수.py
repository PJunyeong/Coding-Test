import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes  = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append(v)
    nodes[v].append(u)
visited = [False for _ in range(n+1)]

connected = 0
queue = deque()

for i in range(1, n+1):
    if not visited[i]:
        queue.append(i)
        visited[i] = True
        while queue:
            cur_node = queue.popleft()

            for next_node in nodes[cur_node]:
                if not visited[next_node]:
                    queue.append(next_node)
                    visited[next_node] = True
        connected += 1

print(connected)
