import heapq
import sys

v, e = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(v+1)]
heap = []

for _ in range(e):
    tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(heap, [cost, tail, head])
    # 최소 신장 트리이므로 최소 비용 순서대로 간선을 정렬한다.
total = 0

def find(node):
    if parents[node] == node: return node
    # 루트 노드가 자기 자신이면 그대로 리턴한다.
    parents[node] = find(parents[node])
    return parents[node]
    # 루트 노드를 찾아 리턴한다. (재귀 효율화)

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if root1 == root2: return False
    else:
        parents[root1] = root2
        return True
    # 루트 노드가 서로 같다면 이미 연결한 노드이므로 신장 트리에 더할 수 없다.

while heap:
    cost, tail, head = heapq.heappop(heap)

    if union(tail, head):
        total += cost
        # 사이클을 만들지 않는 간선이라면 더하자.
print(total)