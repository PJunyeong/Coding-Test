import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    in_degree[head] += 1

queue = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

result = []

while queue:
    cur_node = queue.popleft()
    result.append(cur_node)

    for next_node in nodes[cur_node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

print(*result, sep=' ')