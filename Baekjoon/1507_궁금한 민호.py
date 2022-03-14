import sys

n = int(sys.stdin.readline().rstrip())
nodes = []

for _ in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

is_possible = True
deactivated = [[False for _ in range(n)] for _ in range(n+1)]
for k in range(n):
    for i in range(n):
        if i == k: continue
        for j in range(n):
            if j == k or i == j: continue

            # 서로 다른 i, j, k. i -> k -> j가 가능할 때
            if nodes[i][j] == nodes[i][k] + nodes[k][j]:
                deactivated[i][j] = True
                # k 사용한 경로를 막는다.
            elif nodes[i][j] > nodes[i][k] + nodes[k][j]:
                is_possible = False
                break
                # k 사용이 불가

if not is_possible: print(-1)
else:
    total = 0
    for i in range(n):
        for j in range(i, n):
            if not deactivated[i][j]: total += nodes[i][j]
    print(total)