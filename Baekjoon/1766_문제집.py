import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    # tail -> head 연결
    in_degree[head] += 1
    # head에 몇 개의 tail이 연결되는지 확인

result = []
pq = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)
        # tail이 없는 degree 0인 노드만 heap에 넣는다. 번호가 작을 수록 우선순위 높음 (min-heap)

while pq:
    cur_node = heapq.heappop(pq)
    result.append(cur_node)

    for next_node in nodes[cur_node]:
        # cur_node -> next_node, cur_node 사용했으므로 next_node에 붙은 tail을 1 감소
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            # 0이 되어 큐에 들어갈 수 있음.
            heapq.heappush(pq, next_node)
            # next_node는 min-heap이기 때문에 자동으로 번호가 작은 노드가 다음 result에 더해진다.

print(*result, sep=' ')