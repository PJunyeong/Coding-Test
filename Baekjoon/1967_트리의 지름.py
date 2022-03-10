import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, cost = map(int, sys.stdin.readline().rstrip().split())

    nodes[p].append([c, cost])
    nodes[c].append([p, cost])

def BFS(start):
    visited = [False for _ in range(n+1)]
    visited[start] = True
    queue = deque()
    queue.append([start, 0])
    local_max_cost, local_max_node = 0, start

    while queue:
        cur_node, cur_cost = queue.popleft()

        if local_max_cost < cur_cost:
            local_max_cost = cur_cost
            local_max_node = cur_node

        for next_node, next_cost in nodes[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node, next_cost+cur_cost])

    return local_max_node, local_max_cost

node1, cost = BFS(1)
node2, cost = BFS(node1)
print(cost)

