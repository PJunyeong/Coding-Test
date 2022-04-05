import sys
import heapq

INF = sys.maxsize
n, m, k = map(int, sys.stdin.readline().rstrip().split())
s, d = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c])
    nodes[b].append([a, c])
taxes = [0]
for _ in range(k): taxes.append(int(sys.stdin.readline().rstrip()))

def Dijkstra():
    distances = [[INF for _ in range(n+1)] for _ in range(n+1)]
    distances[s][0] = 0
    pq = []
    heapq.heappush(pq, [0, s, 0])

    while pq:
        cur_cost, cur_node, cur_edge_cnt = heapq.heappop(pq)

        flag = False
        for i in range(cur_edge_cnt):
            if distances[cur_node][i] < cur_cost:
                flag = True
                break
                # 지금 사용한 간선 개수보다 더 적은 간선을 사용했을 때 비용이 작은 경우가 존재한다면 굳이 사용할 필요가 없다.

        if flag or cur_edge_cnt == n: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node][cur_edge_cnt+1] > next_cost + cur_cost:
                distances[next_node][cur_edge_cnt+1] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node, cur_edge_cnt+1])
    return distances

distances = Dijkstra()
path = []
for idx, distance in enumerate(distances[d]):
    if distance != INF:
        path.append([distance, idx])
        # 목적지에 도착 가능한 경로의 거리 및 이동 간선 개수를 기록

def path_filter():
    filtered = [path[0]]
    for i in range(1, len(path)):
        if path[i-1][1] > path[i][1]: filtered.append(path[i])
        # path.sort()에 의해 앞에 있는 path의 distance는 더 작은 게 보장된다.
        # distance가 다른 경우보다 크다면 path에 사용한 간선 개수가 적어야 최소 경로가 될 가능성이 있다.
    return filtered

def path_find(tax):
    global path
    for i in range(len(path)):
        path[i][0] += path[i][1] * tax
    path.sort()
    path = path_filter()
    # 다른 경우보다 이동 거리도 크고 이용 간선 개수도 많다면 path에 있을 까닭 X
    print(path[0][0])

for tax in taxes:
    path_find(tax)
    # tax를 더했을 때 이동 간선 개수에 따라 최소 거리가 바뀔 수 있다.

