import sys
import heapq

v, e = map(int, sys.stdin.readline().rstrip().split())

INF = sys.maxsize
node_max = 100000
k_max = 1000000000
nodes = [[] for _ in range(v+node_max+1)]
# 두 개의 그래프를 만들기 위해 일차원 리스트로 연결 (노드의 개수 범위가 주어지므로)
for _ in range(e):
    x, y, t, k = map(int, sys.stdin.readline().rstrip().split())
    nodes[x].append([y, t])
    nodes[y].append([x, t])
    # 돈까스를 먹지 않은 상태 양방향 간선
    nodes[node_max+x].append([node_max+y, t])
    nodes[node_max+y].append([node_max+x, t])
    # 돈까스를 먹은 상태 양방향 간선
    nodes[x].append([node_max+y, k_max+t-k])
    nodes[y].append([node_max+ x, k_max + t - k])
    # k맛 돈까스를 먹은 상태. k_max가 주어지므로 기존 범위를 건드리지 않는다.

def Dijkstra():
    distances = [INF for _ in range(node_max+v+1)]
    distances[1] = 0

    pq = []
    heapq.heappush(pq, [0, 1])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost+next_cost, next_node])

    for i in range(node_max+2, node_max+v+1):
        # 돈까스를 먹은 상태 node_max+1 ~ node_max+v. 1번 노드가 시작 노드이므로 node_max+2가 2번 노드가 도착 지점인 상태
        print(distances[i]-k_max)
        # k_max를 빼주어야 기존 값이 나온다.

Dijkstra()