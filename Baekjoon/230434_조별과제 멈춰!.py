import sys
import heapq
from collections import deque

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1,node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True
def Kruskal():
    total = 0
    edge_cnt = 0
    while pq:
        cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            nodes[node1].append([node2, cost])
            nodes[node2].append([node1, cost])
            total += cost
            edge_cnt += 1
            if edge_cnt == n-1: return total

def BFS(start):
    queue = deque()
    queue.append([start, 0])
    visited = [False for _ in range(n+1)]
    visited[start] = True

    while queue:
        cur_node, cur_cost = queue.popleft()

        for next_node, next_cost in nodes[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                dp[start][next_node] = max(next_cost, cur_cost)
                queue.append([next_node, dp[start][next_node]])
                # start -> next_node로 가는 가장 짧은 길이의 경로 중 최댓값을 max(next_cost, cur_cost)로 기록한다.

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n+1)]
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(pq, [c, a, b])
total = Kruskal()
# 크루스칼 알고리즘을 통해 MST 구성 간선 및 MST 비용 total 리턴
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
# start 노드 -> 다른 노드로 가는 경로 중 최댓값을 dp[start][end]에 기록한다.
for i in range(1, n+1):
    BFS(i)

q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(total-dp[x][y])
    # x와 y를 연결하는 경로 중 가장 비용이 큰 간선 dp[x][y]를 MST 비용 total에서 뺀 값이 답.



