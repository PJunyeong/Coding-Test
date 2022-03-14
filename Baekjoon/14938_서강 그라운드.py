import sys

n, m, r = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): nodes[i][i] = 0
items = [0] + list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = l
    nodes[b][a] = l

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]
# 플로이드-워셜 알고리즘을 통해 각 노드에서 다른 모든 노드에 대한 최단 거리 리턴

local_max = 0

for i in range(1, n+1):
    total = 0
    for j in range(1, n+1):
        if nodes[i][j] <= m:
            total += items[j]
    local_max = max(local_max, total)
# i번에서 떨어져서 다른 j번까지 가는 거리가 수백 범위 m 이하라면 아이템을 얻을 수 있다.

print(local_max)
