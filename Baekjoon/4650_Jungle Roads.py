import sys
import heapq
import string

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

def Krsukal():
    total = 0
    edge_cnt = 0
    while pq:
        cur_cost, node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            total += cur_cost
            edge_cnt += 1
            if edge_cnt == n-1: break
    if edge_cnt == n-1: return total
    else: return -1

INF = sys.maxsize
letter_num = {letter:num for num, letter in enumerate(string.ascii_uppercase)}
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0: break
    pq = []
    for _ in range(n-1):
        edges = list(sys.stdin.readline().rstrip().split())
        node1 = letter_num.get(edges[0])
        for i in range(2, len(edges), 2):
            node2, cost = letter_num.get(edges[i]), int(edges[i+1])
            heapq.heappush(pq, [cost, node1, node2])
    parents = [i for i in range(n)]
    ans = Krsukal()
    print(ans)