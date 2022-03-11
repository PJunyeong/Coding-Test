import sys
import heapq

while True:
    m, n = map(int, sys.stdin.readline().rstrip().split())
    if m == 0 and n == 0: break
    pq = []
    money = 0
    parents = [i for i in range(m)]
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().rstrip().split())
        money += z
        heapq.heappush(pq, [z, x, y])

    def find(node):
        if parents[node] == node: return node
        else:
            parents[node] = find(parents[node])
            return parents[node]

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)

        if root1 == root2: return False
        else:
            parents[root2] = root1
            return True

    total = 0

    while pq:
        z, x, y = heapq.heappop(pq)

        if union(x, y):
            total += z

    print(money - total)