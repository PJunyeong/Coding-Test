import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())

visited = [False for _ in range(f+1)]

queue = deque()
queue.append([s, 0])
visited[s] = True

while queue:
    cur_node, cur_cnt = queue.popleft()

    if cur_node == g: break

    for next_node in (cur_node+u, cur_node-d):
        if next_node < 1 or next_node > f: continue

        if not visited[next_node]:
            queue.append([next_node, cur_cnt+1])
            visited[next_node] = True

if cur_node == g: print(cur_cnt)
else: print("use the stairs")
