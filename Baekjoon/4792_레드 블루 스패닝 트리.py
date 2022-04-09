import sys
import heapq

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1,node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True
def Kruskal(pq):
    edge_cnt, blue_cnt = 0, 0
    while pq:
        cost, node1, node2, color = heapq.heappop(pq)
        if union(node1, node2):
            if color == 'B': blue_cnt += 1
            edge_cnt += 1
            if edge_cnt == n-1: return blue_cnt

while True:
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0 and k == 0: break

    red_pq, blue_pq = [], []
    # 색깔별 우선순위를 준 우선순위 큐를 각각 만든다.
    for _ in range(m):
        color, node1, node2 = sys.stdin.readline().rstrip().split()
        node1, node2 = int(node1), int(node2)
        if color == 'R':
            heapq.heappush(red_pq, [0, node1, node2, color])
            heapq.heappush(blue_pq, [1, node1, node2, color])
        else:
            heapq.heappush(red_pq, [1, node1, node2, color])
            heapq.heappush(blue_pq, [0, node1, node2, color])
    parents = [i for i in range(n + 1)]
    min_blue_cnt = Kruskal(red_pq)
    parents = [i for i in range(n + 1)]
    max_blue_cnt = Kruskal(blue_pq)
    # 파란색 간선이 사용되는 최소/최대 개수 중 k가 있다면 k개의 간선만 사용하고 MST를 만들 수 있다.

    if min_blue_cnt <= k and k <= max_blue_cnt: print(1)
    else: print(0)



