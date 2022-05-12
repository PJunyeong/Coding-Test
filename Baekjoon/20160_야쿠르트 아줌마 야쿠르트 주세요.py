import sys
import heapq

INF = sys.maxsize
n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
sell_point = list(map(int, sys.stdin.readline().rstrip().split()))
buy_start = int(sys.stdin.readline().rstrip())

def Dijkstra(start):
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
                heapq.heappush(pq, [next_cost + cur_cost, next_node])

    return distances

answer = INF
total = 0
sell = sell_point[0]
my_distances = Dijkstra(buy_start)
# 내가 출발하는 지점으로부터의 최단거리 리스트 my_distances

for end in sell_point:
    distances = Dijkstra(sell)
    distance = distances[end]
    # 출발점에서 각 야구르트를 파는 곳까지 가는 최단 거리 distance
    if distance == INF: continue
    # 팔지 못한다면 continue
    total += distance
    # 거리 누적
    sell = end
    # 다음 출발지 sell = 이번에 도착한 end.
    my_distance = my_distances[end]
    # 야쿠르트를 파는 end까지 가는 최단거리 my_distance
    if total >= my_distance:
        answer = min(answer, end)

if answer == INF: print(-1)
else: print(answer)