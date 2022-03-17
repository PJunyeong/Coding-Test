import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    INF = sys.maxsize
    n, m = map(int, sys.stdin.readline().rstrip().split())
    nodes= [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1): nodes[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        nodes[a][b] = c
        nodes[b][a] = c
    friends_num = int(sys.stdin.readline().rstrip())
    friends = list(map(int, sys.stdin.readline().rstrip().split()))

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                    nodes[i][j] = nodes[i][k] + nodes[k][j]

    result = [0 for _ in range(n+1)]
    result[0] = INF

    for i in friends:
        for j in range(1, n+1):
            result[j] += nodes[i][j]
    print(result.index(min(result)))