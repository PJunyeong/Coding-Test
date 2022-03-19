import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
play = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[x].append(y)
    in_degree[y] += 1

is_possible = True
for _ in range(k):
    cmd, a = map(int, sys.stdin.readline().rstrip().split())
    if cmd == 1:
        if in_degree[a] == 0:
            play[a] += 1
            if play[a] == 1:
                # in_degree 0인 노드이므로 연결 노드의 in_degree를 1 감소
                for next_node in nodes[a]:
                    in_degree[next_node] -= 1
        else:
            is_possible = False
            break
    else:
        if play[a] == 0:
            is_possible = False
            break
        else:
            play[a] -= 1
            if play[a] == 0:
                # 해당 노드가 존재하지 않으므로 해당 노드가 필요한 연결 노드의 in_degree를 1 증가
                for next_node in nodes[a]:
                    in_degree[next_node] += 1

if is_possible: print("King-God-Emperor")
else: print("Lier!")