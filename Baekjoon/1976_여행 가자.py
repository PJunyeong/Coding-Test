import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
nodes = []
INF = sys.maxsize
for i in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if i != j and nodes[i][j] == 0:
            nodes[i][j] = INF

for k in range(n):
    for i in range(n):
        for j in range(n):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

plan = list(map(int, sys.stdin.readline().rstrip().split()))

reachable = True
for i in range(len(plan)-1):
    if nodes[plan[i]-1][plan[i+1]-1] == INF:
        reachable = False
        break

if reachable: print('YES')
else: print('NO')


