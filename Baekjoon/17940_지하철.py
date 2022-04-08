import sys
import heapq

INF = sys.maxsize
n, goal = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n)]
company = []
for _ in range(n): company.append(int(sys.stdin.readline().rstrip()))
for i in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(i+1, n):
        if line[j] != 0:
            nodes[i].append([j, line[j]])
            nodes[j].append([i, line[j]])

def Dijkstra(start):
    distances = [[INF for _ in range(n)] for _ in range(n)]
    distances[start][0] = 0
    pq = []
    heapq.heappush(pq, [0, 0, start])

    while pq:
        cur_cnt, cur_cost, cur_node = heapq.heappop(pq)

        flag = False
        for i in range(cur_cnt):
            if distances[cur_node][i] < cur_cost:
                flag = True
                break

        if flag or cur_cnt == n-1: continue

        for next_node, next_cost in nodes[cur_node]:
            next_cnt = cur_cnt
            if company[cur_node] != company[next_node]: next_cnt += 1
            if distances[next_node][next_cnt] > cur_cost + next_cost:
                distances[next_node][next_cnt] = cur_cost + next_cost
                heapq.heappush(pq, [next_cnt, cur_cost+next_cost, next_node])
    return distances[goal]


distances = Dijkstra(0)
for cnt, cost in enumerate(distances):
    if cost != INF:
        print(cnt, cost)
        break