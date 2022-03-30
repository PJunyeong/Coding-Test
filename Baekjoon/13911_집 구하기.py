import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes_mac = [[] for _ in range(n+1)]
nodes_star = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes_mac[a].append([b, c])
    nodes_mac[b].append([a, c])
    nodes_star[a].append([b, c])
    nodes_star[b].append([a, c])
mac_num, x = map(int, sys.stdin.readline().rstrip().split())
macs = set(map(int, sys.stdin.readline().rstrip().split()))
for mac in macs:
    nodes_mac[0].append([mac, 0])
star_num, y = map(int, sys.stdin.readline().rstrip().split())
stars = set(map(int, sys.stdin.readline().rstrip().split()))
for star in stars:
    nodes_star[0].append([star, 0])
    # 더미 노드 0번 시작 그래프 두 개 생성

def Dijkstra(nodes):
    distances = [INF for _ in range(n+1)]
    distances[0] = 0

    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost+cur_cost, next_node])
    return distances

dist_macs = Dijkstra(nodes_mac)
dist_stars = Dijkstra(nodes_star)
# 맥도날드 / 스타벅스에서 시작한 각 모든 노드에 대한 최단 거리를 다익스트라를 통해 구한다.

ans = INF
for i in range(1, n+1):
    if i not in macs and i not in stars and dist_macs[i] <= x and dist_stars[i] <= y:
        # 최단 거리 x, y 보다 최단 거리가 작거나 같고 집이라면 거리 계산 가능
        ans = min(ans, dist_macs[i]+dist_stars[i])
if ans != INF: print(ans)
else: print(-1)
