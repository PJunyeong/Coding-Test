import sys

v, e = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for _ in range(v+1)] for _ in range(v+1)]
# for i in range(1, v+1): nodes[i][i] = 0
# 자기 자신을 향한 도로는 없기 때문에 거리 무한으로 설정
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

local_min = INF

for i in range(1, v+1):
    for j in range(1, v+1):
        if nodes[i][j] != INF and nodes[j][i] != INF:
            # i -> j 갈 수 있고 j -> i 갈 수 있다면 i <-> j 사이클 거리는 합
            local_min = min(local_min, nodes[i][j] + nodes[j][i])

if local_min == INF: print(-1)
else: print(local_min)