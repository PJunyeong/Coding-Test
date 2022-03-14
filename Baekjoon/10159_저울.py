import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
INF = sys.maxsize
nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1): nodes[i][i] = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j: continue
        if nodes[i][j] == INF and nodes[j][i] == INF:
            # 서로 다른 i번 노드와 j번 노드가 모두 닿지 못할 때 비교 불가능
            cnt += 1
    print(cnt)

