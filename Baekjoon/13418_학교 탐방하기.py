import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]
uphill = []
downhill = []

a, b, c = map(int, sys.stdin.readline().rstrip().split())

if c == 0: k = 1
else: k = 0
# 1번 노드까지 연결된 간선 종류 확인

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a > b: a, b = b, a
    if c == 0:
        heapq.heappush(uphill, [a, b])
    else:
        heapq.heappush(downhill, [a, b])
    # 오르막길, 내리막길 따로 분류 간선 저장

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

def kruskal(base_hill, another_hill):
    base_cnt = 0
    another_cnt = 0
    edge_cnt = 0

    while base_hill:
        node1, node2 = heapq.heappop(base_hill)
        if union(node1, node2):
            edge_cnt += 1
            base_cnt += 1
            if edge_cnt == n-1: break

    # 베이스가 되는 종류(오르막길/내리막길)을 써서 MST 만들 수 있으면 리턴.
    if edge_cnt == n-1:
        return [base_cnt, another_cnt]

    while another_hill:
        node1, node2 = heapq.heappop(another_hill)
        if union(node1, node2):
            edge_cnt += 1
            another_cnt += 1
            if edge_cnt == n-1: break

    return [base_cnt, another_cnt]
    # MST를 만들 때 사용 가능한 베이스가 되는 종류의 간선 개수 최댓값 리턴

uphill_copy = [edge[:] for edge in uphill]
downhill_copy = [edge[:] for edge in downhill]

base_cnt, min_uphill_cnt = kruskal(downhill_copy, uphill_copy)
parents = [i for i in range(n+1)]
# 루트 노드 초기화
max_uphill_cnt, another_cnt = kruskal(uphill, downhill)

max_uphill_cnt += k
min_uphill_cnt += k


print(max_uphill_cnt**2-min_uphill_cnt**2)