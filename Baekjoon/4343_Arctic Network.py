import sys
import heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parents = [i for i in range(m)]
    outposts = []
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        outposts.append([x, y])
    pq = []
    for i in range(m):
        for j in range(i+1, m):
            x1, y1 = outposts[i]
            x2, y2 = outposts[j]
            cost = ((x1-x2)**2+(y1-y2)**2)**0.5
            heapq.heappush(pq, [cost, i, j])
            # 간선 별 비용 입력

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
    edge_num = n-1
    # n개 채널이 주어지므로 MST 중 (m-n)만 찾으면 된다.
    while pq:
        cur_cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            total = cur_cost
            edge_num += 1
            if edge_num == m - 1: break
    print(f"%0.2f"%total)