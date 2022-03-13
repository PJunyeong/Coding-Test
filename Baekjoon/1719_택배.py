import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    nodes[i][i] = 0
path = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = c
    nodes[b][a] = c
    path[a][b] = b
    path[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]
                path[i][j] = path[i][k]

for i in range(1, n+1):
    path[i][i] = '-'

for i in range(1, n+1):
    print(*path[i][1:], sep=' ')


