import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
nodes_inv = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append([head, cost])
    in_degree[head] += 1
    nodes_inv[head].append([tail, cost])

start, end = map(int, sys.stdin.readline().rstrip().split())

def topological_sort():
    queue = deque()
    dp = [0 for i in range(n+1)]
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append([i, 0])

    while queue:
        cur_node, cur_cost = queue.popleft()

        for next_node, next_cost in nodes[cur_node]:
            in_degree[next_node] -= 1
            dp[next_node] = max(dp[next_node], next_cost + dp[cur_node])
            if in_degree[next_node] == 0:
                queue.append([next_node, cur_cost + next_cost])

    return dp
# 위상 정렬을 dp를 통해 값을 누적시키면서 정렬. 각 도시별로 가는 최장 거리를 기록한다.

dp = topological_sort()

edges = set()
def BFS():
    queue = deque()
    queue.append([end, 0])
    # nodes_inv는 그래프의 head와 tail을 거꾸로 만든 그래프

    while queue:
        cur_node, cur_cost = queue.popleft()

        for post_node, post_cost in nodes_inv[cur_node]:
            if dp[cur_node] == post_cost + dp[post_node] and tuple((post_node, cur_node)) not in edges:
                # post_cost를 사용한 루트가 최장 거리일 때에만 추적한다. 이때 중복 간선을 체크하기 위해 set으로 확인.
                edges.add(tuple((post_node, cur_node)))
                queue.append([post_node, cur_cost+post_cost])
BFS()

print(dp[end])
# end까지 간선으로 이동하는 최장 거리
print(len(edges))
# 최장거리 루트에 사용된 간선의 개수
