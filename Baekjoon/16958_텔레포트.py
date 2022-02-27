from collections import deque
import sys

n, t = map(int, sys.stdin.readline().rstrip().split())
teleportable = [0 for _ in range(n)]
positions = [[] for _ in range(n)]
for i in range(n):
    teleport, row, col = map(int, sys.stdin.readline().rstrip().split())
    teleportable[i] = teleport
    positions[i] = [row, col]
    # 노드 별 좌표와 텔레포트 가능 여부 저장
INF = 10000
nodes = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j: nodes[i][j] = 0
        else:
            i_pos = positions[i]
            j_pos = positions[j]
            distance = abs(i_pos[0] - j_pos[0]) + abs(i_pos[1] - j_pos[1])
            if teleportable[i] == 1 and teleportable[j] == 1 and t < distance: distance = t
            nodes[i][j] = distance
            # 각 노드별 거리 초깃값 기록. 텔레포트 가능한 도시일 때 맨해튼 거리와 비교해서 최단 거리를 입력

# 플로이드-워셜 알고리즘으로 각 노드에서 다른 모든 노드로 가는 최단 거리를 구한다.

for k in range(n):
    for i in range(n):
        for j in range(n):
            if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                nodes[i][j] = nodes[i][k] + nodes[k][j]

m = int(input())
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(nodes[start-1][end-1])

