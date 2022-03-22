import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
a, b, k ,g = map(int, sys.stdin.readline().rstrip().split())
GD = list(map(int, sys.stdin.readline().rstrip().split()))
GD_time = [0 for _ in range(g-1)]
INF = sys.maxsize
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, l = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append([v, l])
    nodes[v].append([u, l])
    if u in GD and v in GD and abs(GD.index(u)-GD.index(v)) == 1:
        if GD.index(u) > GD.index(v):
            GD_time[GD.index(v)] = l
        else:
            GD_time[GD.index(u)] = l
        # 국왕이 방문한 도로 i, i+1의 비용 -> GD_time 리스트 i번에 기록

for i in range(1, g-1):
    GD_time[i] += GD_time[i-1]
    # 0초 시작, 국왕이 해당 도로에서 보낸 시간을 구한다. (누적)

def get_GD(cur_cost):
    for i in range(g-1):
        if cur_cost < GD_time[i]:
            return (GD[i], GD[i+1], GD_time[i])
        # 현재 시간 국왕이 위치한 도로 (노드 번호 두 개로 표시) 및 그곳에서 나올 때까지 걸리는 시간 리턴
    return (-1, -1, -1)

def Dijsktra(start, k):
    distances = [INF for _ in range(n+1)]
    distances[start] = k
    # k 있다가 상근 출발하기 때문

    pq = []
    heapq.heappush(pq, [k, start])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        GD_node1, GD_node2, GD_time = get_GD(cur_cost)
        # 현재 시간 국왕의 위치 및 그곳에서 보내는 총 시간 리턴

        for next_node, next_cost in nodes[cur_node]:
            wait_cost = 0

            if (GD_node1 == cur_node and GD_node2 == next_node) or (GD_node1 == next_node and GD_node2 == cur_node):
                wait_cost = GD_time - cur_cost
                # 이용 간선이 국왕이 사용 중이라면 현재 시간과 비교, 기다리는 시간을 구한다.

            if distances[next_node] > wait_cost + cur_cost + next_cost:
                distances[next_node] = wait_cost + cur_cost + next_cost
                heapq.heappush(pq, [distances[next_node], next_node])
            # 다익스트라 알고리즘

    return distances[b] - k # 상근 입장에서 '배달을 마치는' 시간이므로 k 있다 출발한 것을 감산.

print(Dijsktra(a, k))