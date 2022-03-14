import sys
import heapq

n, m, t = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])

parents = [i for i in range(n + 1)]
pq = []
accumulated = 0


def find(node):
    if parents[node] == node:
        return node
    else:
        parents[node] = find(parents[node])
        return parents[node]


for next_node, next_cost in nodes[1]:
    heapq.heappush(pq, [next_cost, next_node])

total = 0
while pq:
    next_cost, next_node = heapq.heappop(pq)

    if 1 != find(next_node):
        parents[next_node] = 1
        total += next_cost
        total += accumulated
        accumulated += t

        for another_node, another_cost in nodes[next_node]:
            heapq.heappush(pq, [another_cost, another_node])
print(total)

