import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    nodes[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if nodes[a][b] > c:
        nodes[a][b] = c
    # 최단 경로만 받아들인다.

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

# 갈 수 없는 도시, 즉 거리 무한인 도시는 0으로 표시
for i in range(1, n+1):
    for j in range(1, n+1):
        if nodes[i][j] == INF: nodes[i][j] = 0

for node in (nodes[1:]):
    print(*(node[1:]), sep=' ')



