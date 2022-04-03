import sys
import heapq

INF = float(sys.maxsize)
start_x, start_y = map(float, sys.stdin.readline().rstrip().split())
goal_x, goal_y = map(float, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
pos = []

for i in range(1, n+1):
    cur_x, cur_y = map(float, sys.stdin.readline().rstrip().split())
    pos.append([cur_x, cur_y])
pos.insert(0, [start_x, start_y])
pos.append([goal_x, goal_y])

nodes = [[] for _ in range(n+1)]

def get_distance(x1, y1, x2, y2):
    distance = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
    return distance

for idx in range(1, n+2):
    x2, y2 = pos[idx]
    distance = get_distance(pos[0][0], pos[0][1], x2, y2)
    nodes[0].append([idx, distance / 5.0])
    # 시작점 ~ 모든 노드로 걷는 시간

for idx in range(1, n+1):
    x1, y1 = pos[idx]
    distance = get_distance(x1, y1, pos[n+1][0], pos[n+1][1])
    nodes[idx].append([n+1, distance/5.0])
    nodes[idx].append([n+1, 2.0 + (abs(distance-50.0) / 5.0)])
    # 대포 ~ 도착점으로 걷는 /대포 이동 시간
    # 걷는 시간은 거리/속도, 대포 이동 시간은 (대포 사용 시간 2초) + (걸어야 하는 시간).

for i in range(1, n+1):
    x1, y1 = pos[i]
    for j in range(i+1, n+1):
        x2, y2 = pos[j]
        distance = get_distance(x1, y1, x2, y2)
        nodes[i].append([j, distance/5.0])
        nodes[i].append([j, 2.0 + (abs(distance-50.0) / 5.0)])
        nodes[j].append([i, distance/5.0])
        nodes[j].append([i, 2.0 + (abs(distance-50.0) / 5.0)])
        # 대포 ~ 대포 걷는 / 대포 이동 시간


def Dijkstra():
    distances = [INF for _ in range(n+2)]
    distances[0] = 0.0
    pq = []
    heapq.heappush(pq, [0.0, 0])
    # 시작점 0번 노드에서 도착점 n+1번 노드까지 다익스트라 알고리즘

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if distances[cur_node] < cur_cost: continue
        elif cur_node == n+1: continue
        # 도착 노드는 간선을 연결하지 않았다.

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > next_cost + cur_cost:
                distances[next_node] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost + cur_cost, next_node])
    return distances[n+1]

print(Dijkstra())


