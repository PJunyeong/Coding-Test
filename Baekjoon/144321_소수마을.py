import sys
import heapq

INF = sys.maxsize
x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
nodes = []
nodes.append((x1, y1))
nodes.append((x2, y2))
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes.append((x, y))

def is_prime(dist):
    if dist < 2: return False
    elif dist == 2: return True
    for i in range(2, int(dist**0.5)+1):
        if dist % i == 0: return False
    return True

def Dijkstra():
    distances = [INF for _ in range(n+2)]
    distances[0] = 0
    pq = []
    heapq.heappush(pq, [0, 0])

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        cur_x, cur_y = nodes[cur_node]
        if distances[cur_node] < cur_cost: continue

        for next_node in range(n+2):
            next_x, next_y = nodes[next_node]
            next_cost = int(((cur_x-next_x)**2 + (cur_y-next_y)**2)**0.5)
            if is_prime(next_cost) and distances[next_node] > cur_cost + next_cost:
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_node])
    return distances[1]

ans = Dijkstra()
if ans == INF: print(-1)
else: print(ans)