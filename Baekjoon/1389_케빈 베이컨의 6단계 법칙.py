import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: nodes[i][j] = 0

for _ in range(m):
    person1, person2 = map(int, sys.stdin.readline().rstrip().split())
    nodes[person1][person2] = 1
    nodes[person2][person1] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

local_min = INF
smallest_kevin = 0

for i in range(1, n+1):
    sum_kevin = sum(nodes[i][1:])
    if local_min > sum_kevin:
        local_min = sum_kevin
        smallest_kevin = i

print(smallest_kevin)


