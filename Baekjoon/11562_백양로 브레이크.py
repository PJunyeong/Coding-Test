import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): nodes[i][i] = 0
for _ in range(m):
    u, v, b = map(int, sys.stdin.readline().rstrip().split())
    if b == 0:
        nodes[u][v] = 0
        nodes[v][u] = 1
        # u -> v라면 v -> u도 설치해야 하므로 비용은 1 추가 된다 (개수이므로)
    else:
        nodes[u][v] = 0
        nodes[v][u] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]
                # 연결해야 하는 수 (즉 일방향 -> 양방향으로 바꿀 개수의 총합)

k = int(sys.stdin.readline().rstrip())

for _ in range(k):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    print(nodes[s][e])
