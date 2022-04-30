import sys
import heapq

INF = sys.maxsize
n, m, a, b, c = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
costs = []
for _ in range(m):
    node1, node2, cost = map(int, sys.stdin.readline().rstrip().split())
    nodes[node1].append([node2, cost])
    nodes[node2].append([node1, cost])
    costs.append(cost)
#   간선 비용 최소/최대 값을 기록, 이후 이분 탐색에 사용 (시간 효율성)
#   양방향 그래프 구현

def Dijsktra(limit):
    distances = [INF for _ in range(n + 1)]
    distances[a] = 0
    pq = []
    heapq.heappush(pq, [0, a])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost and next_cost <= limit:
                # 간선 비용이 제한 비용 이내면 이동 가능
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])
    if distances[b] > c: return INF
    else: return distances[b]
#   사용 가능한 c원 이하로 b에 도착할 수 있다면 INF가 아닌 값 리턴

costs.sort()
left, right = 0, len(costs)-1
answer = INF
while left <= right:
    mid = (left + right) // 2
    total = Dijsktra(costs[mid])
    if total == INF:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(costs[mid], answer)
#   c원 이내로 도착지 b에 도착할 때 간선 비용을 mid로 제한, mid의 최솟값을 answer에 기록한다.

if answer == INF: print(-1)
else: print(answer)
