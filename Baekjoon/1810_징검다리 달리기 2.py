import sys
import heapq

INF = sys.maxsize
n, f = map(int, sys.stdin.readline().rstrip().split())
position = []
position.append([0, 0, 0])
goal = []
for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    position.append([x, y, i])
    if y == f: goal.append(i)

nodes = [[] for _ in range(n+1)]
visited = set()

position.sort()
for i in range(n+1):
    x1, y1, idx1 = position[i]
    for j in range(i+1, n+1):
        x2, y2, idx2 = position[j]
        if abs(x1 - x2) > 2: break
        # x 좌표 기준 j번 이후로는 i번째 인덱스의 좌표값으로부터 점프 불가능
        elif abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
            cost = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            nodes[idx1].append([idx2, cost])
            nodes[idx2].append([idx1, cost])
            if idx1 < idx2: visited.add((idx1, idx2))
            else: visited.add((idx2, idx1))

position.sort(key = lambda x:x[1])
for i in range(n+1):
    x1, y1, idx1 = position[i]
    for j in range(i+1, n+1):
        x2, y2, idx2 = position[j]
        if abs(y1 - y2) > 2: break
        # y 좌표 기준으로는 점프 불가능.
        elif abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
            if idx1 < idx2 and (idx1, idx2) in visited: continue
            elif idx1 > idx2 and (idx2, idx1) in visited: continue
            # x 좌표 기준으로 점프할 때 만들어둔 집합 visited를 통해 중복 체크
            cost = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
            nodes[idx1].append([idx2, cost])
            nodes[idx2].append([idx1, cost])

def Dijkstra():
    distances = [INF for _ in range(n+1)]
    distances[0] = 0
    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if distances[cur_node] < cur_cost: continue

        for next_node, next_cost in nodes[cur_node]:
            if distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])

    answer = INF
    for g in goal:
        answer = min(answer, distances[g])

    if answer == INF: return -1
    else:
        if answer >= int(answer) + 0.5: return int(answer) + 1
        else: return int(answer)

print(Dijkstra())



