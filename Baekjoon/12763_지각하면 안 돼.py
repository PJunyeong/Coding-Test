import sys
import heapq

INF = sys.maxsize

def Dijkstra():
    distances = [[INF for _ in range(t+1)] for _ in range(n+1)]
    distances[1][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, 1])

    while pq:
        cur_cost, cur_time, cur_node = heapq.heappop(pq)
        if distances[cur_node][cur_time] < cur_cost: continue

        for next_node, next_time, next_cost in nodes[cur_node]:
            if t < next_time + cur_time or m < next_cost + cur_cost: continue
            if distances[next_node][next_time+cur_time] > next_cost + cur_cost:
                distances[next_node][next_time+cur_time] = next_cost + cur_cost
                heapq.heappush(pq, [next_cost+cur_cost, next_time+cur_time, next_node])
    answer = min(distances[n])
    if answer == INF: return -1
    else: return answer

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n+1)]
t, m = map(int, sys.stdin.readline().rstrip().split())
l = int(sys.stdin.readline().rstrip())
for _ in range(l):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append([b, c, d])
    nodes[b].append([a, c, d])
print(Dijkstra())