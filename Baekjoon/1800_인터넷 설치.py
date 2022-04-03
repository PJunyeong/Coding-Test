import sys
import heapq

INF = sys.maxsize
n, p, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
max_cost = 0
for _ in range(p):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
    max_cost = max(max_cost, c)

def Dijkstra(cost_budget):
    distances = [INF for _ in range(n+1)]
    distances[1] = 0
    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost ,cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if cost_budget < next_cost:
                if distances[next_node] > cur_cost + 1:
                    distances[next_node] = cur_cost + 1
                    heapq.heappush(pq, [cur_cost + 1, next_node])
                    # cost_budget보다 값이 커지면 무료 기회를 사용해야 한다.
            else:
                if distances[next_node] > cur_cost:
                    distances[next_node] = cur_cost
                    heapq.heappush(pq, [cur_cost, next_node])
                    # cost_budget으로 모두 계산 가능. 무료 기회를 사용할 필요가 없다.
    return distances[n]
    # 1번부터 n번까지 연결했을 때 distances[n]은 무료 기회를 사용한 횟수다.

left, right = 0, max_cost
answer = INF
while left <= right:
    mid = (left + right) // 2
    if Dijkstra(mid) <= k:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

if answer == INF: print(-1)
else: print(answer)
