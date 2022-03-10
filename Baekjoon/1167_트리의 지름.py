import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]

for _ in range(n):
    edges = list(map(int, sys.stdin.readline().rstrip().split()))
    tail = edges[0]
    for i in range(1, len(edges)-2, 2):
        nodes[tail].append([edges[i], edges[i+1]])

def BFS(start):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append([start, 0])
    visited[start] = True
    max_cost, max_cost_node = 0, start

    while queue:
        cur_node, cur_cost = queue.popleft()

        if max_cost < cur_cost:
            max_cost = cur_cost
            max_cost_node = cur_node
            # 거쳐온 거리 중 최장 거리 및 노드 구한다.

        for next_node, next_cost in nodes[cur_node]:
            if not visited[next_node]:
                is_leaf = False
                visited[next_node] = True
                queue.append([next_node, cur_cost+next_cost])

    return max_cost_node, max_cost

node1, cost = BFS(1)
node2, cost = BFS(node1)
# 특정 노드의 최장 거리 노드에서 다시 최장 거리를 구한다.

print(cost)



