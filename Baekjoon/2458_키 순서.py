import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1): nodes[i][i] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

cnt = 0
for i in range(1, n+1):
    is_rankable = True
    for j in range(1, n+1):
        if nodes[i][j] == INF and nodes[j][i] == INF:
            # i로부터의 거리 또는 i에 대한 거리가 모두 측정 불가할 때에는 등수를 매길 수 없다.
            is_rankable = False
            break
    if is_rankable: cnt += 1

print(cnt)