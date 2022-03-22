import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
INF = sys.maxsize
def Dijsktra(start):
    distances = [INF for _ in range(n+1)]
    distances[start] = 0

    pq = []
    heapq.heappush(pq, [0, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost+next_cost, next_node])
    return distances

distances = Dijsktra(2)
# T 기준 다익스트라 알고리즘

def rational_path(cur_node):
    if dp[cur_node] == 0:
        for next_node, next_cost in nodes[cur_node]:
            if distances[cur_node] > distances[next_node]:
                # cur_node보다 next_node 사용이 T에 도달하는 더 합리적인 이동 경로.
                dp[cur_node] += rational_path(next_node)
        return dp[cur_node]
    else:
        return dp[cur_node]


dp = [0 for _ in range(n+1)]
dp[2] = 1
# T -> T일 때 1로 취급
print(rational_path(1))
