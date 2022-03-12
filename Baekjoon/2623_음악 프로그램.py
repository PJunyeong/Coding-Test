import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
for _ in range(m):
    singers = list(map(int, sys.stdin.readline().rstrip().split()))
    if singers[0] > 0:
        for i in range(1, singers[0]+1):
            for j in range(i+1, singers[0]+1):
                nodes[singers[i]].append(singers[j])
                in_degree[singers[j]] += 1
                # tail -> head 연결

queue = deque()
result = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    cur_node = queue.popleft()
    result.append(cur_node)

    for next_node in nodes[cur_node]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)

if len(result) != n: print(0)
# 불가능하다는 뜻은 queue 반복문 중 in-degree가 0이 되는 케이스가 없다는 뜻이므로 조기 종료된다는 뜻.
else: print(*result, sep='\n')
