import sys
import heapq
import string

n = int(sys.stdin.readline().rstrip())
letter_code = {letter:idx for idx, letter in enumerate(string.ascii_letters, start=1)}
parents = [i for i in range(n)]
pq = []
base = 0
for i in range(n):
    line = sys.stdin.readline().rstrip()
    for j in range(n):
        if line[j] != '0':
            base += letter_code.get(line[j])
            heapq.heappush(pq, [letter_code.get(line[j]), i, j])

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
edge_num = 0
while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    if union(node1, node2):
        total += cur_cost
        edge_num += 1
        if edge_num == n-1: break

if edge_num == n-1: print(base - total)
else: print(-1)


