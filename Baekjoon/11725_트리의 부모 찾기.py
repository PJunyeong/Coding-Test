import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    nodes[head].append(tail)

nodes_parent = [0 for _ in range(n+1)]

visited = [False for _ in range(n+1)]
queue = deque()

queue.append(1)
visited[1] = True

while queue:
    cur_node = queue.popleft()

    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            visited[next_node] = True
            nodes_parent[next_node] = cur_node
            queue.append(next_node)

print(*(nodes_parent[2:]), sep='\n')