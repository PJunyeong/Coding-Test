import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]
edges = []
for _ in range(m):
    tail, head, cost = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(edges, [-cost, tail, head])

start, end = map(int, sys.stdin.readline().rstrip().split())

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
while edges:
    # 크루스칼 알고리즘으로 start와 end가 연결되는 경로에서 전달되는 cost 최솟값을 구한다.
    cost, tail, head = heapq.heappop(edges)

    if union(tail, head):
        # 새로운 경로가 추가될 때 이 경로는 (heap으로 현재 cost 이하임이 보장되므로) 로컬 중량 최솟값 업데이트
        total = cost

    if find(start) == find(end): break
        # 신장 트리에 start, end가 원하는 대로 연결되었다. 현재 total이 운송 가능 최댓값

print(-total)

