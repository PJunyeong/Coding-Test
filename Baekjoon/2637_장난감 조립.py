import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
needed = [[0 for _ in range(n+1)] for _ in range(n+1)]
basics = []

for _ in range(m):
    x, y, k = map(int, sys.stdin.readline().rstrip().split())
    nodes[y].append([x, k])
    in_degree[x] += 1

queue = deque()

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)
        basics.append(i)
        # degree 값이 0인 노드는 기본 부품

while queue:
    cur_node = queue.popleft()

    for next_node, next_cost in nodes[cur_node]:
        if cur_node in basics:
            needed[next_node][cur_node] += next_cost
            # next_node를 만들기 위한 cur_node(기본 부품)은 next_cost 더 필요
        else:
            for i in range(1, n+1):
                needed[next_node][i] += needed[cur_node][i] * next_cost
                # next_node를 만들기 위한 cur_node(중간/최종 부품)은 cur_node를 만들기 위한 기본 부품을 각각 더해준다.

        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

for num, cnt in enumerate(needed[n][1:], start=1):
    if cnt > 0:
        print(num, cnt)
