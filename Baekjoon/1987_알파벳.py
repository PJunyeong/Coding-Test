import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(r)]
for i in range(r):
    nodes[i] += list(sys.stdin.readline().rstrip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = set()
# 디큐를 쓰면 시간 초과가 난다.
queue.add((0, 0, nodes[0][0]))
answer = 1

while queue:
    row, col, visited = queue.pop()

    for x, y in zip(dx, dy):
        next_row, next_col = row + y, col + x

        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c: continue

        if nodes[next_row][next_col] not in visited:
            queue.add((next_row, next_col, visited + nodes[next_row][next_col]))
            answer = max(answer, len(visited)+1)

print(answer)