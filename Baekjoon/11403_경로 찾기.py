import sys

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n)]
INF = sys.maxsize

for i in range(n):
    nodes[i] += map(int, sys.stdin.readline().rstrip().split())
    for j in range(n):
        if nodes[i][j] == 0:
            nodes[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

for i in range(n):
    for j in range(n):
        if nodes[i][j] == INF: nodes[i][j] = 0
        else: nodes[i][j] = 1
# 거리가 무한이면 갈 수 없다는 뜻.

for i in range(n):
    print(*nodes[i], sep=' ')

