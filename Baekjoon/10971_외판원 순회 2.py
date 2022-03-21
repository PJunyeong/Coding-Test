import sys

n = int(sys.stdin.readline().rstrip())
nodes = []
for _ in range(n):
    nodes.append(list(map(int, sys.stdin.readline().rstrip().split())))

def DFS(cur_node, start_node, cost, visited_cnt):
    global ans
    if cur_node == start_node and visited_cnt == n:
        ans = min(ans, cost)

    for i in range(n):
        if not visited[i] and nodes[cur_node][i] != 0 and cost < ans:
                visited[i] = True
                visited_cnt += 1
                DFS(i, start_node, cost+nodes[cur_node][i], visited_cnt)
                visited[i] = False
                visited_cnt -= 1


ans = sys.maxsize
visited = [False for _ in range(n)]

for i in range(n):
    DFS(i, i, 0, 0)
print(ans)