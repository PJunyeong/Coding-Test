import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        # 메모라이제이션
        return parents[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    parents[root2] = root1

def is_union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return True
    else: return False

for _ in range(m):
    cmd, node1, node2 = map(int, sys.stdin.readline().rstrip().split())

    if cmd == 0:
        # 합집합
        union(node1, node2)
    else:
        # 합집합 체크
        if is_union(node1, node2): print('YES')
        else: print('NO')

