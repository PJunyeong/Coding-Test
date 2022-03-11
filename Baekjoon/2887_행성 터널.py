import sys
import heapq

n = int(sys.stdin.readline().rstrip())
nodes = []
for idx in range(n):
    pos = list(map(int, sys.stdin.readline().rstrip().split()))
    pos.append(idx)
    # 행성 인덱스까지 기록
    nodes.append(pos)

pq = []
parents = [i for i in range(n)]

# 행성 두 개를 연결하는 가장 짧은 터널을 x, y, z 세 축을 기준으로 만들어 힙에 넣는다. 이때 기존 인덱스를 넣어야 함.
nodes.sort(key= lambda x:x[0])
for i in range(n-1):
    x_a, y_a, z_a, idx_a = nodes[i]
    x_b, y_b, z_b, idx_b = nodes[i+1]
    heapq.heappush(pq, [x_b-x_a, idx_a, idx_b])

nodes.sort(key= lambda x:x[1])
for i in range(n-1):
    x_a, y_a, z_a, idx_a = nodes[i]
    x_b, y_b, z_b, idx_b = nodes[i+1]
    heapq.heappush(pq, [y_b-y_a, idx_a, idx_b])

nodes.sort(key= lambda x:x[2])
for i in range(n-1):
    x_a, y_a, z_a, idx_a = nodes[i]
    x_b, y_b, z_b, idx_b = nodes[i+1]
    heapq.heappush(pq, [z_b-z_a, idx_a, idx_b])

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True
total = 0
cnt = 0

# 크루스칼 알고리즘으로 체크. 남아 있는 힙의 크기가 많을 수 있으므로 cnt를 통해 간선의 수가 n-1이 되면 조기 종료한다.
while pq:
    cost, node1, node2 = heapq.heappop(pq)

    if union(node1, node2):
        total += cost
        cnt += 1
        if cnt == n-1: break

print(total)

