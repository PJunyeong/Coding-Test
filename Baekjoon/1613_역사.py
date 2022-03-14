import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): nodes[i][i] = 0
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

order = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if nodes[i][j] == INF and nodes[j][i] == INF:
            order[i][j] = 0
        elif nodes[i][j] == INF and nodes[j][i] != INF:
            order[i][j] = 1
        else:
            order[i][j] = -1

s = int(sys.stdin.readline().rstrip())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(order[a][b])
