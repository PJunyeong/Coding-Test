import sys
INF = 100000000
n, m = map(int, sys.stdin.readline().rstrip().split())

nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n-1):
    tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail][head] = cost
    nodes[head][tail] = cost
    # 무방향 그래프 구현

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]
# 플로이드-워셜 알고리즘 -> 경유지 k를 통해 i에서 j로 가는 최단 거리 구한다.
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    print(nodes[tail][head])

