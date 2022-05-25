import sys
import heapq

sys.setrecursionlimit(10**6)
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    nodes = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    colors = [-1 for _ in range(v+1)]
    for _ in range(e):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        nodes[u].append(v)
        nodes[v].append(u)

    def DFS(node, color):
        global flag
        visited[node] = True
        colors[node] = color

        for next_node in nodes[node]:
            if visited[next_node]:
                if colors[next_node] == color:
                    flag = False
            else:
                DFS(next_node, abs(1-color))

    flag = True
    for i in range(1, v+1):
        if not visited[i]:
            visited[i] = True
            DFS(i, 1)

    if flag: print("YES")
    else: print("NO")
