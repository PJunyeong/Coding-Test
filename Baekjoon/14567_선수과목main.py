import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    in_degree[head] += 1

def topological_sort():
    queue = []
    result = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if in_degree[i] == 0:
            heapq.heappush(queue, [1, i])

    while queue:
        cur_cnt, cur_node = heapq.heappop(queue)
        result[cur_node] = cur_cnt
        for next_node in nodes[cur_node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                heapq.heappush(queue, [cur_cnt+1, next_node])

    print(*result[1:], sep=' ')
topological_sort()