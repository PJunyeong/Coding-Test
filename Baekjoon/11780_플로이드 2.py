import sys

INF = sys.maxsize
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
path = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    nodes[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if nodes[a][b] > c:
        nodes[a][b] = c
        path[a][b] = [b]
        # 최솟값 간선으로 초기화

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]
                path[i][j] = path[i][k][:] + path[k][j][:]
                # 기존 path를 클리어하고 k를 사용한 경로로 업데이트

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if nodes[i][j] == INF: nodes[i][j] = 0

for i in range(1, n + 1):
    print(*nodes[i][1:], sep=' ')

for i in range(1, n + 1):
    for j in range(1, n + 1):
        length = len(path[i][j])
        if length == 0: print(0)
        else: print(length + 1, i, *path[i][j], sep=' ')